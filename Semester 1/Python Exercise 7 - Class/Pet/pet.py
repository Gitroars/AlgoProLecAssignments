class Pet:
    def __init__(self, name="Not provided", type="Not provided", age=0):
        self.__name = name
        self.__type = type
        self.__age = age

    def setName(self, name):
        self.__name = name

    def setType(self, type):
        self.__type = type

    def setAge(self, age):
        self.__age = age

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getAge(self):
        return self.__age

    def __str__(self):
        return "Name:{} Type:{} Age:{}".format(self.getName(), self.getType(), self.getAge())
