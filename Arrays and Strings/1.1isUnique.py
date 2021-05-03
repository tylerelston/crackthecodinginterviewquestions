# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def isUnique(string):
    unique = set()
    for s in string:
        if s in unique:
            return False
        unique.add(s)
    return True

def isUniqueNoStructures(string):
    if len(string) > 1:
        sorted(string)
        for i in range(len(string) - 1):
            if string[i] == string[i+1]:
                return False
    return True


assert(isUnique('abc') == True)
assert(isUnique('abcc') == False)

assert(isUniqueNoStructures('abc') == True)
assert(isUniqueNoStructures('abcc') == False)
