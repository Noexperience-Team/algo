
load_ext watermark
watermark --iversion
global n

n=4








import tkinter as tk
import GameBoard

def place_queen(E,R,i,j,k=1):
    
    
    #if safe(E,i,j):
    remplir(E,i,j,k)
    E[i][j]=R
   
    return E
imagedata = '''
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABmJLR0
QA/wD/AP+gvaeTAAAEHUlEQVRYhe2WW2wVVRSGvzVzOlNSKK0UKF5SLFQtkVA4QlJQjkis8CYJhQ
Zi4gMkiOADJtDgiwkvYhMuVdAYSXgSQqM2KqXBaFuChdgLRNKUS0m5yEXrKQWhds7pzPLh9ELLmb
ac4oMJ/9Oavdb6/3/23rP3wGP8n6HV9iattjeNhsNIXNwqBC0ELYzFiUESNlBj6wCikJMwV8LQar
tMq+2y0XAkvgQ11kyEPIQ8rbJeTJTHd9q0ijTEeg+RN4HnQCJAC+ghcGvB/AlI7invQt3XEHMByE
pgGqgFnEO0HDfyiSyiY8QG9FhyCNWynvxBVBoxMFHNAy1CsFEZO5BJ76I4IAdBTqF4iAZBi0BckE
IJdR0b1oBWJ81FjBpEfsDpWiuvc/vXiW9nRrqZY3imk1HQHM7Z0PA1kD2oteX8rrnLwz8/n+EZrm
0FaJzXtv+mVpGGYX8JLEW8V2RhtNHXgB7CZLJ9GrjBH87S42vfSTUMZy+wgvv2y7hp4RszSyonYW
ACqCvumc1vtN29OCHzPjoPOBBRb8OrX+z/m0y7EmUSC53ZInjxDVTZSzCowNMZR4tWXh0bsY6D5j
2wRsCzq+qYUtAMCjd+zKX1q7nxygBO2WMCLwcP7M8CaQKWSMg52psc+BUYLAbOyKLI2RQn8L6fOE
D3vQC0ufCXG4v9MdvpdDdJKNIMNCEsHig5ADoFuAQgIquGYu1sewJyLMixYvFQEO3lasXTJ/0NiN
wB0nqepg7N+lCIbVghvUfDx4BKPTBPjzMOaH+EBsJ6klSUlxCp8zeQ1FUOOLjJW1A98sjkVSroSi
4G+Qe3q9zXgMynHfgAtHjWzorfIP7p9ZC4Nau0ognRLYhuHXwiPnAXSMjZg7IjJbtjZ3BfeV3arJ
ttZnL0oVXNMVHG513/M7jvm/qUrPYdICWy0Pn8AT0/Aq22tiOy2VchakDDhFgcDEOS51sKul1Cke
J4maE+4PrewIuY3YblBjRquqpgWK5J+dNQlhUrKLwChZfxIqYrApLkmr09MX0a/ESGvY7DtVk0rF
kWiN6xubAr32zZnW8CcGJif9GJDABaduebF3blm9E7Ng1rlgXCtVnD0Q85AwCkB6+RvQ6SUh2eWt
7Un1h9CbbP6IlbAfrySakO2evqSA9eG9aA7x64fXLJeiWwRyXhf5aYgHqIG3l3/IKje0ds4PTZlk
WKVoJYo1Lvg0ZUKZiTm1MzOOPzerK6V3zbRyV8+/3hvszlK1fZ+uE2ms+d6xv77nAlH+8s5V5nZ9
/YwD6xDDHeiqsUb7CxuWWjCKW9gpmZk7Gt2GR0d3dz9ffrTM16BpFYe/utDlzXY2JG/6U0uE+UjX
m50z8dkYFDqub0sxfXGzBfRcx4NSOFqLrAL+dfmPbZChF3NFyP8Z/gX2+PicIBfSj6AAAAAElFTk
SuQmCC
'''
def print_board(board1,n):
    root1 = tk.Tk()
    
    board = GameBoard.GameBoard(root1,n)
    
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    t=[]
    for i,row in enumerate(board1):
        t.append(tk.PhotoImage(data=imagedata))
        for j,field in enumerate(row):
            if field=='q':
               
                board.addpiece('queen{}'.format(i), t[i], i,j) 
    
    root1.mainloop()
    





def can_place_queen(board, row, col):
    
    for field in board[row]:
        if field=='q': return False
    
    for i in range(len(board[0])):
        if board[i][col]=='q': return False
    i, j = row, col
    l = len(board)
    
    while i < l and j < l:
        if board[i][j]=='q': return False
        i, j = i + 1, j + 1
    i, j = row, col
   
    while i < l and j >= 0:
        if board[i][j]=='q': return False
        i, j = i + 1, j - 1
    i, j = row, col
    
    while i >= 0 and j < l:
        if board[i][j]=='q': return False
        i, j = i - 1, j + 1
    i, j = row, col
   
    while i >= 0 and j >= 0:
        if board[i][j]=='q': return False
        i, j = i - 1, j - 1
    return True
def remplir(T,i,j,k=1):
   
    
    for l in range(0,n):
        T[l][j]=k
    for c in range(0,n):
        T[i][c]=k
    ii, jj = i+1, j+1
    l = len(T)
    while ii < l and jj < l:
        T[ii][jj]=k
        ii, jj = ii + 1, jj + 1
    row=i
    col=j
    ii, jj = row+1, col-1
    while ii < l and jj >= 0:
        T[ii][jj]=k
        ii, jj = ii + 1, jj - 1
        
        
    row=i
    col=j
    ii, jj = row-1, col+1
    while ii >= 0 and jj < l:
        
       
        T[ii][jj]=k
        ii, jj = ii - 1, jj + 1
    
    
    return T
    







def place_queens(board, row=0):
    global nSolutions
    
    if row >= len(board):
        
        if nSolutions==1:
            print_board(board,n)

        nSolutions += 1
        return
    for col, field in enumerate(board):
        
        if board[row][col]==0:
            
            
            if can_place_queen(board, row, col):
                
                place_queen(board,'q',row,col)
                place_queens(board, row + 1)
                
                place_queen(board,0,row,col,0)
                
global entry
def run():
    n1=entry.get()
    n=int(n1)
    root.destroy()
root=tk.Tk()
label=tk.Label(text='donner la taille de votre echequier')
label.pack()
entry=tk.Entry()
entry.pack()
button=tk.Button(text='valider',command=run)
button.pack()
root.mainloop()
nSolutions = 0
board1 = [[0] * n for i in range(n)]
place_queens(board1)
print("Found %s solutions!" % nSolutions)






