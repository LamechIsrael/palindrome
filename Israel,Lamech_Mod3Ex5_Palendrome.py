#########################################
# CS 1110A - Programming in Python      #
# Module 3 - Exercise 5 - Palindromes   #
# Author: Lamech Israel                 #
# Date:   01/23/2023                    #
#########################################

# Create the palindrom method
def is_palindrome(s):
    string_length = len(s)
    half_length = 0
    before_half = 0
    after_half = 0
    
    
    # Acts if the string is odd
    if string_length % 2 != 0:
        # Get the letters on either side of the middle character
        half_length = int(string_length/2)
        before_half = half_length - 1
        after_half = half_length +1
        
    # Acts if the string is even
    else :
        # Get the letters in the middle of the string
        half_length = int(string_length/2)
        before_half = half_length - 1
        after_half = half_length   
        
    # Compares the string by examining the letter starting from the middle
    for i in range(half_length):
        if s[before_half-i] != s[after_half+i]:
            print('This is not a palindrome')
            return False
    print('This is a palindrome')
    return True
    
    
                
    

Running = True
while Running:
    
    Running = is_palindrome(input('Enter a word or phrase. I\'ll see if it\'s a palendrome. '))
    print('\n')
    
print('\Done')
exit()
                