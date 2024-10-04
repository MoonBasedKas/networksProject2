"""
Name: Kassidy Maberry
Project: Star Network
Date: 2024/11/01

Implementation of the frame class. This is used as a container 
for handling the information of a packet and for preparing 
the packet for when its sent.
"""

import socket
import select

class switch:

    def __init__(self) -> None:
        self.connections = []

    """
    Builds sockets to be lisetened to.
    """
    def buildConnects(self, nodes):
        self.socks = []
        self.ports = []
        con = None
        offset = 0
        for i in range(nodes):
            while True:
                con = self.openConnection(i + 5000 + offset)
                if con == None:
                    offset += 1
                else:
                    break
            self.port.append(i + 5000 + offset)
            self.socks.append(con)

    """
    Accepts all of the connections for all open ports.
    """
    def acceptConnects(self):
        for i in self.socks:
            self.connections.append(i.accept())


    def monitorConnects(self):
        readableConnections = []
        while True:
            readableConnections = select.select(self.connections, [], [])
            for z in readableConnections:
                msg = z[0].recv(128).decode("ascii")
                print("Node recieved: " + msg.strip(), end="\n")
                msg = ""



    """
    Attempts to open a port for other nodes to connect to. If it fails there is a port 
    conflict and terminates the program.
    """
    def openConnection(port):
        try:
            con = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
            con.bind((socket.gethostname(), port))
            con.listen(5)
        except OSError:
            print("Error | Port conflict! Port is currently in use edit config file or close the port")
            return None # If None don't decrement instead try again with a new port.
        return con