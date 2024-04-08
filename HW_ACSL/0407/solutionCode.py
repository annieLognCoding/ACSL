def powerN(base, n):
    if(n == 0): return 1
    return powerN(base, n-1) * base

def noX(str):
    if(len(str) <= 1): return "" if str == "x" else str
    return noX(str[1:]) if (str[0] == "x") else str[0] + noX(str[1:])

def parenBit(str):
    if(len(str) == 0): return str
    if(str[0] != "("): return parenBit(str[1:])
    if(str[-1] != ")"): return parenBit(str[:-1])
    return str

def strDist(str, sub):
    strLen = len(str)
    subLen = len(sub)
    if(strLen < subLen): return 0
    if(str[:subLen] == sub):
        if(str[strLen - subLen:] == sub): return strLen
        return strDist(str[:-1], sub)
    return strDist(str[1:], sub)

def groupSum(start, nums, target):
    if(target == 0): return True
    if(start == len(nums)): return False
    return groupSum(start + 1, nums, target - nums[start]) or groupSum(start + 1, nums, target)

def groupSum6(start, nums, target):
    if(start == len(nums)): return target == 0
    if(nums[start] == 6): return groupSum6(start + 1, nums, target - nums[start])
    return groupSum6(start + 1, nums, target - nums[start]) or groupSum6(start + 1, nums, target)


if __name__ == "__main__":
    print(strDist("catcowcat", "cow"))
    print(strDist("catcowcat", "cat"))
    print(strDist("cccatcowcatxx", "cat"))
    print(strDist("hiHellohihihi", "hi"))
    print(strDist("abccatcowcatcatxyz", "cat"))

