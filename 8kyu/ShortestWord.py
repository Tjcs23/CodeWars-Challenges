'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''

def find_short(s):
    # your code here
    l = []
    count = 0
    for x in s:
        if x == " ":
            l.append(count)
            count = 0
        else:
            count+=1
    l.append(count)
    return min(l) # l: shortest word length

'''
Looking through other solutions I realize I should have made use of the split method 
and then iterate over the string of words returning the min of len(x)

Ex.
def find_short(s):
    results = []
    for x in s.split():
        results.append(len(x))
    return min(results)
'''