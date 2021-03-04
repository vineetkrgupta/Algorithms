from collections import deque

def generate_series(n):

    to_visit = deque()
    to_visit.append((0, 0))

    prev_row, prev_col = -1, -1
    while to_visit:

        row, col = to_visit.popleft()

        if row == n:
            break

        if row == prev_row:
            print(' ' * col + str(col), end='')
        else:
            print(' ' * col + str(col))
            


        to_visit.append((row + 1, 2 * col))
        to_visit.append((row + 1, 2 * col + 1))

        prev_row = row
        prev_col = col


if __name__ == "__main__":
    generate_series(3)

    
