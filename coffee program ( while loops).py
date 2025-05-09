# Demonstrate how to use a while loop
# Author: Elaine Labuschane
# Date: 09/05/2025
# Version 1

# While loops
'''keep_going = "" # The variable contains an empty string
while keep_going == "":
    
    like_coffee=input("Do you like coffee")

    if like_coffee=="Yes":
        print("That is great, I like coffee too,")
        keep_going="finished"

    if like_coffee=="No":
        print(" That is sad, Why not?,")
        keep_going="finished"'''
     
     
# Version 2 Make the program more pythonic

keep_going= ""
while keep_going== "":
    # .lower converts the answer to lower case
    like_coffee=input(" Do you like coffee").lower()
    if like_coffee== "yes" or like_coffee== "y":
        print("That is great, I like coffee too,")

    elif like_coffee=="no" or like_coffee=="n":
        print("You are miising out!")    

        like_tea=input("Do you like tea instead,").upper()

        if like_tea=="YES" or like_tea=="Y":
           print (" Good for you. Give coffee another try:),")
        elif like_tea=="NO" or like_tea=="N":
            print("I am sorry. That is all I have for now,")  
        else:
            print("I don't understand please answer with either yes or no,")      
    
    else:
        print("I don't understand please answer with either yes or no,")  

    keep_going= input(" Press enter to countied of any other kep to quit")             
                 
          



        

   


