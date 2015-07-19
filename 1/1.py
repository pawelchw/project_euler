#Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.


#for integer up to 1000
n =1000
l_sum =0

# loop through the number
for xx in range (1, n):

# if divisible by 3 or 5 increment
   if ( xx % 3==0 ) or ( xx % 5 == 0 ):
       print xx
       l_sum += xx

print "Sum is: "+ str(l_sum)
