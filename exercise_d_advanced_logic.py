# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print(even_numbers) 


# 2. Print the difference between the largest and smallest value:
min_value = min(numbers)
max_value = max(numbers)

print(max_value - min_value) 

# 3. Print True if the list contains a 2 next to a 2 somewhere.

previous_number = None
for number in numbers: 
    if number ==2 and previous_number == 2:
        print(True)
    previous_number = number  

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

start_index = numbers.index(6)
stop_index = numbers.index(7)

i = 0 
total = 0
for number in numbers: 
    
    if i >= start_index and i <= stop_index:
        pass
    else:
        total= total + number 
    i= i + 1


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 







