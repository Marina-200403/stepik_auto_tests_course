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


def start_menu(message_input: str, message_err: str, template: dict):
    while True:
        ch = valid_value(message_input,
                         message_err,
                         list(template))
        f, is_break = template[ch]
        f()
        if is_break:
            break
    return False


if __name__ == "__main__":
    # тесты

    caption_start = "menu_main \n 1) f1 \n 2) f2 \n 0) exit \n"
    caption_err = 'err'
    menu_template = {
        0: (lambda: True, True),
        1: (lambda: print("f1"), False),
        2: (lambda: print("f2"), False)}  
    start_menu(caption_start, caption_err, menu_template)

    exit(0)