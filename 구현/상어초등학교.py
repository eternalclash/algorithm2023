import copy
N = int(input())
arr = [[0] * N for _ in range(N)]
students = [list(map(int,input().split())) for _ in range(N*N)]
directions = [(-1,0),(0,-1),(1,0),(0,1)]
for student in students:
    seat_student = student[0]
    order = []
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0 :
                like = 0
                blank = 0
                for direction in directions:
                    dx = x+direction[0]
                    dy = y+direction[1]
                    if 0<=dx<N and 0<=dy<N:
                        if arr[dx][dy] in student[1:]:
                            like+=1
                        if arr[dx][dy] == 0 :
                            blank+=1
                order.append([like,blank,x,y])
    order.sort(key=lambda x: (-x[0],-x[1],x[2],x[3]))
    arr[order[0][2]][order[0][3]] = seat_student
answer =0
for x in range(N):
    for y in range(N):    
        count =0
        student_list = []
        for student in students:
            if arr[x][y] == student[0]:
                student_list = copy.deepcopy(student)
                break
        for direction in directions:
            dx = x + direction[0]
            dy = y + direction[1]
            if 0<=dx<N and 0<=dy<N:
                if arr[dx][dy] in student_list[1:]:
                    count+=1
        if count == 0 : continue
        answer+=10**(count-1)
print(answer)

    

