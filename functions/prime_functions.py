def is_prime( p_in):
   l_prime=True
   for xx in range(2,p_in):
      if ( p_in % xx ==0 ):
        l_prime=False
        break

   return l_prime


def prime_list( p_in ):

  l_res = []
  for xx in xrange(2,p_in+1):
    if is_prime(xx):
       l_res.append(xx)

  return l_res
