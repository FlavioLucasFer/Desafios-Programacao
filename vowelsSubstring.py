def findSubstring(s, k):
    vowels = 'aeiou'

    i = 0
    biggerCount = 0
    biggerSubstring = ''

    while i < len(s):
        actualSubstring = s[i:i+k]
        
        if len(actualSubstring) == k:
            vowelsCount = 0
            
            for letter in actualSubstring:
                if (letter in vowels):
                    vowelsCount += 1
            
            if vowelsCount > biggerCount:
                biggerSubstring = actualSubstring
        

        i += 1
    
    if biggerSubstring != '':
        return biggerSubstring
    else:
        return 'Not found!'

print(findSubstring('herique', 3))
