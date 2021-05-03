# Given two strings, write a method to decide if one is a permutation of the other

# o(n log n) runtime, o(n) space complexity
def checkPermutation(str1, str2):
    if len(str1) == len(str2):
        if sorted(str1) == sorted(str2):
            return True
    return False

def checkPermutationNoSort(str1, str2):
    if len(str1) == len(str2):
        letters = {}
        
        for c in str1:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1

        for c in str2:
            if c not in letters:
                return False
            letters[c] -= 1
            if letters[c] < 0:
                return False
            
        return True
    return False

assert(checkPermutation('abc', 'cba') == True)
assert(checkPermutation('abc', 'abcdef') == False)

assert(checkPermutationNoSort('abc', 'cba') == True)
assert(checkPermutationNoSort('abc', 'abcdef') == False)
