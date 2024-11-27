from menu import start_menu as prot_menu

def make_mat():
    pass

def sum_mat():
    pass

def mat_output():
    pass

def menu_main():
    caption_start = "МЕНЮ\n1. Создать матрицы\n2. Выполнить алгоритм\n3. Вывести результат \n0. Выход\n"
    caption_err = "ERROR"
    menu_template = {
        0: (lambda: True, True),
        1: (make_mat, False),
        2: (sum_mat, False),
        3: (mat_output, False)}
    prot_menu(caption_start, caption_err, menu_template)
    
if __name__ == "__main__":
    menu_main()