global x2
global y2
global x_limit
global y_limit

def print_mat(matrix):
    for i in matrix:
        for j in i:
            print j,
        print '\n'

def move(x,y,last_step):
    # import ipdb; ipdb.set_trace()
    if x>x_limit-1 or y>y_limit-1:
        return False
    if x==x2 and y==y2:
        if maze_matrix[x][y] == 1:
            return True
        if maze_matrix[x][y] == 0:
            return False
    if maze_matrix[x][y] == 0:
        return False
    else:
        try:
            if last_step == 'right':
                res = move(x,y+1,'right')
                if res:
                    res_matrix[x][y+1] = 1
                if not res:
                    res = move(x+1,y,'down')
                    if res:
                        res_matrix[x+1][y] = 1
                    if not res:
                        res = move(x-1,y,'up')
                        if res:
                            res_matrix[x-1][y] = 1
            if last_step == 'left':
                res = move(x+1,y,'down')
                if res:
                    res_matrix[x+1][y] = 1
                if not res:
                    res = move(x,y-1,'left')
                    if res:
                        res_matrix[x][y-1] = 1
                    if not res:
                        res = move(x-1,y,'up')
                        if res:
                            res_matrix[x-1][y] = 1
            if last_step == 'up':
                res = move(x,y+1,'right')
                if res:
                    res_matrix[x][y+1] = 1
                if not res:
                    res = move(x,y-1,'left')
                    if res:
                        res_matrix[x][y-1] = 1
                    if not res:
                        res = move(x-1,y,'up')
                        if res:
                            res_matrix[x-1][y] = 1
            if last_step == 'down':
                res = move(x,y+1,'right')
                if res:
                    res_matrix[x][y+1] = 1
                if not res:
                    res = move(x+1,y,'down')
                    if res:
                        res_matrix[x+1][y] = 1
                    if not res:
                        res = move(x,y-1,'left')
                        if res:
                            res_matrix[x][y-1] = 1
        except Exception as e:
            pass
            # print str(x),stry+'==>'+str(e)
        return res


if __name__ == '__main__':
    global x2,y2
    print "Enter matrix size X Y"
    x_limit = raw_input()
    y_limit = raw_input()
    x_limit = int(x_limit)
    y_limit = int(y_limit)
    print "Enter elements"
    maze_matrix=[]
    for i in range(int(x_limit)):
        j_list=[]
        for j in range(int(y_limit)):
            ele = raw_input()
            ele = int(ele)
            j_list.append(ele)
        maze_matrix.append(j_list)
    res_matrix = [[0 for y in range(int(y_limit))] for x in range(int(x_limit))]
    print "Your matrix"
    print_mat(maze_matrix)
    print "Enter source x y and dest x y co-ordinates"
    x1 = int(raw_input())
    y1 = int(raw_input())
    x2 = int(raw_input())
    y2 = int(raw_input())
    res = move(x1,y1,'right')
    if res:
        res_matrix[x1][y1]=1
        print "Route Found"
        print_mat(res_matrix)
    else:
        # res = move()
        print "No route Found"
