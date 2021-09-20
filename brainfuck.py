from sys import stdin, stdout


class BrainfuckInterpreter():
    class MemoryArray():
            
            def __init__(self):
                
                self.mainArray = [0,0]
                self.pointer = 0
            
            def increment_pointer(self):
                if self.pointer < len(self.mainArray) - 1:
                    self.pointer += 1
                elif self.pointer >= len(self.mainArray) - 1:
                    self.mainArray.append(0)
                    self.pointer += 1
                else:
                    print("pointer ERROR ( increment_pointer() )")
            
            def decrement_pointer(self):
                if self.pointer > 0:
                    self.pointer -= 1
                elif self.pointer <= 0:
                    self.pointer = 0
                else:
                    print("pointer ERROR ( decrement_pointer() )")
            
            def increment_byte(self):
                if self.mainArray[self.pointer] < 255 :
                    self.mainArray[self.pointer] += 1
                elif self.mainArray[self.pointer] == 255:
                    self.mainArray[self.pointer] = 0
                else:
                    print(self.mainArray[self.pointer])
                    print("memory ERROR ( increment_byte() )")
            
            def decrement_byte(self):
                if self.mainArray[self.pointer] > 0 :
                    self.mainArray[self.pointer] -= 1
                elif self.mainArray[self.pointer] == 0:
                    self.mainArray[self.pointer] = 255
                else:
                    print("memory ERROR ( decrement_byte() )")

            def read_input(self):
                self.mainArray[self.pointer] = ord(stdin.read(1))
            
            def write_output(self):
                stdout.write(chr(self.mainArray[self.pointer]))

            def dump(self):
                i = 0
                empty_list = []
                while i < len(self.mainArray) :
                    empty_list.append(str(self.mainArray[i]))
                    i+=1
                string= "|"
                print(string.join(empty_list))


    def __init__(self):
        self.charBuffer = ""
        self.charList = []
        self.charPointer = 0
        self.loopEntry = []
        self.memory = self.MemoryArray()

    def __str__(self):
        return self.charBuffer

    def __int__(self):
        return len(self.charBuffer)

    def __currentMemoryValue__(self):
        return self.memory.mainArray[self.memory.pointer]

    def flushCharBuffer(self):
        self.charBuffer = ""
        self.charList = []

    def loadCharBuffer(self,String):
        try:
            self.charBuffer = str(String)
        except:
            print("charBuffer loading ERROR")
        try:
            self.charList = list(self.charBuffer)
        except:
            print("charList loading ERROR")
        

    def interprete(self,debug=False):
        if self.charList != []:
            while self.charPointer < len(self.charList):

                if self.charList[self.charPointer] == "+":
                    self.memory.increment_byte()

                elif self.charList[self.charPointer] == "-":
                    self.memory.decrement_byte()

                elif self.charList[self.charPointer] == ">":
                    self.memory.increment_pointer()

                elif self.charList[self.charPointer] == "<":
                    self.memory.decrement_pointer()

                elif self.charList[self.charPointer] == ",":
                    self.memory.read_input()

                elif self.charList[self.charPointer] == ".":
                    self.memory.write_output()

                elif self.charList[self.charPointer] == "[":
                    self.loopEntry.insert(0,self.charPointer)
                    self.charPointer += 1
                    self.interprete()
                    
                elif self.charList[self.charPointer] == "]":
                    if self.__currentMemoryValue__()>0:
                        self.charPointer = self.loopEntry[0]
                    else:
                        self.loopEntry.pop(0)
                        if debug:
                            print("returned from loop")
                        return

                else:
                    pass
                
                if debug:
                    print(self.charList)
                    print("loop entrys:" + str(self.loopEntry))
                    print("char pointer: " + str(self.charPointer))
                    self.memory.dump()
                    print("current operation: " + self.charList[self.charPointer] + " selected byte: "+ str(self.memory.pointer) + " selected value: " + str(self.memory.mainArray[self.memory.pointer]) )
                    input()

                self.charPointer += 1
        else:
            print("no char to run in buffer")
            exit()
    






    