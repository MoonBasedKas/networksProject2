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
        self.port = None
        self.messages = None
        self.nodeName = 0

    