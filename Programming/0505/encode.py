lorenzDict = {"A": 11000, "B": 10011, "C": 1110, "D": 10010, "E": 10000, "F": 10110,
              "G": 1011, "H": 101, "I": 1100, "J": 11010, "K": 11110, "L": 1001,
              "M": 111, "N": 110, "O": 11, "P": 1101, "Q": 11101, "R": 1010,
              "S": 10100, "T": 1, "U": 11100, "V": 1111, "W": 11001, "X": 10111,
              "Y": 10101, "Z": 10001,
              "+": 11011, "/": 0, "9": 100, "8": 11111, "4": 1000, "3": 10}

KEY1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
KEY2 = ["A", "A", "B", "B"]

def xor(a, b):
    s = 0
    for i in range(4, -1, -1):
        b1 = a // (10 ** i) % 10
        b2 = b // (10 ** i) % 10
        s += b1 ^ b2
        s *= 10
    return s // 10

def parseInput(input_text):
    [key1_ind, key2_ind, plaintext] = input_text.split(",")
    return [int(key1_ind), int(key2_ind), plaintext.strip()]

def encode(input_array):
    [key1_ind, key2_ind, plaintext] = input_array
    str = ""
    for char in plaintext:
        key1_sec = KEY1[(key1_ind-1) % len(KEY1)]
        key2_sec = KEY2[(key2_ind-1) % len(KEY2)]
        print(char, key1_sec, key2_sec)
        print(lorenzDict[char], lorenzDict[key1_sec], lorenzDict[key2_sec])
        val = xor(xor(lorenzDict[char], lorenzDict[key1_sec]), lorenzDict[key2_sec])
        print(val)
        str += list(lorenzDict.keys())[list(lorenzDict.values()).index(val)]
        key1_ind += 1
        key2_ind += 1
    return str

print(encode(parseInput("10, 4, MOTK8YVBGAKN")))
