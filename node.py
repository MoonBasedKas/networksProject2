"""
Name: Kassidy Maberry
Project: Star Network
Date: 2024/11/01

Implementation of the frame class. This is used as a container 
for handling the information of a packet and for preparing 
the packet for when its sent.
"""

import socket

class node:

    def __init__(self, name) -> None:
        self.port = int(name)
        self.nodeName = str(name)
        self.fInput = open("./nodeInput/node" + self.nodeName, "r")
        self.messages = self.fInput.readlines()

    