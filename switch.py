"""
Name: Kassidy Maberry
Project: Star Network
Date: 2024/11/01

Implementation of the frame class. This is used as a container 
for handling the information of a packet and for preparing 
the packet for when its sent.
"""

class switch:

    def __init__(self) -> None:
        self.connections = []

    """
    Builds sockets to be lisetened to.
    """
    def buildConnects(self):
        pass