maze = [
    [1,1,0,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,1,1,0,1]
    ]

def find_entry(mazeToSolve):
    first_line = mazeToSolve[0]
    for x in range(len(first_line)):
        if first_line[x] == 0:
            return x
    return -1

def check_field_for_pathway(maze, x, y):
    if x < 0 or y < 0 or y >= len(maze) or x >= len(maze[y]):
        return 1
    return maze[y][x]

def check_next_way(maze, x, y):
    tmp_maze = list(maze)
    tmp_maze[y][x] = 1
    if check_field_for_pathway(tmp_maze, x-1,y) == 0:
        print("Going to X: ", x-1, " Y: ", y)
        check_next_way(tmp_maze, x-1, y)
    if check_field_for_pathway(tmp_maze, x+1, y) == 0:
        print("Going to X: ", x+1, " Y: ", y)
        check_next_way(tmp_maze, x+1, y)
    if check_field_for_pathway(tmp_maze, x, y-1) == 0:
        print("Going to X: ", x, " Y: ", y-1)
        check_next_way(tmp_maze, x, y-1)
    if check_field_for_pathway(tmp_maze, x, y+1) == 0:
        print("Going to X: ", x, " Y: ", y+1)
        check_next_way(tmp_maze,x, y+1)
    return

# liste = [1,2,3]

#def rwl(liste):
#    if len(liste) == 0:
#        return 
#    else:
#        print("before Recursion ")
#        print(liste)
#        tmp_liste = list(liste)
#       tmp_liste.pop()
#       rwl(tmp_liste)
#        print("after Recursion ")
#        print(liste)
#    return

        
        
    
