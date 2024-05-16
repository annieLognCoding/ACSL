import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(f'{__location__}/input.txt', 'r')
lines = file1.readlines()

n = None
ops = {}
acc = 0
vars = {}
branches = {}

def readInput(lines):
    global n, ops, vars, branches
    for i in range(len(lines)):
        if i == 0:
            n = lines[i].split()
        else:
            op = lines[i].strip()
            ops[i] = op
            line = op.split()
            if(len(line) == 3):
                code = line[1]
                if(code == "DC"):
                    vars[line[0]] = int(line[2])
                else:
                    branches[line[0]] = i

def calculate():
    global n, ops, acc, vars
    nind = 0
    ind = 1
    end = False
    while not end:
        op = ops[ind]
        line = op.split()
        code = None

        if(len(line) == 3):
            code = line[1]
            operand = line[2]
        elif(len(line) == 2):
            code = line[0]
            operand = line[1]
        elif(len(line) == 1):
            code = line[0]        
        
        if code == "DC" and line[0] not in vars:
            vars[line[0]] = int(operand)
        elif code == "LOAD":
            try:
                acc = int(operand[1:])
            except:
                acc = vars[operand]
        elif code == "STORE":
            vars[operand] = acc
        elif code == "ADD":
            try:
                acc += int(operand[1:])
            except:
                acc += int(vars[operand])
        elif code == "SUB":
            try:
                acc -= int(operand[1:])
            except:
                acc -= int(vars[operand])
        elif code == "MULT":
            try:
                acc *= int(operand[1:])
            except:
                acc *= int(vars[operand])
        elif code == "DIV":
            try:
                acc //= int(operand[1:])
            except:
                acc //= int(vars[operand])
        elif code == "BG":
            if(acc > 0):
                ind = branches[operand]
                continue
        elif code == "BE":
            if(acc == 0):
                ind = branches[operand]
                continue
        elif code == "BL":
            if(acc < 0):
                ind = branches[operand]
                continue
        elif code == "BU":
            ind = branches[operand]
            continue
        elif code == "READ":
            vars[operand] = int(n[nind])
            nind += 1
        elif code == "PRINT":
            print(acc)
        elif code == "END":
            end = True
        elif operand == "END":
            end = True
        
        ind += 1

readInput(lines)
calculate()
print(acc)


