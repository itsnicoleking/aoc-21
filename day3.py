from statistics import mode
from copy import deepcopy

file = open("./inputs/day3_input.txt", "r")
input = [line.strip('\n') for line in file]
file.close

bits = 12

# part 1
gammaStr = \
  mode([p[0] for p in input]) + \
  mode([p[1] for p in input]) + \
  mode([p[2] for p in input]) + \
  mode([p[3] for p in input]) + \
  mode([p[4] for p in input]) + \
  mode([p[5] for p in input]) + \
  mode([p[6] for p in input]) + \
  mode([p[7] for p in input]) + \
  mode([p[8] for p in input]) + \
  mode([p[9] for p in input]) + \
  mode([p[10] for p in input]) + \
  mode([p[11] for p in input])

gammaInt = int(gammaStr, 2)
epsilonBin = bin((gammaInt ^ (2 ** (bits+1) - 1)))[3:]

print('Print 1:', gammaInt * int(epsilonBin, 2))


# part 2
def getMode(dataset, defaultVal, anti=False):
  frequency = {}

  for value in dataset:
    frequency[value] = frequency.get(value, 0) + 1

  most_frequent = max(frequency.values())

  modes = [key for key, value in frequency.items() if value == most_frequent]
  
  if len(modes) == 1:
    if anti:
      return 1 if modes[0] == '0' else 0
    else:
      return modes[0]
  else:
    return defaultVal

def findLinesWherePosIsMode(linesArr, pos, mode):
  filteredArr = []

  for line in linesArr:
    if int(line[pos]) == int(mode):
      filteredArr.append(line)

  return filteredArr

def findRating(defaultMode, antiMode):
  filtered = deepcopy(input)

  for i in range(bits):
    if (len(filtered) == 1):
      break
    mode = getMode([p[i] for p in filtered], defaultMode, antiMode)
    filtered = findLinesWherePosIsMode(filtered, i, mode)

  return filtered[0]

oxy = int(findRating(1, False), 2)
co2 = int(findRating(0, True), 2)

print('Part 2:', oxy * co2)
