#Written By Siddhanth Jaiswal

import random,os,time,sys,tkinter

def ran():
  return random.randint(1,9)
def print_game(Mtemp):
  c=1
  print("   1  2  3    4  5  6    7  8  9")
  print("")
  for i in range(0,9):
    print(c,"  ",end="")
    c+=1
    for j in range(0,9):
      if(j==2 or j==5):
        print(Mtemp[i][j]," | ",end='')
      else:
        print(Mtemp[i][j]," ",end='')
    if(i==2 or i==5):
      print("\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    print("")  
def diff_selection():
  diff=input()
  if diff=='1'or diff=='2'or diff=='3':
    return diff
  else:
    print("Invalid Input.Please enter a number between 1 and 3.")
    return diff_selection()
def sudoku_generator():
  def default_matrix():
    return [[0 for j in range(0,9)] for i in range(0,9)]
  def check_valid(m,r,c):
    c1=c2=c3=0
    if m[r][c]==" ":
      return True
    if m[r][c]>9:
      return True
    elif m[r][c]==0:
      return False
    else:
      for i in range(0,9):
        if(m[i][c]==m[r][c]):
          c1+=1
        if(m[r][i]==m[r][c]):
          c2+=1
      for i in range((r//3)*3,(r//3)*3+3):
        for j in range((c//3)*3,(c//3)*3+3):
          if(m[i][j]==m[r][c]):
            c3+=1
      if(c1==1 and c2==1 and c3==1):
        return True
      else:
        return False    
  def create_gamematrix(): 
    for i in range(0,9):
      for j in  range(0,9):
        t=ran()
        for k in range(0,10):
          M[i][j]=t
          if k<9:
            if(t<10):
              if(check_valid(M,i,j)==True):
                M[i][j]=t
                break
              else:
                t+=1
            else:
              t=1
          else:
            M[i][j]=(i+j)*100
  def true_sudoku(Mtemp):
    c=0
    for i in range(0,9):
      for j in range(0,9):
        if check_valid(Mtemp,i,j):
          c+=1
    if c==81:
      return True
    else:
      return False
  def PONT():
    for i in range(9):
      for j in range(9):
        if M[i][j]>9:
          M[i][j]=0

  while True:#SEARCHING
      M=default_matrix()
      create_gamematrix()
      PONT()
      if true_sudoku(M):
        break#SUDOKU FOUND,STORED IN 'M'
  return M
def insert_space(mtemp,difftemp):
  if difftemp==1:
    temp=4
  elif difftemp==2:
    temp=6
  else:
    temp=7
  for i in range(9):
    c=0
    while True:
      t=ran()-1
      if mtemp[i][t]!=" ":
        mtemp[i][t]=" "
        c+=1
      if c==temp:
        break
  return mtemp
def check_valid_main(m,r,c):
    c1=c2=c3=0
    if m[r][c]==' ':
      return False
    for i in range(0,9):
      if(m[i][c]==m[r][c]):
        c1+=1
      if(m[r][i]==m[r][c]):
        c2+=1
    for i in range((r//3)*3,(r//3)*3+3):
      for j in range((c//3)*3,(c//3)*3+3):
        if(m[i][j]==m[r][c]):
          c3+=1
    if(c1==1 and c2==1 and c3==1):
      return True
    else:
      return False  
def true_sudoku_main(Mtemp):
    c=0
    for i in range(0,9):
      for j in range(0,9):
        if check_valid_main(Mtemp,i,j):
          c+=1
    if c==81:
      return True
    else:
      return False
def main_game():
  print("Enter a difficulty")
  print("Press 1 for easy")
  print("Press 2 for medium")
  print("Press 3 for difficult")
  diff=diff_selection()
  time.sleep(0.5)
  print("Please wait, your game is loading")
  Matrix=sudoku_generator()
  m=[[Matrix[i][j] for j in range(0,9)] for i in range(0,9)]
  m=insert_space(m,int(diff))
  while True:
    os.system('cls')
    print_game(m)
    print("Enter your answers in the following pattern:")
    print("<row><column><space><number to input>")
    print("")
    wrong=0
    while True:#to get valid answer once
      userinput=input()
      if len(userinput)==4:
        try:
          rc=int(userinput[0])-1
          cc=int(userinput[1])-1
          tocheck=int(userinput[3])
        except ValueError:
          print("Invalid Input.Please read the Instructions!!!")
        if m[rc][cc]==" ":#FIXING OVERLAPPING
          m[rc][cc]=tocheck
          if tocheck==Matrix[rc][cc]:
            print("Correct Number!")
            time.sleep(1)
            break
          else:
            if wrong==3:
              print(3-(wrong+1)," chances are remaining")
              print("You lost!!")
              print("Thanks for playing my game!!")
              time.sleep(2)
              print("Written and Designed by Siddhanth Jaiswal.")
              time.sleep(15)
              sys.exit()
            else:
              print("Wrong Number!")
              print(3-(wrong+1)," chances are remaining")
              wrong+=1 
            m[rc][cc]=" "
        else:
          print("Invalid index!!.You can only fill blank digits")
      else:
        print("Invalid Input.Please read the Instructions!!!")
    if true_sudoku_main(m):
      os.system('cls')
      print_game(m)
      break
  if true_sudoku_main(m):
    print("You won!!!")
    print("Thanks for playing my game!!")
    time.sleep(2)
    print("Written and Designed by Siddhanth Jaiswal.")
    time.sleep(15)
main_game()