word = input('Enter the word you want to check:')

def palindromeCheck(word):
    len_word = len(word)

    first_half_word = word[0:0+int(len_word/2)].lower()
    if len_word % 2 == 0:
        second_half_word = ''.join(reversed(word[int(len_word/2):len_word].lower()))
    else:
        second_half_word = ''.join(reversed(word[((int(len_word/2)+1)):len_word].lower()))

    if first_half_word == second_half_word:
        print(word + ' is a palindrome')
    else:
        print(word + ' is not a palindrome')


palindromeCheck(word)
