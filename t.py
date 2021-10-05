l =[[1,2,3],["a","d","h"]]
def list_check(text):
    
    [for i in text all(type(i)  == list)]

print(list_check(l))
