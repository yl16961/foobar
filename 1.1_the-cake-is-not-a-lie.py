def solution(s):
    s_rev = s[::-1] #reverse string 
    seq_prefix = "" #for tracking sequence forwards
    seq_suffix = "" #for tracking sequence backwards
    
    #edge case: sequence is same char 
    if (s.count(s[0]) == len(s)):
        return s.count(s[0])

    #iterate through string forwards and backwards to check if we found the word
    for i in range(0, len(s)):
        seq_prefix += s[i]
        seq_suffix += s_rev[i]
        
        if seq_prefix == seq_suffix[::-1]: #potential word found
            #check if word evenly divides into s (no leftovers)
            if (s.count(seq_prefix)*len(seq_prefix) == len(s)):
                return s.count(seq_prefix) 


print(solution("abccbaabccba")) #2
print(solution("abcabcabcabc")) #4
print(solution("aaa")) #3
print(solution("abdc")) #1