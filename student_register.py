# Output practice

# Step 1: Make while loop to make sure the person inputs the right amount of students.
while True:
    student_amount = input('Please enter the total amount of students registering.\nTotal amount of students registering: ')    
    if student_amount.isdigit():             
        student_amount = int(student_amount)
        print(f'The total amount of students registering are: {student_amount}. ') # Printing here to make sure everything looks fine in python, can remove if need be.        
        break        
    else:        
        print(f'You have entered {student_amount} which is an invalid number.')
        
# Step 2: Make for loop asking students or person registering to write the student ID numbers.        
total_student_id_list = []

for i in range(0, student_amount):  # I will not be doing a while loop with the isdigit() method here as in some colleges/unis some student IDs also have letters in them.    
    student_id = input('Please enter your student ID number: ')    
    total_student_id_list.append('Student ID number:  ' + student_id + ':\t Signature: ......................................... \n \n')
    
total_student_id_list = ''.join(total_student_id_list) # Turn from list to string.      
print(f'Student ID numbers below: \n \n{total_student_id_list}') # Printing here to make sure everything looks fine in python itself, can remove if need be.

# Step 3: Create a .txt document using with method to make sure everything as it should be.             
with open ('reg_form.txt', 'w') as file:    
    file.write((f'Student ID numbers below: \n \n{total_student_id_list}'))
