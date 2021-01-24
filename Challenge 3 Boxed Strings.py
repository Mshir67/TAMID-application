var1 = input('Enter a sentence: ');

list1 = var1.split();

longestString = ""

length = len(list1);

maxLength = [];

def wordCount(size, words):
    for i in range(size):
        maxLength.append(len(words[int(i)]))               # places the lengths of words into a list


    



wordCount(length,list1);                                    # calls function and passes variables

maxStars = max(maxLength)                                


print(longestString)

def Box(size,words):
    for x in range(maxStars+5):                             # first line of stars
        print("*", end ="")

    print("\n", end="")                                     # starts a line for when the first word is printed
    for x in range(size):                        
                                      
        print("* " + words[x], end="")                      # prints the first star and the word of the sentence
    

        for y in range(len(words[int(x)])+2,maxStars+3):    # prints spaces depending on how long the word
            print(" ", end="")                               

        print(" *")                                          
                           
        
            
    for x in range(maxStars+5):                              # prints last line of stars
        print("*", end ="")

Box(length,list1);                                          # calls function and passes variables
            





    
    
    
