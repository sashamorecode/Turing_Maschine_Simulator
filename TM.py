from enum import Enum
import copy
class InnerNode:
    def __init__(self,val):
        self.value = val
        self.right = None
        self.left = None
class Node:
    def __init__(self, val):
        self.__current = InnerNode(val)

    def step(self, direction):
        if direction == step.L:
            self.left()
        if direction == step.R:
            self.right()

    def right(self):
        if self.__current.right == None:
            newNode = InnerNode("B")
            newNode.left = self.__current
            self.__current.right = newNode
        self.__current = self.__current.right
    def left(self):
        if self.__current.left == None:
            newNode = InnerNode("B")
            newNode.right = self.__current
            self.__current.left = newNode
        self.__current = self.__current.left

    def val(self):
        return self.__current.value

    def setVal(self, val):
        self.__current.value = val
class step(Enum):
    L = -1
    N = 0
    R = 1

class State:
    def __init__(self,name):
        self.name = name
        self.transition = {"0": None, "1": None, "B":None}

    def __str__(self):
        return str(self.name)

    def setTransition(self,readLetter,state,writeLetter, step:step):
        self.transition[readLetter] = [state,writeLetter,step]


    def read(self, letter):
        try:
            return self.transition[letter]
        except:
            return None

def printBand(a:Node):
    current = a
    #while current.val() != "B":
    for x in range(5):
        current.left()
    for x in range(10):
        print(current.val(),end="|")
        current.right()
    for x in range(5):
        current.left()
class TM:
    def __init__(self, initState:State, endState:State):
        self.initState = initState
        self.endState = endState
        self.inputAlphabeat = ["0","1"]
        self.bandAlphabeat = ["0","1","B"]
        self.head = Node("B")
        self.currentState = self.initState
        self.startOfBand = self.head

    def start(self, input_tm):
        print("input:", input_tm)
        for letter in input_tm:
            self.head.setVal(letter)
            self.head.right()
        self.head.left()
        while(self.head.val() != "B"):
            self.head.left()
        self.head.right()



    def next(self):
        instructions = self.currentState.read(self.head.val())
        if instructions != None:
            print("   The instructions from, ", self.currentState.name, " with input ", self.head.val(), "->", instructions[0].name," write",instructions[1], instructions[2])
            self.currentState = instructions[0]
            self.head.setVal(instructions[1])
            self.head.step(instructions[2])

            if self.currentState == self.endState:
                print("Reached End State (Accepted)")
        else:
            self.currentState = self.endState
            print("Not Accepted")

    def run(self):
        print("         cur")
        print("          ↓")
        while self.currentState != self.endState:
            printBand(self.startOfBand)
            self.next()


qinit = State("qinit")
q0 = State("q0")
q1 = State("q1")
qend = State("qend")

qinit.setTransition("0", q0, "0", step.R)
qinit.setTransition("1", q1, "1", step.R)
qinit.setTransition("B", qend, "B", step.N)

q0.setTransition("1", q1, "1", step.R)
q0.setTransition("B", qend, "B", step.N)

q1.setTransition("0", q0, "0", step.R)
q1.setTransition("B", qend, "B", step.N)


changL = TM(qinit,qend)
changL.start("1010")
changL.run()