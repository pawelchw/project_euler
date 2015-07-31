l_max = 100

sum_of_sq = sum([i**2 for i in range(1,l_max+1)])

sq_of_sum = sum([i for i in range(1,l_max+1)])**2

print sq_of_sum - sum_of_sq


