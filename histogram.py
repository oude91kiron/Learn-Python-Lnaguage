""" This program wrote to generate random list with 20 number from 0 to 10
       and show how many times each number had generated in the list """

import random

random_list = []
list_length = 20

while len(random_list) < list_length: 
	# Add numbers to the list from 0 to 10 randomly
    random_list.append(random.randint(0,10))  

count_list = [0] * 11  # list with 10 zero element 
index = 0 

while index < len(random_list):  
    number = random_list[index]   # Generating number at the position index
    count_list[number] = count_list[number] + 1  # Every time find the number add 1
    index = index + 1  

print "This is a list generated randomly" 
print ""   
print random_list
print ""
print "number | occurrence","   number | occurrence"
index = 0
num_len1 = len("number")  # The length of the string "number"
num_len2 = len("number  occurrence")
while index < len(count_list):  # count list has 11 element
  # Printing spaces to make the list1 more readable
  num_spaces1 = num_len1 - len(str(index)) 
  # Printing spaces to make the list2 more readable
  num_spaces2 = num_len2 - len(str(index))

  print (" " * num_spaces1 + str(index) + " | " + str(count_list[index] )),\
  (" " * num_spaces2  + str(index) + " | " + str(count_list[index] * "*" ))
  index = index + 1