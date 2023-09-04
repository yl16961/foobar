#fill out a dict: key = index, value = count # of values that l[index] divides in the rest of the list
#iterate through using only 2 nested loops: if x divides y, look up # of values that y divides and add to counter 
def solution(l):
    num_divisible = {len(l)-1: 0} #for completeness, add last value to dict w/ count of 0 
    for i in range(len(l)):
        num_divisible[i] = 0 
        for j in range(i+1, len(l)):
            if l[j]%l[i] == 0:
                num_divisible[i] += 1 
    
    counter = 0 
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j]%l[i] == 0:
                counter += num_divisible[j] 
    return counter

print(solution([1, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6])) 

def trivial_solution(l):
    counter = 0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if (l[j]%l[i] == 0):
                for k in range(j+1, len(l)):
                    if (l[k]%l[j] == 0):
                        counter += 1
    return counter