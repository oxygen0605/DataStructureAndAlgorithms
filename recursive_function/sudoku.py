# -*- coding: utf-8 -*-

# 数独パズル9×9 ソルバー
# 手法:再起関数を用いた深さ優先探索
# ref: https://qiita.com/drken/items/23a4f604fa3f505dd5ad

def printAns(res):
    print('\nanswer: ')
    for l in res:
        print(*l)

def solve_sudoku(field):
    
    # -1のマスを特定する。
    emp_i = -1
    emp_j = -1
    for i in range(9):
        for j in range(9):
            if field[i][j] == -1:
                emp_i = i
                emp_j = j
                break
        if emp_i != -1:
            break
    
    # 全部埋まったら標準出力する
    if(emp_i == -1) or (emp_j == -1):
        printAns(field)
        return
    
    # 空きマスに入れられる数字を求める。
    isAvailable = [True for i in range(10)]
    for i in range(9):
        
        #同じ列に同じ数字はダメ
        if field[emp_i][i] != -1:
            isAvailable[field[emp_i][i]] = False
        
        #同じ行に同じ数字はダメ
        if field[i][emp_j] != -1:
            isAvailable[field[i][emp_j]] = False

        #同じブロックに同じ数字はダメ
        bi = emp_i // 3 * 3 + 1
        bj = emp_j // 3 * 3 + 1
        for di in [bi-1, bi, bi+1]:
            for dj in [bj-1, bj, bj+1]:
                if field[di][dj] != -1:
                    #print(emp_i, emp_j, bi, bj, di,dj)
                    isAvailable[field[di][dj]] = False
    
    # 利用可能な数字で再帰関数
    for i in range(1,10):
        if isAvailable[i]:
            field[emp_i][emp_j] = i
            solve_sudoku(field)
    
    # 候補が全てダメだったら-1に戻す(重要！)
    field[emp_i][emp_j] = -1
    return

if __name__ == "__main__":
    
    field = [[-1 for j in range(9)] for i in range(9)]
    
    # 問題読み込み
    with open('sudoku_mondai.txt','r') as f:
        print("suudoku puzzle:")
        for i in range(9):
            line = f.readline()
            print(*line, end="")
            for j in range(9):
                l = line[j:j+1]
                if l == "*":
                    continue
                else:
                   field[i][j] = int(l)
    
    # ソルバー起動
    solve_sudoku(field)