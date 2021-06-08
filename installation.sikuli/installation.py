import os
import json

def read_default_pathfile (location):
    home_path = os.path.expanduser('~')
    open_file_name = 'extension_file'
    open_file_extension = 'json'
    file_details = home_path + '\\' + location + '\\' + open_file_name + '.' + open_file_extension

    if not os.path.exists(file_details):
        return "Error: Can not open file path"
    else:
    # read file
        with open(file_details, 'r') as jsonfile:
            data = jsonfile.read()

        # parse file
        obj = json.loads(data)

        return str(obj['version']), str(obj['download_path']), str(obj['default_filename']), str(obj['extension'])


try:
    home = os.path.expanduser('~')
    list_details = read_default_pathfile ('Desktop\Installation File Extension')
    cc_instaler = home + '\\' + list_details[1] + '\\' + list_details[2] + '_' + list_details[0] + '.' + list_details[3]
    print(cc_instaler)
    installer = App.open(cc_instaler)
except TypeError:
    e = sys.exc_info()[0]
    print('Cannot find file' + e)

except FileNotFoundError:
    e = sys.exc_info()[0]
    print('Cannot find file' + e)

sleep(2)
installer.focus()
assert waitVanish("installation_wizard.png", 20)

assert wait("set up.png", 20)
sleep(2)
type(Key.ENTER)
sleep(2)
type("a",Key.CTRL)
sleep(1)
type("c",Key.CTRL)

check_directory = Env.getClipboard()
default_directory_name = 'C:\Program Files\ControlCenter' + '_' + list_details[0]
print(check_directory)
print(default_directory_name)

if check_directory != default_directory_name:
    sleep(1)
    type(Key.BACKSPACE)
    sleep(1)
    type(default_directory_name)

sleep(1)
# Move on with default
type(Key.TAB * 2)
sleep(1)
type(Key.ENTER)
sleep(1)
type(Key.TAB * 2)
sleep(1)
type(Key.ENTER)
sleep(1)
type(Key.TAB * 5)
sleep(1)

## Check services
type("a",Key.CTRL)
sleep(1)
type("c",Key.CTRL)

check_service = Env.getClipboard()
default_service = 'dbWatch Control Center' + '_' + list_details[0]
print(check_service)
print(default_service)

if check_service != default_service:
    sleep(1)
    type(Key.BACKSPACE)
    sleep(1)
    type(default_service)

sleep(1)
type(Key.TAB * 4)
sleep(1)

## work directory
type("a",Key.CTRL)
sleep(1)
type("c",Key.CTRL)

check_work = Env.getClipboard()
default_work = 'C:\ProgramData\dbWatchControlCenter' + '_' + list_details[0]
print(check_work)
print(default_work)

if check_work != default_work:
    sleep(1)
    type(Key.BACKSPACE)
    sleep(1)
    type(default_work)

sleep(1)
type(Key.TAB * 5)
sleep(1)
type(Key.ENTER)
sleep(1)
type(Key.TAB * 3)
sleep(1)
type(Key.ENTER)
assert wait ("progress bar.png",20)
sleep(2)
type(Key.TAB)
sleep(1)
type(Key.ENTER)
sleep(1)
popup("Done Installing dbWatch version " + list_details[0])


