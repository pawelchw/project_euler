def is_prime( p_in, p_primes ):
   l_prime=True
   for xx in p_primes:
      if ( p_in % xx ==0 ):
        l_prime=False
        break
   if l_prime:
     p_primes.append(p_in)
   return p_primes

def main():

  l_primes=[]
  l_counter=2;
  l_limit = 10001
  while len(l_primes)<l_limit:
    l_primes = is_prime(l_counter,l_primes)
    l_counter +=1

  print l_primes

main()
  
  
