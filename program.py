import pyttsx3
import os
import time
import calendar
print('\t\t\tHello, I am Addy, your Windows Assistant')
pyttsx3.speak('Hello, I am addy, your windows assistant, How are you , how can i help you')
while True:
    print('\t----------------------------------------------------------------------------------')
    print('\tWhat is your requirements: ', end='')
    pyttsx3.speak('What is your requirements')
    p=input()
    if (('run' in p) or ('execute' in p) or ('open' in p) or ('launch' in p) or ('send' in p) or ('show' in p)):
        if ('email' in p) or ('email' in p) or ('Email' in p) or ('Gmail' in p) or ('mail' in p):
            print('\t\tIf you want to send Mail - [y]/[n]: ',end='')
            pyttsx3.speak('if you want to send mail using python then press yes')
            your_choice=input()
            if your_choice=="y":
                import smtplib as s
                ob=s.SMTP("smtp.gmail.com",587)
                ob.starttls()
                pyttsx3.speak('enter sender mail')
                sender_mail=input('\tEnter sender\'s Mail: ')
                pyttsx3.speak('enter sender msil passcode')
                mail_passcode=input('\tEnter Sender\'s Mail Passcode: ')
                ob.login(sender_mail,mail_passcode)
                pyttsx3.speak('write Reciver\'s Mail')
                rec_mail=input('\tWrite Your Reciver\'s Mail: ')
                pyttsx3.speak('write your mail subject')
                subject=input('\tWrite your Mail Subject: ')
                pyttsx3.speak('write your message')
                body=input('\tWrite Your Message: ')
                message="Subject:{}\n\n{}".format(subject,body)
                ob.sendmail(sender_mail,rec_mail,message)
                print("\tSend Your mail Sucessfully")
                pyttsx3.speak('your mail sent sucessfully')
            else:
                pyttsx3.speak('opening email')
                os.system('start  http://www.gmail.com/')
        elif (('notepad' in p) or ('editor' in p)):
            pyttsx3.speak('launching notepad')
            os.system('notepad')
        elif ('facebook' in p):
            pyttsx3.speak('opening facebook')
            os.system('start  http://www.facebook.com/')
        elif ('linkedln' in p):
            pyttsx3.speak('opening linkedln')
            os.system('start  http://www.linkedin.com/')
        elif (('media player' in p) or ('video player' in p)):
            pyttsx3.speak('launching windows media player')
            os.system('wmplayer')
        elif (('google' in p) or ('chrome' in p)):
            pyttsx3.speak('Launching chrome')
            os.system('chrome')
        elif (('opera' in p) or ('browser' in p)):
            pyttsx3.speak('Launching your opera browser')
            os.system('launcher')
        elif ('notepad++' in p) or ('pad editor' in p):
            pyttsx3.speak('Launching your notepad++')
            os.system('notepad++')
        elif ('calculator' in p):
            pyttsx3.speak('Opening your calculator')
            os.system('calc')
        elif (('mozilla' in p) or ('firefox' in p) or ('web' in p)):
            pyttsx3.speak('opening Mozilla firefox')
            os.system('firefox')
        elif ('bluetooth' in p):
            pyttsx3.speak('opening bluetooth')
            os.system('bthudtask')
        elif ('screen saver' in p):
            pyttsx3.speak('launching your screen saver')
            os.system('Bubbles')
        elif ('prompt' in p) or ('command' in p) or ('cmd' in p):
            pyttsx3.speak('opening your command prompt')
            os.system('start cmd.exe')
        elif ('host' in p) or ('window host' in p):
            pyttsx3.speak('launching your windows host')
            os.system('conhost')
        elif ('control panel' in p) or ('windows panel' in p) or ('panel' in p):
            pyttsx3.speak('Please wait, launching your Windows control panel')
            os.system('control')
        elif ('display color' in p) or ('color calibration' in p) or ('calibration' in p):
            pyttsx3.speak('wait I am launching your display color calibration')
            os.system('dccw')
        elif ('dvd player' in p):
            pyttsx3.speak('please wait i am launching your dvd player')
            os.system('dvdplay')
        elif ('private character' in p) or ('character editor' in p) or ('private editor' in p):
            pyttsx3.speak('wait I am launching your Private Character Editor')
            os.system('eudcedit')
        elif ('event viewer' in p) or ('event launcher' in p) or ('snapin launcher' in p):
            pyttsx3.speak('please wait I am opening your Event Viewer Launcher')
            os.system('eventvwr')
        elif ('file history' in p):
            pyttsx3.speak('opening file history')
            os.system('FileHistory')
        elif ('file transfer' in p) or ('bluetooth file transfer' in p) or ('bluetooth transfer' in p):
            pyttsx3.speak('wait launching your bluetooth file transfer')
            os.system('fsquirt')
        elif ('fax service' in p):
            pyttsx3.speak('launching your fax service')
            os.system('FXSSVC')
        elif ('game panel' in p):
            pyttsx3.speak('launching your game panel')
            os.system('GamePanel')
        elif ('group converter' in p) or ('program converter' in p):
            pyttsx3.speak('launching your windows program group converter')
            os.system('grpconv')
        elif ('hardware wizard' in p) or ('add wizard' in p):
            pyttsx3.speak('opening your hardware wizard')
            os.system('hdwwiz')
        elif ('tray' in p):
            pyttsx3.speak('launching tray')
            os.system('igfxTray')
        elif ('user service' in p) or ('mode service' in p) or ('eidi' in p):
            pyttsx3.speak('launching WiDi user mode service')
            os.system('IntelWiDiUMS64')
        elif ('sync center' in p):
            pyttsx3.speak('launching Microsoft Sync Center')
            os.system('mobsync')
        elif ('microsoft' in p) or ('windows' in p) or ('malicious' in p) or ('software' in p) or ('removal tool' in p):
            pyttsx3.speak('opening your microsoft windows software removal tool')
            os.system('MRT')
        elif ('system' in p) or ('configuration' in p) or ('utility' in p):
            pyttsx3.speak('opening system configuration utility')
            os.system('msconfig')
        elif ('paint' in p) or ('mspaint' in p) or ('microsoft' in p):
            pyttsx3.speak('please wait, i am opening your microsoft paint')
            os.system('mspaint')
        elif ('windows remote' in p) or ('remote assistance' in p) or ('windows assistance' in p):
            pyttsx3.speak('please wait, opening your windows remote assistance')
            os.system('msra')
        elif ('photo screen' in p) or ('photo saver' in p):
            pyttsx3.speak('plaese wait, ready to running your photo screen saver')
            os.system('PhotoScreensaver')
        elif ('cast device' in p) or ('device casting' in p):
            pyttsx3.speak('opening your device casting')
            os.system('WMPDMC')
        elif ('wordpad' in p):
            pyttsx3.speak('Please wait,  opening  your wordpad')
            os.system('wordpad')
        elif ('powerpoint' in p) or ('powerpnt' in p):
            pyttsx3.speak('please wait launching your microsoft powerpoint')
            os.system('start powerpnt')
        elif ('internet explorer' in p) or ('explorer' in p):
            pyttsx3.speak('launching your internet explorer')
            os.system('start iexplore')
        elif ('msword' in p) or ('ms word' in p):
            pyttsx3.speak('opening microsoft word')
            os.system('start winword')
        elif ('zoom' in p):
            pyttsx3.speak('opening zoom meeting')
            os.system('Zoom')
        elif ('computer' in p) or ('mycomputer' in p):
            pyttsx3.speak('opening my computer')
            os.system('start explorer')
        elif ('program' in p) or ('process' in p):
            pyttsx3.speak('opening program')
            os.system('tasklist')
        elif ('setting' in p) or ('settings' in p):
            pyttsx3.speak('opening your setting')
            os.system('start ms-settings:')
        elif ('ip' in p):
            pyttsx3.speak('opening ip address')
            os.system('ipconfig | find /N "IPv4"')
        elif ('youtube' in p):
            pyttsx3.speak('opening youtube')
            os.system('start  http://www.youtube.com/')
        elif ('camera' in p):
            pyttsx3.speak('opening camera')
            os.system('start microsoft.windows.camera:')
        elif ('change' in p) or ('color' in p) or ('colour' in p):
            pyttsx3.speak('opening colour changing file')
            os.system('color f0')
        elif ('what' in p) or ('date' in p):
            pyttsx3.speak('today date')
            os.system('date')
        elif ('py' in p) or ('python' in p):
            pyttsx3.speak('opening python')
            a='cmd.exe /K python'
            os.system('start {}'.format(a))
        elif ('clear' in p) or ('delete' in p) and (('cache' in p) or ('temp' in p)):
            pyttsx3.speak('clearing your cache data')
            os.system('start %temp%')

    elif ('exit' in p) or ('close' in p) or ('terminate' in p):
        print('Thanks for using me')
        pyttsx3.speak('Thanks for using me')
        print('GOOD BYE')
        break
    else:
        print('This Application is not installed in your System')
        
                          
            
        
        
         
                          
            
        
            

            
