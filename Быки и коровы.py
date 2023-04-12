import random as rd
import numpy as np

i_bull = 4
i_caw = 5
max_a = 10000
max_x = 3024
temp = np.array([0] * max_x)
tc = 0
h = np.array([0]*4)
# Массив по разрядам
def i_to_a(x):
    a = np.array([0]*4)
    a[0] = (x//1000)%10
    a[1] = (x//100)%10
    a[2] = (x//10)%10
    a[3] = (x)%10
    return a
# Проверяет число человека на правильность. Возвращает его ввиде массива
def get_move():
    a = ""
    while (a == ""):
        b = np.array([0]*4)
        a = input("Угадайте такое число у машины->")
        if (not a.isdigit() or len(a) !=4):#< 4):
            print("Неправильный ввод: нужно 4 цифры!")
            a = ""
            continue
        for i in range(4):
            b[i] = int(a[i])
        for i in range(3):
            if (b[i] == b[(i + 1) % 4] or b[i] == b[(i + 2) % 4] or b[i] == b[(i + 3) % 4]):
                print("Неправильный ввод: нужны разные цифры!")
                a = ""
                break
    return b
# Считает коров и быков, Выводит на экран
# поменять for
def make_ans(c_cod, m_mov):
    b = 0
    k = 0
    for i in range(4):
        if (c_cod[i] == m_mov[i]):
            b += 1
        for j in range(4):
            if (c_cod[j] == m_mov[i]):
                k += 1
    print("В Вашем числе", m_mov, "<<быков>>:", b, "<<коров>>:", k)
    return b*10+k

# Подбирает первое случайное число
def make_suggest():
    used = np.array([0]*10)
    h = np.array([0]*4)
    for i in range(4):
        while (True):
            h[i] = rd.randint(1, 9)
            if (used[h[i]] != 0):
                continue
            used[h[i]] = 1
            break
    move = h[0]*1000 + h[1]*100 + h[2]*10 + h[3]
    return move

def make_comb():
    used = np.array([0]*10)
    global h
    for i in range(4):
        while (True):
            h[i] = rd.randint(1, 9)
            if (used[h[i]] != 0):
                continue
            used[h[i]] = 1
            break
    move = h[0]*1000 + h[1]*100 + h[2]*10 + h[3]
    return h

# Выбирает случайное число из массива возможных
def make_next_suggest():
    global tc
    rm = rd.randint(0,tc-1)
    move = temp[rm]
    return move

# Ход машины
def my_move(c,a,x,z):
    if c == 0:
        move = make_suggest()
    else:
        move = make_next_suggest()
    print("Попытка:", c, "-> Машина думает, что у вас:", move)
    while (True):
        s = input("Введите двумя цифрами чиcло <<быков>> и <<коров>>")
        q = int(s)
        if (not s.isdigit()):
            print("Неправильный ввод: Должны быть 2 цифры!")
            continue
        #else:
            #q = int(s)
        if (q%10) + (q//10) > 4:
            print("Неправильный ввод: Пересчитывайте!")
            continue
        if ((q//10) == 4):
            return 1
        break
    global tc, temp
    lc = 0
    xc = 0
    list = np.array([0]*max_x)
    xlist = np.array([0]*max_x)
    for i in range(max_x):
        if z[a[move]][i] == q:
            list[lc] = x[i]
            lc +=1
    if c == 0:
        tc = lc
        temp = list
    else:
        for i in range(lc):
            for j in range(tc):
                if list[i] == temp[j]:
                    xlist[xc] = list[i]
                    xc += 1
                    break
        tc = xc
        temp = xlist

    if tc == 0:
        print("Вы где-то соврали!")
        return 1
    return 0
# Вся игра
def game():
    global h
    y = np.fromfile('z_array', dtype=int)
    a = np.fromfile('a_array', dtype=int)
    x = np.fromfile('x_array', dtype=int)
    z = y.reshape(max_x, max_x)
    c = 0
    make_comb()
    print("Загадайте четырёхзначное число из неповторяющихся чисел от 1 до 9")
    while (True):
        if (make_ans(h,get_move()) < 40):
            if (my_move(c,a,x,z) == 0):
                c += 1
                continue
            else:
                print("Машина победила!")
                print("Число машины было:", h)
                break
        else:
            print("Человек победил!")
            print("Число машины было:", h)
            break
    return
game()
