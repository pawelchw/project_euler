import pandas as pd
import numpy as np
import sys
from time import gmtime, strftime

sys.setrecursionlimit(10000)

def recursive_prime(p_in, p_div):

   if ( p_in % p_div <> 0 ) and ( p_div > 1):
      return recursive_prime(p_in, p_div-1)
   elif ( p_div == 1):
      return 1 ; # is prime
   else:
      return 0 ; # is not prime


def iterative_prime(p_in, p_div):

   for xx in xrange(p_div,1,-1):
      if ( p_in % xx  == 0 ):
         return 0 ; # is not prime

   return 1 ; # is prime

def multipliers_prime(p_in,p_max):

  l_div = 2

  while (l_div < p_max):
     if (p_in % l_div == 0):
        p_in = p_in/l_div
        print 'curr max: ', p_in, ' curr div: ', l_div
     l_div +=1 

  return l_div
     

  


def main():
   l_num = 600851475143

   l_max_prime = int(np.floor(np.sqrt(l_num))) ;
   l_min_prime = 2
   l_is_prime = 0
   l_is_prime = multipliers_prime( l_num,l_max_prime)
   print l_is_prime

   #for xx in xrange( l_max_prime , l_min_prime, -1):
      #print 'doing ', xx 
   #   
     
   #   if (xx%100 == 0):
   #      print str(round( (l_max_prime*1.0 - xx)/l_max_prime,4)), strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
   #   elif (l_is_prime == 1) and (l_num % xx ==0):
   #      print l_is_prime, 'prime'
   #      return 0

main()
#a=pd.DataFrame(zip(  range(1,l_max_prime),  [0 for i in range(1,l_max_prime)]   ), columns=['num','done'])

#l_done =0
#l_max = 0

#l_done =  np.bincount(a['done'].tolist())[0]


#while l_done > 0 :

#a.done [ a.1 % 2==1] =3
