####################################################################################################################################
#This is one of another project by Innovation University of Australia for Automatic Grading System
#This program allows lecturer to automatically calculate the final marks of the students
#The inputs provided are 6 digit number ID, student name, marks of assignement1, assignment2 and final exam
#The marks are then converted to weighted marks on the basis of 20, 30 and 50% respectively
#Then the bonus is given depending on the criteria
#
#
#Bonus Policy Table
#Total Weighted Mark	                             Bonus mark
#Between 0 and 50	                             Nil
#Greater than 50, but less than or equal to 70	     10% of every mark above 50
#Greater than 70, but less than or equal to 90	     2 marks PLUS 15% of every mark above 70
#Greater than 90, but less than or equal to 100	     5 marks PLUS 20% of every mark above 90#

###################################################################################################################################

#Displaying the welcome banner for the program of Innovation University of Australia
print("-------------------------------------------------------------")
print("The Innovation University of Australia (IUA) Grade System")
print("------------------------------------------------------------- \n")

#global constant(NEXT_MARKS) is set to true for program to run at the beginning. It is placed here so that program can rerun without
#exiting when the user presses "y" as an answer

NEXT_MARKS = True


while (NEXT_MARKS): #starting of while loop

    #getting input from the user for student ID. User is prompted with the example of ID.
    studentID = input("Please enter the student ID. \nThe student ID should be in format of 6 digits. Eg: \"11651300\" :")

    #getting input from the user for the student name. User is prompted the pattern with which the name is to be placed.
    studentName = input("\nPlease enter the student Name. \nName should be in the format of first name followed by last name: ")

    #displaying the message for the user to enter marks obtained out of 100
    print("\nPlease enter all the marks out of 100")
    
    #getting input of assignment 1 from the user.
    assignment1 = int(input("Please enter the marks for Assignment 1 (0 - 100): "))

    #checking for negative value and value greater than 100
    while(assignment1 < 0 or assignment1 >100 ): # if one of this condition meets then the loop starts

        #this for loop start giving user with message for attemps of 3 tries
        print(" You have 3 tries")

        #start of for loop
        for prompt in range(3):
            print("\nPlease enter a valid number from range 0 to 100.\n") #displaying the message the user
            assignment1 = int(input("Please enter the marks for Assignment 1 (0 - 100): ")) #getting input from the user 

            #this condition ends only if the user input the number from range 0 to 100
            if (assignment1 > 0 and assignment1 <= 100):
                break            #using break to directly out of loop if the condition meets in if statement

            #this loop starts if the user again gives invalid input
            
            if (assignment1 < 0 or assignment1 > 100):
                prompt = prompt + 1  #prompt acts as a counter. Each times the user places invalid input the count increases.

                #when the counter hits 3 tries, this loop starts
                if (prompt == 3):

                    #if the user gives input that is less than 0, this loop starts
                    if (assignment1 <0):
                        assignment1 = 0    #by default after 3 tries, assignement marks is set to 0.

                    #if the user gives input that is greater than 100, this loop starts
                    if (assignment1 >100):
                        assignment1 = 100   #by default after 3 tries, assignement marks is set to 100.

                    #prints user with number of attempt and default assigned marks in new line.
                    print("\nYour", prompt, "attempts were invalid.\nBy default the marks assigned to assignment 1 is", assignment1, "\n")
                

    #getting input of assignment 1 from the user.        
    assignment2 = int(input("Please enter the marks for Assignment 2: (0 - 100) "))

    #checking for negative value and value greater than 100
    while(assignment2 < 0 or assignment2 >100 ):
        #this for loop start giving user with message for attemps of 3 tries
        print(" You have 3 tries")
        
        for prompt in range(3):
            print("\nPlease enter a valid number from range 0 to 100.\n")
            assignment2 = int(input("Please enter the marks for Assignment 2 (0 - 100): "))
            if (assignment2 > 0 and assignment2 <= 100):
                break

            if (assignment2 < 0 or assignment2 > 100 ):
                prompt = prompt + 1 
                
                if (prompt == 3):
                    
                    if (assignment2 <0):
                        assignment2 = 0   #by default after 3 tries, assignment marks is set to 0.
                    
                    if (assignment2 >100):
                        assignment2 = 100  #by default after 3 tries, assignment marks is set to 100.
                        
                    print("\nYour", prompt, "attempts were invalid.\nBy default the marks assigned to assignment 2 is", assignment2, "\n")



    finalExam = int(input("Please enter the marks for the Final Exam: "))

    while(finalExam < 0 or finalExam >100 ):
        print(" You have 3 tries")
        for prompt in range(3):
            print("\nPlease enter a valid number from range 0 to 100.\n")
            finalExam = int(input("Please enter the marks for final Exam(0 - 100): "))
            if (finalExam > 0 and finalExam <= 100):
                break

            if (finalExam < 0 or finalExam > 100 ):
                prompt = prompt + 1 
                
                if (prompt == 3):
                    
                    if (finalExam <0):
                        finalExam = 0
                    
                    if (finalExam >100):
                        finalExam = 100
                        
                    print("\nYour", prompt, "attempts were invalid.\nBy default the marks assigned to final exam is", finalExam, "\n")

    print("\nThank You!\n")
