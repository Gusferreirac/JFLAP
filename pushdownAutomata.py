
lines = ''
states = ''
input_symbols = ''
stack_symbols = ''
initial_state = ''
initial_stack = ''
final_states = ''
productions = ''

def read_automato_from_txt(file_path):
    global lines,states,input_symbols,stack_symbols,initial_state,initial_stack,final_states,productions

    with open(file_path, 'r') as file:
        lines = [line.rstrip() for line in file]
        states = lines[0].rstrip().split()
        input_symbols = lines[1].rstrip().split()
        stack_symbols = lines[2].rstrip().split()
        initial_state = lines[3][0]
        initial_stack = lines[4][0]
        final_states = lines[5].rstrip().split()
        productions = lines[6:]
        for i in range(len(productions)):
            productions[i] = productions[i].rstrip().split()

def apRun(inputString):
    stack = []
    inputString = inputString+'e'

    currentStackSymbol = initial_stack
    currentState = initial_state
    stack.append(initial_stack)
    for char in inputString:
        for production in productions:
            if ((production[0] == currentState) and (production[1] == char) and (production[2] == currentStackSymbol)):
                currentState = production[3]
                if(len(production[4]) == 2):
                    stack.append(char)
                elif(len(production[4]) == 3):
                    stack.append(char)
                    stack.append(char)
                elif ((production[4] == 'e') and (len(stack) != 1)):
                    stack.pop()
                    break
        currentStackSymbol = stack[len(stack)-1]

    if(currentState in final_states):
        return True
    else:
        return False