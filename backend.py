import time
import os
import shutil

def createtxt(name,url, email):
    now = time.localtime()
    timern = time.strftime("%H:%M:%S", now)   
    f = open(f"{timern}.txt", 'w')
    f.write(f"Name: {name} \nURL: {url} \nEmail: {email}")
    f.close()
    shutil.move(os.path.join('G:\dsc-vanity-url', f'{timern}.txt'), 'url-requests/')

createtxt('idk', 'hehe.com', 'notmyemail')