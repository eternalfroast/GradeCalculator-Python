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

