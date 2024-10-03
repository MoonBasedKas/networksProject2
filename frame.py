"""
Name: Kassidy Maberry
Project: Star Network
Date: 2024/11/01

Implementation of the frame class. This is used as a container 
for handling the information of a packet and for preparing 
the packet for when its sent.
"""

class frame:
    def __init__(self, data) -> None:
        # This is a type of psuedo overloading since python does not support it
        if type(data) == type([]):
            self.buildIntWise(data) # List input
        else:
            self.buildBitWise(data) # String Input

    """
    Debugging method will print out a packet.
    """
    def __str__(self):
        str = "{} -> {} \t size: {}\n{}".format(self.srcBin, self.srcInt, self.sizeInt, self.messageChar)
        return str

    """
    Builds the frame if it was built at the node.
    """
    def buildIntWise(self, data):
        self.srcInt = data[0]
        self.destInt = data[1]
        self.sizeInt = data[2]
        self.messageChar = data[3]
        self.srcBin = self.intToBinary(data[0])
        self.destBin = self.intToBinary(data[1])
        self.sizeBin = self.intToBinary(data[2])
        self.messageBin = self.messageToBinary(data[3])

    """
    Builds the node if it was recieved at the bit level.
    """
    def buildBitWise(self, data):
        # Takes the first 8 bits of scratch then remove it.
        scratch = data
        self.srcBin = scratch[0:8] 
        scratch = scratch[8:]
        self.destBin = scratch
        scratch = scratch[8:]
        self.sizeBin = scratch
        scratch = scratch[8:]
        self.charsBin = scratch
        self.srcInt = self.binToInt(self.srcBin)
        self.destInt = self.binToInt(self.destBin)
        self.sizeInt = self.binToInt(self.sizeBin)
        self.messageChar = self.messageToChar(self.charsBin)


    """
    Converts the frame class into an actual frame to send.
    """
    def packetize(self):
        message = ""
        message += self.srcBin
        message += self.destBin
        message += self.sizeBin
        for i in self.charsBin:
            message += i
        return message

    """
    This will be used to convert a frame into a byte stream.
    """
    def messagify(self):
        str = self.srcBin + self.destBin + self.sizeBin
        for i in self.messageChar:
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
    Convert a binary number into a base 10 number.
    """
    def binToInt(self, num):
        sum = 0
        for i in range(0,8):
            if num[i] == "1":
                sum += 2**i
        return sum
    
    """
    Converts a message into characters.
    """
    def messageToChar(self, message):
        temp = ""
        res = ""
        while message != "":
            temp = message[0:8]
            message = message[8:]
            res += ascii(self.binToInt(temp))
        return res
    
    """
    Converts a given string of characters into binary.
    """
    def messageToBinary(self, message):
        lis = []
        for char in message:
            lis.append(self.intToBinary(ord(char)))

        return lis


x = frame([1, 2, 3, ""])
print(x)
z = frame(x.messagify())
print(z)
print(z.srcBin)