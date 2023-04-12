import numpy as np

mark_empty = "_"
mark_comp = "O"
mark_man = "X"

def show_state(s):
    for i in range(3):
        print(s[i][0], s[i][1], s[i][2])

def show_board():
    b = range(1, 10)
    print("-------------")
    for i in range(3):
        print("|", b[0 + i * 3], "|", b[1 + i * 3], "|", b[2 + i * 3], "|")
        print("-------------")


def get_move(s):
    need_move = 1
    while(need_move == 1):
        a = int(input("Введите ход"))

        row = (a - 1) // 3
        col = (a - 1) % 3

        if ((a > 0) and (a < 10) and (s[row][col]==mark_empty)):
            s[row][col] = mark_man
            need_move = 0
        else:
            print("Неверный ход!")
# Сама игра
def make_move(s):
    depth = 3
    crit = 2
    size_s=len(s)
    filled=0
    w=np.array([[0]*size_s]*size_s)
    law_row=[0,1,1, 1, 0,-1,-1,-1]
    law_col=[1,1,0,-1,-1,-1, 0, 1]

    for i in range(3):
        for j in range(3):
            comp = [0, 0, 0, 0]
            if (s[i][j] == mark_empty):
                for l in range(8):
                    r=i
                    c=j
                    for d in range(1,depth):
                        r+=law_row[l]
                        c+=law_col[l]
                        if ((r >= 0) and (c >= 0) and (r <size_s) and (c < size_s)):
                            if (s[r][c] == mark_comp):
                                comp[l%4]+=1
                                if (comp[l%4] >= crit):
                                    s[i][j]=mark_comp
                                    print("Я выиграл!")
                                    return 1
                for l in range(4):
                    w[i][j]+=comp[l]
            else: filled+=1
    if (filled >= size_s*size_s):
        print("Ничья!")
        return 1
    print(w)
    for i in range(3):
        for j in range(3):
            man = [0, 0, 0, 0]
            if (s[i][j] == mark_empty):
                for l in range(8):
                    r=i
                    c=j
                    for d in range(1,depth):
                        r+=law_row[l]
                        c+=law_col[l]
                        if ((r >= 0) and (c >= 0) and (r <size_s) and (c < size_s)):
                            if (s[r][c] == mark_man):
                                man[l%4]+=1
                                if (man[l%4] >= crit):
                                    s[i][j]=mark_comp
                                    return 0
                for l in range(4):
                    w[i][j]+=man[l]
    print(w)
    max_w = 0
    max_r = 1
    max_c = 1

    for i in range(3):
        for j in range(3):
            if (w[i][j]>max_w):
                max_w=w[i][j]
                max_r=i
                max_c=j
    s[max_r][max_c] = mark_comp
    return 0


def my_move(s):
    depth = 3
    crit = 2
    size_s = len(s)
    filled = 0
    w = np.array([[0] * size_s] * size_s)
    law_row = [ 0,  1,  1,  1,  0, -1, -1, -1]
    law_col = [ 1,  1,  0, -1, -1, -1,  0,  1]
    law_max = [20, 21, 20, 21, 20, 21, 20, 21]
    for i in range(3):
        for j in range(3):
            if (s[i][j] != mark_empty):
                for l in range(8):
                    r = i
                    c = j
                    m = law_max[l]
                    if (s[i][j] == mark_comp):
                        m += 5
                    for d in range(1, depth):
                        r += law_row[l]
                        c += law_col[l]
                        if ((r >= 0) and (c >= 0) and (r < size_s) and (c < size_s)):
                            if (s[r][c] == mark_empty):
                                w[r][c] += m
                                m += -5
                            elif s[r][c] == s[i][j]:
                                m = m * 2
                            else:
                                break
                        else:
                            break
                filled += 1
    if (filled >= size_s * size_s):
        print("Ничья!")
        return 1
    print(w)
    max_w = 0
    max_r = 0
    max_c = 0

    for i in range(3):
        for j in range(3):
            if (w[i][j] > max_w):
                max_w = w[i][j]
                max_r = i
                max_c = j
    s[max_r][max_c] = mark_comp
    return 0


def check_end(s):
    depth = 3
    crit =3
    size_s=len(s)
    law_row=[0,1,1, 1, 0,-1,-1,-1]
    law_col=[1,1,0,-1,-1,-1, 0, 1]
    for i in range(3):
        for j in range(3):
            if (s[i][j] == mark_man):
                for l in range(8):
                    m = 1
                    r=i
                    c=j
                    for d in range(1,depth):
                        r+=law_row[l]
                        c+=law_col[l]
                        if ((r >= 0) and (c >= 0) and (r <size_s) and (c < size_s)):
                            if (s[r][c] == mark_man):
                                m +=1
                                if (m >= crit):
                                    print("Поздравляю, Вы выиграли.")
                                    return 1
    return 0

def game(s):
    while(check_end(s) == 0):
        show_state(s)
        get_move(s)
        if (check_end(s) != 0):
            break
        if (my_move(s) != 0):
            break
    show_state(s)



state=[mark_empty,mark_empty,mark_empty],[mark_empty,mark_empty,mark_empty],[mark_empty,mark_empty,mark_empty]
show_board()
game(state)