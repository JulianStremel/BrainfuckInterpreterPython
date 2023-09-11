from brainfuck import BrainfuckInterpreter


helloWorld = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++." # Hello World!
brainfuck = "+[[->]-[-<]>-]>.>>>>.<<<<-.>>-.>.<<.>>>>-.<<<<<++.>>++." #brainfuck

Interpreter = BrainfuckInterpreter()

Interpreter.loadCharBuffer(helloWorld)

Interpreter.interprete(debug=False)
