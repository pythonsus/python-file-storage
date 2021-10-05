def sum_pairs(lis,num):
    for i in range(0,len(lis)):
        if lis[i] + lis[i+1] == num:
            return lis[i],lis[i+1]
    return[]

print(sum_pairs([4,2,10,5,1], 6))
