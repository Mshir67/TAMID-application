print("Welcome to TAMID calculator")

yn = input("Would you like to calculate something (y/n): ")                             



# loop that initiates the calculator
# asks for user inputted values
# then stores the value in formula as a string
# formula is then evaluated. if it works then answer is outputted
# if doesn't work either a divide by zero error occurs or another error
# at the end the if statement checks for if n is inputted in the beginning or when the while loop is broken

while (yn == "y"):

    
    value1 = input("Please enter the first number: ")                                   
    
    value2 = input("Please enter the second number: ")                                  

    function = input("Please enter your function: ")                                    

    formula = ""                                                                        
    def number():
        global formula

        formula = str(value1) + str(function) + str(value2)                             

        
        try:
            answer = eval(formula)                                                      
            print("Your result is: ", end="")                                           
            print(answer)                                                               
        except:
            if (value2 == "0" and function == "/"):                                     
                print("You cannot divide by zero! Try again")
            else:                                                                       
                print("There was an error. Try again")
            
    
    number();   # calls function
    yn = input("Would you like to calculate something (y/n): ")                         

    
    
if (yn == "n"):    # stops the calculator 
    print("Thanks for coming")



                  


