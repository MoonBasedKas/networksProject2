"""
Name: Kassidy Maberry
Project: Star Network
Date: 2024/11/01

Implementation of the frame class. This is used as a container 
for handling the information of a packet and for preparing 
the packet for when its sent.
"""

class frame:
    def __init__(self, src, dest, size, message) -> None:
        parts = [] 
        self.srcBin = self.intToBinary(src)
        self.destBin = self.intToBinary(dest)
        self.sizeBin = self.intToBinary(size)
        self.charsBin = self.messageToBinary(message)

    """
    This will be used to convert a frame into a byte stream.
    """
    def messagify(self):
        str = self.srcBin + self.destBin + self.sizeBin
        for i in self.charsBin:
            str += i
        return str

    """
    Converts a given integer into binary.
    """
    def intToBinary(self, num):
        ans = ""
        for i in range(7,-1, -1):
            if num // (2**i) == 1:
                num -= 2**i
                ans += '1'
            else:
                ans += '0'
        return ans
    
    """
    Converts a given string of characters into binary.
    """
    def messageToBinary(self, message):
        lis = []
        for char in message:
            lis.append(self.intToBinary(ord(char)))

        return lis
