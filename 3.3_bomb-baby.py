def solution(x, y):
    x = int(x)
    y = int(y)
    
    if x == 1 and y == 1:
        return 0 #edge case 
    
    if x%2 == 0 and y%2 == 0: 
        return "impossible" #if both are even -> impossible
    
    #assign bigger and smaller values
    bigger = x if x > y else y 
    smaller = x if x < y else y 

    counter = 0 
    while(bigger > 1):
        counter += bigger/smaller #number of times we can subtract smaller from bigger 
        temp = bigger%smaller #remainder of ^ 

        #reassign bigger and smaller
        bigger = temp if temp > smaller else smaller 
        smaller = temp if temp < smaller else smaller

        if smaller == 0 and bigger != 1: #if we "ran out" of one bomb before the other reaches 1 -> impossible
            return "impossible"
        
    return str(counter-1) #it'll count an extra step at the end so remove that 

print(solution(1, 1)) #0 
print(solution('4', '7')) #4
print(solution('2', '4')) #impossible 
print(solution('53', '36')) #12
print(solution('531', '36')) #impossible 