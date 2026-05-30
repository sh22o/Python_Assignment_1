
# #TASK 1 : 
print()  # empty line
# Ask user for name
name = input("Enter your name: ") 
try:
    age = int(input("Enter your age: "))
    print(f"Hello {name}, you are {age} years old!")
except ValueError:
    print("Invalid input. Please enter a valid number for age.")

#===========================================================================
#task2 :A level 
print()  # empty line 
print("\nThis program will analyze a two numbers and display the rusults of addition ,subtraction ,multiplication and division")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: ")) 

#print results 
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}") 

#================================================================================= 
#task3 >> B level 
#Ask user for input 3 scores 
print("\nThis program will analyze a scores for 3 subject and display average with your grade")

score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: ")) 

# calculate avg  
average = (score1 + score2 + score3) / 3 

#check grade by value 
if average >= 90:
    grade = "A"
elif average >= 75 and average < 90:
    grade = "B"
elif average >= 60 and average < 75:
    grade = "C"
else:
    grade = "F" 

#Print formatted output
#print avg round 2
print(f"Average score: {average:.2f}")
print(f"Grade: {grade}")  

#===================================================================== 

#Task 4 >> C level 
print("\nThis program will analyze a list of numbers and calculate the sum, largest number, smallest number, and average.")
print("Please enter numbers separated by commas (example: 10,20,30,40,50)\n")

#Ask user to enter numbers with comma 
numbers_input = input("Enter numbers separated by commas: ")
#make variable to save numbers ==> (numbers will be string values )=>>
numbers_str = numbers_input.split(",")
#empty list to add numbers after convert from string to int 
numbers = [] 
#convert string values to int values 
for item in numbers_str:
    numbers.append(int(item))
#start total from zero, define (largest , smallest)
total = 0
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
     # Add current number to total
    total += num
    #check if current number is largest number ? 
    if num > largest:
        largest = num
    #check if current number is smallest number ? 
    if num < smallest:
        smallest = num
#calculate avg , use (len ) python function for get numbers of items 
average = total / len(numbers)
#print Result 
print(f"Sum: {total}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
print(f"Average: {average:.2f}")



