with open('day4.txt') as prompt:
    wordsearch = prompt.read().splitlines()
xmas_count = 0
x_mas_count = 0

def check_for_next_letter(wordsearch, x, y, next_letter, direction):
    match direction:
        case 'up':
            if y >= 0 and wordsearch[y][x] == next_letter:
                return True
        case 'down':
            if y < len(wordsearch) and wordsearch[y][x] == next_letter:
                return True
        case 'left':
            if x >= 0 and wordsearch[y][x] == next_letter:
                return True
        case 'right':
            if x < len(wordsearch[y]) and wordsearch[y][x] == next_letter:
                return True
        case 'up-left':
            if y >= 0 and x >= 0 and wordsearch[y][x] == next_letter:
                return True
        case 'up-right':
            if y >= 0 and x < len(wordsearch[y]) and wordsearch[y][x] == next_letter:
                return True
        case 'down-left':
            if y < len(wordsearch) and x >= 0 and wordsearch[y][x] == next_letter:
                return True
        case 'down-right':
            if y < len(wordsearch) and x < len(wordsearch[y]) and wordsearch[y][x] == next_letter:
                return True
    return False

for y, row in enumerate(wordsearch):
    for x, col in enumerate(row):
        if col == 'X':
            directions_and_incs = [['up', (0, -1)], ['up-right', (1, -1)], ['right', (1, 0)], ['down-right', (1, 1)], ['down', (0, 1)], ['down-left', (-1, 1)], ['left', (-1, 0)], ['up-left', (-1, -1)]]
            for direction_and_inc in directions_and_incs:
                if check_for_next_letter(wordsearch, x + direction_and_inc[1][0], y + direction_and_inc[1][1], 'M', direction_and_inc[0]):
                    if check_for_next_letter(wordsearch, x + direction_and_inc[1][0] * 2, y + direction_and_inc[1][1] * 2, 'A', direction_and_inc[0]):
                        if check_for_next_letter(wordsearch, x + direction_and_inc[1][0] * 3, y + direction_and_inc[1][1] * 3, 'S', direction_and_inc[0]):
                            xmas_count += 1
        elif y > 0 and y < len(wordsearch) - 1 and x > 0 and x < len(wordsearch[y]) - 1 and col == 'A':
            directions_and_incs = [['up-right', (1, -1)], ['down-right', (1, 1)], ['down-left', (-1, 1)], ['up-left', (-1, -1)]]
            mas_count = 0
            for direction_and_inc in directions_and_incs:
                if check_for_next_letter(wordsearch, x + direction_and_inc[1][0], y + direction_and_inc[1][1], 'M', direction_and_inc[0]):
                    if check_for_next_letter(wordsearch, x + direction_and_inc[1][0] * -1, y + direction_and_inc[1][1] * -1, 'S', direction_and_inc[0]):
                        mas_count += 1
            if mas_count == 2:
                x_mas_count += 1

print("pt 1:", xmas_count)
print("pt 2:", x_mas_count)
