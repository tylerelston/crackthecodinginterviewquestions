''' Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith" '''

# assumes given a list of string letters
def urlify(string, l):
    spaces = string[0:l].count(' ')
    newLen = l + spaces * 2
    index = newLen - 1
    #iterate from end to start of original word
    for i in range(l - 1, 0, -1):
        print(index)
        if string[i] == ' ':
            string[index] = '0'
            string[index - 1] = '2'
            string[index - 2] = '%'
            index -= 3
        else:
            string[index] = string[i]
            index -= 1
    return ''.join(string).strip()
    
assert('Mr%20John%20Smith' == urlify(list('Mr John Smith       '), 13))
