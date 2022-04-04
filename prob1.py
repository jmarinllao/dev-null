def get_sum_multiples_5_3(): 
    array = []
    sum = 0
    for n in range(0, 1000):
        if n % 3 == 0 or n % 5 == 0: 
            sum += n
            array.append(n)
    return sum, array

print(get_sum_multiples_5_3())
