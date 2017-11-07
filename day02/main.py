import vector

# Vector origin is in the southwest corner.
POSITION_TO_SYMBOL = {
  2: ['1', '2', '3'],
  1: ['4', '5', '6'],
  0: ['7', '8', '9'],
}

def main():
  with open('input') as f:
    command_lines = f.read().strip().split('\n')

  v = vector.BoundedVector(vector.Vector(1, 1), 2, 2)
  cle = vector.CommandLineExecutor(vector.CommandExecutor(v))

  sequence = []
  for command_line in command_lines:
    cle.execute(command_line)
    position = cle.vector().position()
    sequence.append(position_to_symbol(position))

  print(''.join(sequence))

def position_to_symbol(position):
  x = position[0]
  y = position[1]
  return POSITION_TO_SYMBOL[y][x]

if __name__ == '__main__':
  main()
