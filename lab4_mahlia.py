# Mahlia Stallworth-Lewis | Lab 4 | Intro to Python

#Ticket 1

# age = [17, 11, 25, 13, 9]

# for item in age:
#     if item >= 13:
# #PREDICT: Ages 17, 25, and 13 will get "Access granted". Ages 11 and 9 will get "Too young".
#         print("Access granted")
#     else:
#         print("Too young")
    
#EXPLAIN: The variable 'age' holds the age the users input.

#Ticket 2

# count = 0

# keep_checking = "yes"

# while keep_checking == "yes":
#     age = int(input("Enter an age: "))
# #PREDICT: I think that if the user types no on the very first check, the loop will not run at all.
#     if age >= 13:
#         print("Access granted")
#     else:
#         print("Access denied")
    
#     keep_checking = input("Check another age? (yes/no): ")

#EXPLAIN: A while loop is the right choice here instead of a for loop because it keeps going until you give it something to stop the loop.

#Ticket 3

# while True:
#     entry = input("Enter an age or type stop: ")
#     if entry == "stop":
#         break
# #PREDICT: I think that if I ran the code without the 
#     print(entry)

#EXPLAIN: The difference between this while loop and Ticket 2's while loop is that this while loop is a while True loop.

#Ticket 4

# ages = [17, 11, 25, 13, 9]

# def can_access(age):
#     if age >= 13: 
#         return True

#     else:
#         return False
# #PREDICT: I think the difference between how this code works is that we're able to reuse the can_access(age) whenever we want instead of rewriting the entire thing all over again.     
# for age in ages:
#     if can_access(age):
#         print("Access granted")
    
#     else:
#         print("Too young")
#EXPLAIN: It's more efficient to put the check inside of a function.

#Ticket 5

def can_access(age):
    return age >= 13

def signup_report(ages):
    approved = 0

    print(" -- StreamPass Signup Report -- ")

    for number, age in enumerate(ages, start=1):
        if can_access(age):
            print(f"Signup #{number} | Age {age} - Access granted")
            approved += 1
        else:
            print(f"Signup #{number} | Age {age} - Too young")
        
    print(f"Approved: {approved} out of {len(ages)}")

#PREDICT: 
#-- StreamPass Signup Report -- 
# Signup #1 | Age 22 - Access granted
# Signup #2 | Age 10 - Too young
# Signup #3 | Age 15 - Access granted
# Signup #4 | Age 8 - Too young
# Signup #5 | Age 19 - Access granted
# Signup #6 | Age 13 - Access granted
# Approved: 4 out of 6

signups = [22, 10, 15, 8, 19, 13]
signup_report(signups)

#EXPLAIN: For the functions I used (def signup_report, and def can_access). For the parameters, I used (ages, and age). 
#Explain ext.: I used lists (signups). I used for loops and while loops, as well as if/else conditional. I used counter variables, and len(). Lastly I used f-strings and function calls for this ticket.