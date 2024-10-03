#!/usr/bin/python3

def pascal_row(row_num, previous_row):
    row = [1] * row_num
    for j in range(1, row_num - 1):
        row[j] = previous_row[j - 1] + previous_row[j]
    return row

def pascal_triangle(n):
    if n <= 0:
        return []
    
    lists = [[1]]
    print(lists[0])
    
    for i in range(2, n + 1):
        row = pascal_row(i, lists[i - 2])
        print(row)
        lists.append(row)
    
    return lists

if __name__ == "__main__":
    n = int(input("n: "))
    pascal_triangle(n)
