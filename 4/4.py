import time as ti

def reverse_number(p_in):
# returns reversed number
# for 1234 it converts that into
# string first, reverses it and returns 
# that number 4321; 200 conversts to 2
   return int(  str( p_in )[::-1]  )

def main():
  tt = ti.time()
  l_min = 100
  l_max = 999
  l_max_pal = 0
  for xx in xrange(l_min,l_max,1):
    for yy in xrange(l_min,l_max,1):
       l_rev = reverse_number(xx*yy)
       if ( xx*yy == l_rev ):
          if l_rev > l_max_pal:
             l_max_pal = l_rev
             print l_max_pal
          

main()


