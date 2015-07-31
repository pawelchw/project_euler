import numpy as np


def main():
  l_max_max = 2000000

  l_max = int(np.ceil(np.sqrt(l_max_max))) #
  l_min = 2
  l_sum = 0

  l_input_num =  range(1,l_max_max+1)
  l_input_flag = [False for i in  range(1,l_max_max +1)]
  
  l_set_1 = [1,13,17,29,37,41,49,53]
  l_set_2 = [7,19,31,43]
  l_set_3 = [11,23,47,59]
  
  for xx in xrange(1,l_max):
     for yy in xrange(1,l_max):
        n = 4*xx**2+yy**2
        if ( n % 60 in l_set_1 ) and ( n < l_max_max ): l_input_flag[n] =  not l_input_flag[n]

        n = 3*xx**2+yy**2
        if ( n % 60 in l_set_2 ) and ( n < l_max_max ): l_input_flag[n] =  not l_input_flag[n]

        n = 3*xx**2-yy**2
        if ( n % 60 in l_set_3 ) and (xx > yy) and ( n < l_max_max ):
           l_input_flag[n] =  not l_input_flag[n]


  for xx in xrange(5,l_max+1):
     if l_input_flag[xx] == 1 :
        l_value = (xx)**2
        for yy in xrange( l_value, l_max_max, l_value ):
            l_input_flag[yy] = False

  l_sum =2+3+5
  for xx in xrange(1,l_max_max):
    if l_input_flag[xx]:
       l_sum +=xx
  print l_sum
  


main()
