file = open("./inputs/day2_input.txt", "r")
input = [line.strip('\n') for line in file]
file.close

# part 1
horizontal = 0
depth = 0

for line in input:
  direction = line.split(' ')
  if direction[0] == 'forward':
    horizontal += int(direction[1])
  elif direction[0] == 'up':
    depth -= int(direction[1])
  elif direction[0] == 'down':
    depth += int(direction[1])
    
print('Part 1:', horizontal * depth)


# part 2
horizontal = 0
depth = 0
aim = 0

for line in input:
  direction = line.split(' ')
  if direction[0] == 'forward':
    horizontal += int(direction[1])
    depth += aim * int(direction[1])
  elif direction[0] == 'up':
    aim -= int(direction[1])
  elif direction[0] == 'down':
    aim += int(direction[1])
    
print('Part 2:', horizontal * depth)
