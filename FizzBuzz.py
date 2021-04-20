#Fizzbuzz Program

""" If the number is devisable by 3 and 5 program will output Fizzbuzz.
 If devisable by 3 it will output Fizz.
 If devisable by 5 it will output Buzz. """

for fizzbuzz in range(1,101):

    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
       print ("Fizzbuzz")
       continue
    elif fizzbuzz % 3 == 0:
        print ("Fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print ("Buzz")
        continue
    print (fizzbuzz)
