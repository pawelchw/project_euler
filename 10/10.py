import sys
import pandas as pd
import numpy as np
from time import gmtime, strftime
#sys.path.append('../functions/')
#from prime_functions import is_prime, prime_list


def main():
  l_max = 20000 #
  l_min = 2
  l_sum = 0

  l_input = pd.DataFrame(zip(  range(1,l_max+1),  [0 for i in range(1,l_max +1)]   ), columns=['num','is_prime'])
  
  l_set_1 = [1,13,17,29,37,41,49,53]
  l_set_2 = [7,19,31,43]
  l_set_3 = [11,23,47,59]
  
  for xx in xrange(1,l_max):
     if xx % 1000==0:
        print strftime("%Y-%m-%d %H:%M:%S", gmtime())
     for yy in xrange(1,l_max):
        n = 4*xx**2+yy**2
        if ( n % 60 in l_set_1 ) and ( n <= l_max ):
           l_input.is_prime[l_input.num == n] = abs( l_input.is_prime[l_input.num == n] - 1)

        n = 3*xx**2+yy**2
        if ( n % 60 in l_set_2 ) and ( n <= l_max ):
           l_input.is_prime[l_input.num == n] = abs( l_input.is_prime[l_input.num == n] - 1)

        n = 3*xx**2-yy**2
        if ( n % 60 in l_set_3 ) and (xx > yy) and ( n <= l_max ):
           l_input.is_prime[l_input.num == n] = abs( l_input.is_prime[l_input.num == n] - 1)

  for xx in xrange(5,int(np.ceil(np.sqrt(l_max)))):
     if 1 in l_input.is_prime[l_input.num == xx].tolist() :
        for yy in xrange(xx*xx, l_max, xx*xx):
           if 1 in l_input.is_prime[l_input.num == yy].tolist() :
              l_input.is_prime[l_input.num == yy] = abs( l_input.is_prime[l_input.num == yy] - 1)


  print sum([2,3,5]+l_input[l_input.is_prime==1].num.tolist())
 # print prime_list(l_max)

  
         
         
  #initialise primes up to 59
  #l_set = prime_list(60)
  # add 1 into set and remove 2,3,5
  #l_set = [1] + [ i for i in l_set if i> 5]
  #print l_set

  #sieve
  #l_sieve=[]
  # max to start filling
  #l_sieve_max = 0
  # needed to ofset 60 multipliers
  #w=0

  #while l_sieve_max <= l_max:
  #   l_sieve = l_sieve+  [ 60*w + i for i in l_set]
  #   w = w+1
  #   l_sieve_max = max(l_sieve)

  
  #print l_sieve

  # corresponding prime flags
  #l_is_prime = [0 for i in l_sieve]

  #print [1] + prime_list(240)

  #while
  # for xx in xrange(l_min,l_max+1):
  #    if is_prime(xx):
  #       l_sum+=xx
  #    if ( xx % 10000 == 0):
  #       print xx
  #print l_sum


main()
