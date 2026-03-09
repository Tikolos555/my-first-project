def plusone(numbers):
    for i in range(len(numbers)-1 , -1, -1):
        if numbers[i]<9:
            numbers[i]+=1
            return numbers
        else:
            numbers[i]=0
    return [1] + [0]*len(numbers)
print(plusone([9, 9, 9, 9]))