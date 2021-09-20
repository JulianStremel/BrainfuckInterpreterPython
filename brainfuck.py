from sys import stdin, stdout


class BrainfuckInterpreter():
    
    class MemoryArray():

            # initializing memory array with 1 Byte        
            def __init__(self):
                self.mainArray = [0]
                self.pointer = 0
            
            # moves memory pointer to next byte (array is dynamcly allocated and pointer will NOT rollover)
            def increment_pointer(self):
                if self.pointer < len(self.mainArray) - 1:
                    self.pointer += 1
                elif self.pointer >= len(self.mainArray) - 1:
                    self.mainArray.append(0)
                    self.pointer += 1
                else:
                    print("pointer ERROR ( increment_pointer() )")
            
            # moves memory pointer to previous byte (pointer will NOT rollover if bellow 0 [this can be used as an anchoring mechanism])
            def decrement_pointer(self):
                if self.pointer > 0:
                    self.pointer -= 1
                elif self.pointer <= 0:
                    self.pointer = 0
                else:
                    print("pointer ERROR ( decrement_pointer() )")
            
            # increments current memory location by one bit (incrementing 255 will rollover to 0)
            def increment_byte(self):
                if self.mainArray[self.pointer] < 255 :
                    self.mainArray[self.pointer] += 1
                elif self.mainArray[self.pointer] == 255:
                    self.mainArray[self.pointer] = 0
                else:
                    print(self.mainArray[self.pointer])
                    print("memory ERROR ( increment_byte() )")
            
            # decrements current memory location by one bit (decrementing 0 will rollover to 255)
            def decrement_byte(self):
                if self.mainArray[self.pointer] > 0 :
                    self.mainArray[self.pointer] -= 1
                elif self.mainArray[self.pointer] == 0:
                    self.mainArray[self.pointer] = 255
                else:
                    print("memory ERROR ( decrement_byte() )")

            # read single ascii char value from stdin into current memory location
            def read_input(self):
                self.mainArray[self.pointer] = ord(stdin.read(1))
            
            # write current memory value as ascii char to stdout
            def write_output(self):
                stdout.write(chr(self.mainArray[self.pointer]))

            # dumps a map of the memory and its values in human readable form (used for debugging purposes)
            def dump(self):
                i = 0
                dump_list = []
                while i < len(self.mainArray) :
                    dump_list.append(str(self.mainArray[i]))
                    i+=1
                string= "|"
                print(string.join(dump_list))


    # initializing interpreter with fresh memory array
    def __init__(self):
        self.charBuffer = ""                # string which stores the initial string
        self.charList = []                  # list of the characters of the initial string
        self.charPointer = 0                # pointer to the current char in the charList
        self.loopEntry = []                 # stores char pointer location for loop entrys to jump back to
        self.memory = self.MemoryArray()    # dynamic memory array on which the actions are performed

    # calling the str() method on the class will return the current char buffer
    def __str__(self):
        return self.charBuffer

    # calling the int() method on the class will return the length of the current char buffer 
    def __int__(self):
        return len(self.charBuffer)

    # returns the current memory value
    def __currentMemoryValue__(self):
        return self.memory.mainArray[self.memory.pointer]

    # emptys the current char buffer (and char list)
    def flushCharBuffer(self):
        self.charBuffer = ""
        self.charList = []

    # loads a string into the char buffer and makes a list of it
    def loadCharBuffer(self,String):
        try:
            self.charBuffer = str(String)
        except:
            print("charBuffer loading ERROR")
        try:
            self.charList = list(self.charBuffer)
        except:
            print("charList loading ERROR")
        
    # interpretes the currently loaded char buffer with all io actions
    def interprete(self,debug=False):
        
        # checking for chars in charList
        if self.charList != []:

            # using charPointer to walk over the string
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
                    self.interprete(debug)
                    
                elif self.charList[self.charPointer] == "]":
                    if self.__currentMemoryValue__()>0:
                        self.charPointer = self.loopEntry[0]
                    else:
                        self.loopEntry.pop(0)
                        if debug:
                            print("returned from loop")
                        return

                else:
                    # here we could remove non interpretable character from string and char list 
                    pass
                
                if debug:
                    # debugging output
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
    






    