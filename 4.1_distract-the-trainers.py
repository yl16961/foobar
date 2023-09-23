from itertools import combinations
import operator

def solution(banana_list):
    banana_indices = [x for x in range(len(banana_list))] #make array for indices of banana list
    pairings = list(combinations(banana_indices, 2)) #get all combinations of trainers
    
    tracker = {} #dict for tracking wins and losses
    for i in banana_indices:
        temp = {}
        counter = 0
        tracker[i] = [counter, temp]
    
    for pair in pairings: #for each pairing, check if they will play infinitely
        a, b = pair 
        if infinite_play(banana_list[a], banana_list[b]): 
            #if inf play -> update tracker to reflex a match and which one it matched with 
            counter, temp_tracker = tracker[a]  
            temp_tracker[b] = temp_tracker[b]+1 if b in temp_tracker else 1
            tracker[a] = [counter+1, temp_tracker]
            counter, temp_tracker = tracker[b] 
            temp_tracker[a] = temp_tracker[a]+1 if a in temp_tracker else 1
            tracker[b] = [counter+1, temp_tracker]

    #sort tracker from least number of matches to most 
    sorted_tracker = (sorted(tracker.items(), key=operator.itemgetter(1)))
    unmatched_trainers = 0

    while(len(sorted_tracker) != 0): #keep going through the sorted list to match trainers
        i, [count, tracker] = sorted_tracker[0]
        if count == 0: #if a trainer has no match, we increment unmatched_trainers
            unmatched_trainers += 1
            sorted_tracker = sorted_tracker[1:] #remove this trainer from the list
        
        else: #if there is a possible match, look in order of least to greatest counts
            flag = False
            for j in range(len(sorted_tracker)):
                match_i, [match_count, match_tracker] = sorted_tracker[j]

                if i in match_tracker and match_tracker[i] > 0: 
                    sorted_tracker = sorted_tracker[1:j] + sorted_tracker[j+1:] #remove both trainers from list
                    flag = True
                    break
            if not flag: 
                unmatched_trainers += 1 #no match found 
                sorted_tracker = sorted_tracker[1:] #remove trainer from list 
            
    return unmatched_trainers #return final count

def gcd(a,b): #function to calculate gcd 
    while b:
        a, b = b, a % b
    return a

#infinite play will happen if reduced sum of total bananas is not a power of 2 
def infinite_play(a, b): 
    temp = int((a+b) / gcd(a,b))
    return bool(temp & (temp - 1))

    if a == b:
        return False
    if a%2 is not b%2:
        return True
    
    tracker = {}
    bigger = a if a > b else b
    smaller = a if a < b else b
    key = str(smaller)+"+"+str(bigger)
    tracker[key] = 0
    
    while(True):
        if (bigger == smaller):
            return False 

        temp1 = bigger - smaller
        temp2 = smaller + smaller

        bigger = temp1 if temp1 > temp2 else temp2
        smaller = temp1 if temp1 < temp2 else temp2 

        key = str(smaller)+"+"+str(bigger)

        if key in tracker:
            return True
        
        tracker[key] = 0
        
print(solution([1, 7, 3, 21, 13, 19]))
print(solution([1, 1]))

