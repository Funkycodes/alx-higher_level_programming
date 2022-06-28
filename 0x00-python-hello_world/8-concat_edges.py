#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = (str[39:66] + str[106:112] + str[0:6]) #' '.join([str.split()[5], str.split()[6],str.split()[-4], str.split()[0]])
print(str)
