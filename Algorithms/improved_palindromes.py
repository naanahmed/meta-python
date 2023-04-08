def isPalindrome(word):
    startIndex = 0
    endIndex = len(word)-1
    for i in range(startIndex, endIndex):
        if word[startIndex] != word[endIndex]:
            return False
        print(word[startIndex], word[endIndex])
        startIndex +=1
        endIndex -=1
    print(True)


isPalindrome('nataan')
