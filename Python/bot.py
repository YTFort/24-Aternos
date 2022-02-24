from tkinter import RIGHT, Label, Entry, Tk, Button
from javascript import require, On
mineflayer = require('mineflayer')
from configparser import ConfigParser
import threading, os, webbrowser
config = ConfigParser()
config.read('config.ini')

def getInputBoxValue():
	userInput = host.get()
	return userInput

def getInputBoxValue():
	userInput = port.get()
	return userInput

def getInputBoxValue():
	userInput = nick.get()
	return userInput

def startbot():
    bot = mineflayer.createBot({
      'host': f'{host.get()}',
      'port': port.get(),
      'username': f'{nick.get()}'
    })
    @On(bot, "login")
    def login(this):
        bot.chat(config.get('command', 'commandjoin'))
    @On(bot, "error")
    def error(err, *a):
        print("Connect ERROR", err, a)
    @On(bot, "kicked")
    def kicked(this, reason, *a):
        print("I was kicked", reason, a)
        print('reconnect'); startbot()
    @On(bot, "chat")
    def handle(this, username, message, *args):
        if username == bot.username:
            return
        elif message.startswith(config.get('command', 'pos')):
            say_position(username)
        elif message.startswith(config.get('command', 'aatrue')):
          bot.chat('AntiAFK start')
          bot.setControlState('forward', True)
          bot.setControlState('jump', True)
          bot.setControlState('sprint', True)
        elif message.startswith(config.get('command', 'aafalse')):
          bot.chat('AntiAFK stop')
          bot.clearControlStates()
    @On(bot, "spawn")
    def spawn(this):
        bot.chat("Spawned")
    @On(bot, "death")
    def death(this):
        bot.chat("I died, respawn")
    def say_position(username):
        p = bot.entity.position
        bot.chat(f"I am at {p.toString()}")

def stopb():
    os.system('taskkill /f /im node.exe')
    strtb.join()
    bb.configure(text = "start", command=startb)
strtb=threading.Thread(target=startbot)
def startb():
    strtb.start()
    bb.configure(text = "stop", command=stopb)

def updt():
	webbrowser.open('https://discord.gg/bjgpVAxgyE')

root = Tk()

root.geometry('293x123')
root.configure(background='#F0F8FF')
root.title('24 Aternos | By FORTCOTE')

host=Entry(root)
host.place(x=5, y=8)

port=Entry(root)
port.place(x=5, y=33)

nick=Entry(root)
nick.place(x=5, y=58)

Label(root, text='ip', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=138, y=4)

Label(root, text='ip port', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=138, y=30)

Label(root, text='nickname', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=137, y=55)

bb=Button(root, text='start', bg='#F0F8FF', font=('arial', 12, 'normal'), command=startb)
bb.pack(side=RIGHT, padx=20, pady=15)

Button(root, text='update', bg='#F0F8FF', font=('arial', 12, 'normal'), command=updt).place(x=12, y=84)

Label(root, text='Alpha 1.1', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=90, y=88)

root.mainloop()
