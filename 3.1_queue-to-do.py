#XOR of two consecutive even + odd ints = 1
#XOR of two 1s = 0
#for each pass through the line, group bunnies into even+odd pairs 
#check if there's an odd number of pairs
#check if initial ID is odd -> XOR that
#check if final ID wasn't grouped into a pair -> XOR that as well 
def solution(start, length):
    counter = start
    skip = length
    answer = 0
    for i in range(length):
        if counter%2 == 1:
            answer = answer ^ counter
            remainder = ((skip-1)/2)%2 #is there an odd number of pairs 
            len = skip-1 #is last ID included in a pair (no if odd, yes if even)
        else:
            remainder = ((skip)/2)%2
            len = skip

        if (len%2 == 1):
            last = counter+skip-1
            if (last != counter or (counter%2 == 0)):
                answer = answer ^ last
                
        answer = answer ^ remainder
        counter = counter + length
        skip -= 1
    
    return answer

#test cases
print(solution(3, 1)) #3 
print(solution(0, 3)) #2
print(solution(17, 4)) #14

#generates the grid of bunny workers according to example 
# 0 1 2 /
# 3 4 / 5
# 6 / 7 8
def generate_arr(start, length):
    arr = []
    counter = start
    skip = length
    for i in range(length):
        col = []
        for j in range(length+1):
            if skip == j:
                col.append(-1)
                skip -= 1
            else:
                col.append(counter)
                counter += 1
        arr.append(col)
        print(col)

#using same idea as generate_arr, XOR all values that would have been in the array before / 
def brute_force_attempt(start, length):
    checked_bunnies = []
    counter = start
    skip = length
    answer = 0
    for i in range(length):
        for j in range(length+1):
            if j < skip:
                answer = answer ^ counter
                checked_bunnies.append(counter)   
            if j != skip:
                counter += 1
        skip -= 1

    print(checked_bunnies)
    print(answer)
