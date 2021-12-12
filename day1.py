file = open("./inputs/day1_input.txt", "r")
input = [int(line) for line in file]
file.close

# part 1
numIncreases = 0

for i in range(len(input)-1):
  if input[i+1] > input[i]:
    numIncreases+=1
  
print('Part 1:', numIncreases)


# part 2
numIncreases = 0

for i in range(len(input)-3):
  windowA = input[i] + input[i+1] + input[i+2]
  windowB = input[i+1] + input[i+2] + input[i+3]
  if windowB > windowA:
    numIncreases += 1

print('Part 2:', numIncreases)
