from brainfuck import BrainfuckInterpreter


helloWorld = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++." # Hello World!
brainfuck = "+[[->]-[-<]>-]>.>>>>.<<<<-.>>-.>.<<.>>>>-.<<<<<++.>>++." #brainfuck

n = BrainfuckInterpreter()
n.loadCharBuffer(helloWorld)

n.interprete(debug=False)






