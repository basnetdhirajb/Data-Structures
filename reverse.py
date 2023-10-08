def reverseString(str):
    left = 0
    right = len(str)-1
    words = list(str)
    while left < right:
        words[left],words[right] = words[right],words[left]
        left+=1
        right-=1
    return "".join(words)

def reverseStringRec(str):
    if not str:
        return ''
    return reverseString(str[1:]) + str[0]
    
print(reverseString('yoyo mastery'))
print(reverseStringRec('yoyo mastery'))

