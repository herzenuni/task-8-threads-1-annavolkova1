import threading

X = [[9, 8], [7, 6]]
Y = [[5, 4], [3, 2]]

def calculate_element(row, col):
    Z = 0

    for i, item in enumerate(row):
        Z += item * col[i]
    return Z

def calculate_row(rowA, Y):
    cols = [[row[i] for row in Y] for i in range(len(Y[0]))]
    Z = list(map(lambda x: calculate_element(rowA, x), cols))
    print(Z)
    return Z

for row in X:
    threading.Thread(target=calculate_row, args=(row, Y)).start()