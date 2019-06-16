
stack = []
arr = [[0,0,0,0,0,0],[0,1,1,0,0,0],[0,0,1,1,0,0],[0,0,0,1,0,0],[0,0,1,0,0,0],[0,0,0,0,0,0]]
c,r = 5,5
number,high = 0,0


for i in range(1,r):
    for j in range(1,c):
        if(number >= high):
            high = number
        # out.append(number)
        if(arr[i][j] == 1):
            number = 0
            stack.append((i,j))
            # print(arr)
            while stack:
                first = stack.pop(-1)
                f_i,f_j = first[0], first[1]
                if(arr[f_i][f_j] != -1):
                    arr[f_i][f_j] = -1 
                    number += 1
                    neighbour = [(f_i,f_j-1),(f_i,f_j+1),(f_i-1,f_j),(f_i+1,f_j),(f_i-1,f_j-1),(f_i-1,f_j+1),(f_i+1,f_j-1),(f_i+1,f_j+1)]
                    for n in neighbour:
                        n_i,n_j = n[0],n[1]
                        if(arr[n_i][n_j] == 1):
                            stack.append(n)
                    # print("stack",stack)

print("largest",high)


        
             # left = arr[i][j-1]
                    # right = arr[i][j+1]
                    # top = arr[i-1][j]
                    # bottom = arr[i+1][j]
                    # d0 = arr[i-1][j-1]
                    # d1 = arr[i-1][j+1]
                    # d2 = arr[i+1][j-1]
                    # d3 = arr[i+1][j+1]
                    # neighbour = [left, right, top ,bottom, d0, d1, d2, d3]
