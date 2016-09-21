def getFailedEventManager():
    objstr = AdminControl.completeObjectName('WebSphere:*,type=FailedEventManager')
    return objstr
def getJmxFailedEventManager(mgrName):
    jmxFeMgr = AdminControl.makeObjectName(mgrName)
    return jmxFeMgr
def getAllFailedEventCount():
    objstr = getFailedEventManager()
    jmxFeMgr = getJmxFailedEventManager(objstr)
    totalFailedEventCount = AdminControl.invoke(jmxFeMgr, 'getFailedEventCount')
    print "Total Failed Event Count: ", totalFailedEventCount 
    return totalFailedEventCount
def getAllFailedEvents():
    objstr = getFailedEventManager()
    jmxFeMgr = getJmxFailedEventManager(objstr)
    print "FailedEventManager:", jmxFeMgr
    msglist = AdminControl.invoke_jmx(jmxFeMgr, 'getAllFailedEvents', [0], ['int'])
    return msglist   
def getFEListByModule(sourceModuleName):
    sourceComponentName = "*"
    pagesize = 0
    objstr = getFailedEventManager()
    jmxFeMgr = getJmxFailedEventManager(objstr)
    msglist=AdminControl.invoke_jmx(jmxFeMgr, 'getFailedEventsForSource', [sourceModuleName, sourceComponentName, 0], ['java.lang.String', 'java.lang.String', 'int'])
    return msglist   
def printFailedEvents(msglist):
    i = 0
    for fe in msglist:
        i += 1 
        print i, fe.getMsgId(), fe.getType(), fe.getFailureDateTime(), fe.getSourceModuleName()
def printFailedEventDetails(messageId):
    objstr = getFailedEventManager()
    jmxFeMgr = getJmxFailedEventManager(objstr)
    fep = AdminControl.invoke_jmx(jmxFeMgr, 'getFailedEventWithParameters', [messageId], ['java.lang.String'])
    print "MessageID: ", messageId
    print "FailureDateTime: ", fep.getFailureDateTime()
    print "Failure Message: " , fep.getFailureMessage()   
def resubmitFailedEvent(messageId):
    msglist = getAllFailedEvents()
    from java.util import ArrayList
    msgIdList = ArrayList()
    for fe in msglist: 
        if (messageId == fe.getMsgId()):
            print "resubmitFailedEvent: ", fe.getMsgId()
            msgIdList.add(fe)
    resubmitFailedEventsList(msgIdList)   
def resubmitFailedEventsList(msgIdList):
    objstr = getFailedEventManager()
    jmxFeMgr = getJmxFailedEventManager(objstr)
    AdminControl.invoke_jmx(jmxFeMgr, 'resubmitFailedEvents', [msgIdList], ['java.util.List'])
def discardFailedEvent(messageId):
    msglist = getAllFailedEvents()
    from java.util import ArrayList
    msgIdList = ArrayList()
    for fe in msglist:
        if (messageId == fe.getMsgId()):
            print "discardFailedEvent: ", fe.getMsgId()
            msgIdList.add(fe)
    discardFailedEventsList(msgIdList)
def discardFailedEventsList(msgIdList):
    objstr = getFailedEventManager()
    jmxFeMgr = getJmxFailedEventManager(objstr)
    AdminControl.invoke_jmx(jmxFeMgr, 'discardFailedEvents', [msgIdList], ['java.util.List'])
def manageFailedEvents(sourceModuleName):
    if ('' == sourceModuleName):
        msglist = getAllFailedEvents() 
    else:
        msglist = getFEListByModule(sourceModuleName)
    i = msglist.size()
    while (i > 0):
        i -= 1
        fe = msglist.get(i)
        print '******************************************************'
        print i, fe.getMsgId(), fe.getType(), '[', fe.getFailureDateTime(), ']', fe.getSourceModuleName()
        value = raw_input("Full event information      'D'\nResubmit event              'R'\nDelete event                    'S'\nSkip event               'I'\n")
        if ('D' == value or 'd' == value):
            printFailedEventDetails(fe.getMsgId())
            value = raw_input("Resubmit event              'R'\nDelete event                    'S'\nSkip event               'I'\n")
        if ('R' == value or 'r' == value):
            resubmitFailedEvent(fe.getMsgId())
        if ('S' == value or 's' == value):
            discardFailedEvent(fe.getMsgId())
manageFailedEvents('')