from time import gmtime, strftime

def find_prime_numbers( p_in ):

   l_ret = []   

   for xx in xrange(p_in,1,-1):
     l_div_test = False
     for yy in xrange(p_in,1,-1):
       if ( (xx % yy == 0) and  (xx != yy) ):
           l_div_test = True
           break
     if not l_div_test:
        l_ret.append(xx)

   return l_ret

def least_common_multiplier( p_max, p_mask ):

   l_test = [i for i in xrange(1,p_max+1)]
   l_ret = []

   for xx in p_mask:
      l_divisor = 1
      l_div_test = 1
      while ( l_div_test == 1):
         l_res = map( lambda x: x % xx**l_divisor, l_test)
         if len( [i for i in l_res if i ==0]) > 0:
            l_divisor+=1
         else:
            l_div_test =0
      l_ret.append(l_divisor-1)
 
   return l_ret
def main():

   l_max = 20
   l_base = find_prime_numbers(l_max)
   print l_base
   l_power = least_common_multiplier(l_max, l_base)
   print l_power
  
   #print l_prod
   l_pow=map( lambda x,y: x**y, l_base,l_power)

   print reduce( lambda x,y: x*y, l_pow)
   



main()
