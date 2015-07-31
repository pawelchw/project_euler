
l_min = 1
l_max = 1000
xx = 1
yy = 1
zz = 1
l_break = False

for xx in xrange(1,l_max):
  xx_s = xx**2
  if l_break:
    break
  for yy in xrange(1,l_max):
    if l_break:
      break
    yy_s = yy**2
    for zz in xrange(1,l_max):
      if ( xx_s + yy_s == zz**2 ) and (xx + yy + zz ==1000):
         print str(xx) + ' ' + str(yy) + ' ' + str(zz)
         print xx*yy*zz
         l_break = True
         break
      if l_break:
         break
