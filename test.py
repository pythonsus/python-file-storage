def sum_pairs(lis,num):
    for i in range (0, len(lis)):
        if lis[i] + lis[i+1] == 0:
            print(i)
##            return lis[i:i+2]
##        
        return[]
            
print(sum_pairs([3,2,3,4,5,6,7,8,9],9))
print(sum_pairs([3,2,3,4,5,6,7,8,9],5))

