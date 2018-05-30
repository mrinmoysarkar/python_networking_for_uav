#!/usr/bin/env python

import socket
from appJar import gui

# handle button events
def press(button):
    if button == "Exit":
        app.stop()
    elif button == "Initialize":
        TCP_IP = '192.168.1.59'
        TCP_PORT = 7777
        BUFFER_SIZE = 1024
        MESSAGE = "init"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        s.close()
        TCP_IP = '192.168.198.129'
        TCP_PORT = 7777
        BUFFER_SIZE = 1024
        MESSAGE = "init"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        s.close()
        print("init")
    elif button == "Start":
        TCP_IP = '192.168.1.59'
        TCP_PORT = 7777
        BUFFER_SIZE = 1024
        MESSAGE = "start"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        s.close()
        TCP_IP = '192.168.198.129'
        TCP_PORT = 7777
        BUFFER_SIZE = 1024
        MESSAGE = "start"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        s.close()
        print("start")
    elif button == "Emergency Stop UAV1":
        TCP_IP = '192.168.1.59'
        TCP_PORT = 7777
        BUFFER_SIZE = 1024
        MESSAGE = "estop"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        s.close()
        print("stop1")
    elif button == "Emergency Stop UAV2":
        TCP_IP = '192.168.198.129'
        TCP_PORT = 7777
        BUFFER_SIZE = 1024
        MESSAGE = "estop"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        #data = s.recv(BUFFER_SIZE)
        s.close()
        print("stop2")

if __name__ == "__main__":
	# create a GUI variable called app
    app = gui("UAV Control Panel", "400x200")
    app.setFont(18)
    app.addButton("Exit", press)
    app.addButton("Initialize", press)
    app.addButton("Start", press)
    app.addButton("Emergency Stop UAV1", press)
    app.addButton("Emergency Stop UAV2", press)
    app.go()