# WebSphere Failed Event Manager Cli
##Command Line Interface for manage failed events on websphere.

Add this script to your file sistem (Where the WebSphere installed).

To launch tool type:

    {path_to_wsadmin}/wsadmin.sh -lang jython -f {path_to_fem-cli}/fem-cli.py -user {user_alias} -password {password_alias}
Or you can create a .sh script with this command.

After launch you will be asked for input:

    1. Full event information      'D'
    2. Resubmit event              'R'
    3. Delete event                'S'
    4. Skip event                  'I'
 
Optionally you can pass an 'sourceModuleName' parameter, to specify a module name.
