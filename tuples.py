#!/usr/bin/python


tup1 = ('Lincoln', 'JFK', 'Jefferson', 'Hamilton');

tup2 = ('1804','1963', '1865', '1825')


print("tup1[0]: ", tup1[0]) #prints index tup1 0
print("tup2[1:5]: ", tup2[1:5]) #prints the dates of tup2
print(tup1[-2]) #prints the index of -2


tup3 = ('Adams', 'Roosevelt', 'Obama', 'Taft', 'Grant')

if "Adams" in tup3:
    print("Yes, Adams was the second president of the United States")

    print(len(tup3)) #prints the length

tup4 = tup1 + tup3 #Concatenates the tups
print(tup4)

if "Washington" in tup4:
    print("Yes, George Washington was the first President of the United States of America.")
else:
    print("Invalid option")
