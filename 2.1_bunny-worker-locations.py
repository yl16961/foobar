# find x value for corner of triangle: x + (y-1) 
# 45-45-90 triangle --> y value = x value; -1 bc we start at y=1
# | 7
# | 4 8
# | 2 5 9
# | 1 3 6 10
# find the value for that location using the equation below
# equation for sum of 1+2+...+n: n(n+1)/2
# "backtrack" by y-1 to find the target value 

def solution(x, y):
    return str((x+y-1)*(x+y)/2 - (y-1))

print(solution(5, 10)) #96
print(solution(3, 2)) #9
print(solution(1, 1)) #1
print(solution(2, 2)) #5