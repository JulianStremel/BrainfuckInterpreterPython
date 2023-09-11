# BrainfuckInterpreterPython REPO

BrainfuckInterpreterPython is my personal repo for my own python based Brainfuck-Interpreter implementation :)

Have fun :)

## Usage
```python
# first you need to initialize the interpreter class
Interpreter = BrainfuckInterpreter()

# then load the string to interpret
Interpreter.loadCharBuffer("YOUR STRING HERE")

# interprete and watch output
Interpreter.interprete()

# (optional you can use the debug=True argument to single Step (using ENTER) through the string and watch the execution in detail)
Interpreter.interprete(debug=True)
```
