if __name__ == '__main__':
  
  N = int(input())
  print(("Not weired " if N%2==0 and (N<=4 or N>20) else "") + "Weird")
