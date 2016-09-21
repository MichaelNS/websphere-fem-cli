# WebSphere Failed Event Manager Cli
##Command Line Interface for manage failed events on websphere.

Add this script to your file sistem (Where the WebSphere installed).

To launch tool type:

    {path_to_wsadmin}/wsadmin.sh -lang jython -f {path_to_fem-cli}/fem-cli.py -user {user_alias} -password {password_alias}
Or you can create a .sh script with this command.

After launch you will be asked for input:

    ******************************************************
    147 ID:414d51204342514d2020202020202020f33dcf5450020010 JMS [ Mon Feb 16 16:13:19 MSK 2015 ] None
    Full event information      'I'
    Resubmit event              'R'
    Delete event                'D'
    Skip event                  'S'

After type I:

    MessageID:  A201D8E9FA97FAC5_24000017
    FailureDateTime:  Thu Mar 19 17:14:13 MSK 2015
    Failure Message:  com.ibm.websphere.sca.ServiceRuntimeException: com.ibm.bpe.api.RuntimeFaultException: [...]
    Resubmit event              'R'
    Delete event                'D'
    Skip event                  'S'
 
Optionally you can pass an 'sourceModuleName' parameter, to specify a module name.
