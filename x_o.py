from colorama import just_fix_windows_console
just_fix_windows_console()
answer = ''


def printtable(s):
    print('\033[H')
    for i in range(8):
        print('\033[K\033[B')
    print('\033[H', end='')
    print('Введите номер строки и столбца через пробел.')
    print('╔═══╦═══╦═══╦═══╗')
    print('║x|o║ 1 ║ 2 ║ 3 ║')
    print('╠═══╬═══╬═══╬═══╣')
    print(f'║ 1 ║ {s[0][0]} ║ {s[0][1]} ║ {s[0][2]} ║')
    print('╠═══╬═══╬═══╬═══╣')
    print(f'║ 2 ║ {s[1][0]} ║ {s[1][1]} ║ {s[1][2]} ║')
    print('╠═══╬═══╬═══╬═══╣')
    print(f'║ 3 ║ {s[2][0]} ║ {s[2][1]} ║ {s[2][2]} ║')
    print('╚═══╩═══╩═══╩═══╝\n')


def check_win(s):
    if s[0][0] == s[0][1] == s[0][2] != ' ':
        return True
    elif s[1][0] == s[1][1] == s[1][2] != ' ':
        return True
    elif s[2][0] == s[2][1] == s[2][2] != ' ':
        return True
    elif s[0][0] == s[1][0] == s[2][0] != ' ':
        return True
    elif s[0][1] == s[1][1] == s[2][1] != ' ':
        return True
    elif s[0][2] == s[1][2] == s[2][2] != ' ':
        return True
    elif s[0][0] == s[1][1] == s[2][2] != ' ':
        return True
    elif s[0][2] == s[1][1] == s[2][0] != ' ':
        return True
    else:
        return False


while answer != 'n':
    i = 0
    table = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    x_or_o = True
    printtable(table)
    while not check_win(table) and i < 9:
        turn = input('Ход крестиков: ' if x_or_o else 'Ход ноликов: ').split()
        turn.append('')
        if turn[0] and turn[1]:
            if table[int(turn[0])-1][int(turn[1])-1] == ' ':
                table[int(turn[0])-1][int(turn[1])-1] = 'x' if x_or_o else 'o'
                print('\033[2K\033[A', end='')
                x_or_o = not x_or_o
                i += 1
            else:
                print('Клетка занята! Повторите ввод.', end='')
                print('\033[A\033[2K\r')
        else:
            print('Некорректная позиция! Повторите ввод.', end='')
            print('\033[A\033[2K\r')
        printtable(table)
    if not check_win(table):
        print('\033[2KНичья!')
    else:
        print('\033[2KПобеда ноликов!' if x_or_o else '\033[2KПобеда крестиков!')
    answer = input('Повторить? (y/n):')
    print('\033[A\033[2K\r')
