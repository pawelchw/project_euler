#Each new term in he Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#fibonacci terms
f_curr = 0
f_prev = 1
f_old = 0

#needed for sum
l_sum = 0

#fibonacci limit
n = 4000000

#run up to some limit
while f_curr <= n :
   # fib formular
   f_curr = f_prev + f_old
   # add even numbers
   if ( f_curr % 2 == 0 ) :
      l_sum += f_curr
   # move pointers
   f_old = f_prev
   f_prev = f_curr

print "sum is:" + str(l_sum)
      
