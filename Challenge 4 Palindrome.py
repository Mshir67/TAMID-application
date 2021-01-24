string1 = input("Please enter a string: ")    # user inputted word

string2 = string1[::-1]    # reverses string


def Palindrome():
    if (string1 == string2):     # indicates palindrome 
        print(string1 + " is a palindrome")
    else:
        print(string1 + " is not a palindrome")

Palindrome();    # calls function
 
