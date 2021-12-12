file = open("./inputs/day4_input.txt", "r")
input = file.read().split('\n\n')
input = [x.replace('\n', ' ').split() for x in input]
file.close

markChar = 'X'

def splitList(aList, numParts):
  length = len(aList)
  return [aList[i*length // numParts: (i+1)*length // numParts]
          for i in range(numParts)]
  
def markNumber(boards, old, new):
  for board in boards:
    for row in board:
      for j, num in enumerate(row):
        if num == old:
          row[j] = new

def isBingo(boards, breakOnFirstWin):
  bingoed = []
  for i, board in enumerate(boards):
    if isRowMarked(board) or isColMarked(board):
      if breakOnFirstWin:
        return [True, i]
      else:
        bingoed.append(i)
  if not breakOnFirstWin and len(bingoed) > 0:
    return [True, bingoed]
  return [False, -1]

def isRowMarked(board):
  for row in board:
    if len(set(row)) <= 1:
      return True
  return False

def isColMarked(board):
  # assume square board
  for i in range(len(board[0])):
    col = [c[i] for c in board]
    if len(set(col)) <= 1:
      return True
  return False

def sumUnmarked(board, markChar):
  sumBoard = 0
  
  for row in board:
    for num in row:
      if num != markChar:
        sumBoard += int(num)
        
  return sumBoard

# part 1
draws = [x.split(',') for x in input.pop(0)][0]
boards = []
for i in range(len(input)):
  boards.append(splitList(input[i], 5))

for round in draws:
  markNumber(boards, round, markChar)
  bingo = isBingo(boards, True)
  if bingo[0]:
    print('Part 1:', sumUnmarked(boards[bingo[1]], markChar) * int(round))
    break
  

# part 2
draws = [x.split(',') for x in input.pop(0)][0]
boards = []
for i in range(len(input)):
  boards.append(splitList(input[i], 5))

boardsBingoed = set()
lastBingoed = {}
for round in draws:
  markNumber(boards, round, markChar)
  bingo = isBingo(boards, False)
  if bingo[0]:
    lastBingoed = boardsBingoed.symmetric_difference(set(bingo[1]))
    boardsBingoed.update(bingo[1])
    if len(boardsBingoed) == len(boards):
      print('Part 2:', sumUnmarked(boards[lastBingoed.pop()], markChar) * int(round))
      break
