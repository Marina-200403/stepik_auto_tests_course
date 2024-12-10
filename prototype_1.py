from random import randint
import numpy as np


def is_int(s):
    try:
        if type(s) is int:
            return True
        if s is None:
            return False
        if not s.isdecimal():
            return False
        int(s)
        return True
    except (Exception, ValueError, TypeError):
        return False


def valid_value(message_input: str, message_err: str, template: list):
    while True:
        ch = input(message_input, )
        if is_int(ch):
            ch = int(ch)
            if ch in template:
                return ch
        print(message_err)

def valid_comand(ch, flag):
    return True

def make_mat():
    size = int(input("Введите размер матрицы "))
    mat_1 = mat_input(size)
    mat_2 = mat_input(size)
    return (mat_1, mat_2, size)

def sum_mat(mat_1, mat_2, size):
    mat_rezult = [ [0]*size for i in range(size)]
    mat_rezult = np.add(np.array(mat_1), np.array(mat_2))
    det = np.linalg.det(np.array(mat_rezult))
    return (mat_rezult, det)

def mat_input(size):
    mat = [ [0]*size for i in range(size)] 
    return mat

def mat_output(mat_1, mat_2, mat_rezult, det):
    print (mat_1, '\n', mat_2)
    print(mat_rezult, '\n', det)

def menu_main():
    caption_start = "МЕНЮ\n1. Создать матрицы\n2. Выполнить алгоритм\n3. Вывести результат \n0. Выход\n"
    caption_err = "ERROR"
    menu_template = {
        0: (lambda: True, True),
        1: (make_mat, False),
        2: (sum_mat, False),
        3: (mat_output, False)}
    flag = 1
    while True:
        ch = valid_value(caption_start,
                         caption_err,
                         list(menu_template))
        f, is_break = menu_template[ch]
        if ch == 1:
            mat_1, mat_2, size = f()
            flag = 2
        if ch == 2 and valid_comand(ch, flag):
            mat_rezult, det = f(mat_1, mat_2, size)
            flag = 3 
        if ch == 3 and valid_comand(ch, flag):
            f(mat_1, mat_2, mat_rezult, det)
        if is_break:
            break
    return False
    
if __name__ == "__main__":
    menu_main()