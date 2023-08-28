def solution(src, dest):
    x_src, y_src = src/8, src%8 #translate src # to x,y coord
    x_dest, y_dest = dest/8, dest%8 #translate dest # to x,y coord

    visited = {(x_src, y_src): 1} #use dict to track visited cells 
    return moveBunny(x_dest, y_dest, visited) 
    
def moveBunny(x_dest, y_dest, visited):
    if visited.has_key((x_dest, y_dest)): #check if dest has been found
        return 0 
    
    new_visted = {}
    for pos in visited: #for each position, add all valid moves to a new dict 
        x, y = pos
        moves = [(x-1, y-2),(x-1, y+2),(x+1, y-2),(x+1, y+2),(x-2, y-1),(x+2, y-1),(x-2, y+1),(x+2, y+1)] 
        for move in moves:
            x_new, y_new = move
            if (inBounds(x_new, y_new)):
                new_visted[(x_new, y_new)] = 1
    
    return 1 + moveBunny(x_dest, y_dest, new_visted) #recursively call until dest cell found --> return level of recursion
    
def inBounds(x, y): #check if x, y coord are in 8x8 array
    if (x >= 0 and x < 8 and y >=0 and y < 8):
        return True
    return False

print(solution(1, 1))
print(solution(0, 1))
print(solution(19, 36))

# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------

# [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
# [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
# [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)]
# [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3)]
# [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4)]
# [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5)]
# [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
# [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]