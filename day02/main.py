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

  code = []
  for command_line in command_lines:
    cle.execute(command_line)
    position = cle.vector().position()
    symbol = POSITION_TO_SYMBOL[position[1]][position[0]]
    code.append(symbol)

  print(''.join(code))

if __name__ == '__main__':
  main()
