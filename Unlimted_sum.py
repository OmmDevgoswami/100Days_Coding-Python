def add(*args):
    sum = 0
    for _ in args:
        sum += _
    return sum
        
print (add(3,5,4,6,7,4,8,2))