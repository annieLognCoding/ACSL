operators = {"ter": ["@", ">"], "bi": ["+", "-", "*"], "uni":["|"]}

def evaluate(elem, queue):    
    try:
        return int(elem)
    except:
        if elem in operators["ter"]:
            a = evaluate(queue.pop(), queue)
            b = evaluate(queue.pop(), queue)
            c = evaluate(queue.pop(), queue)
            if(elem == "@"):
                return b if a > 0 else c
            else:
                return max([a, b, c])
        elif elem in operators["bi"]:   
            right = evaluate(queue.pop(), queue)
            left = evaluate(queue.pop(), queue)
            if elem == "+":
                return right + left
            if elem == "-":
                return right - left
            if elem == "*":
                return right * left
        elif elem in operators["uni"]:
            a = evaluate(queue.pop(), queue)
            return abs(a)

def readInput(str):
    arr = str.split()
    return list(reversed(arr))

queue = readInput("| * @ - 1 6 34 12 > - 990 1000 * -2 3 + -51 49")
first = queue.pop()
print(evaluate(first, queue))


"""
* + 4 5 - 3 -1
@ - 8 9 82 46
@ | - -8 10 82 46
+ > 8 * 2 7 9 6
| * @ - 1 6 34 12 > - 990 1000 * -2 3 + -51 49

"""
    