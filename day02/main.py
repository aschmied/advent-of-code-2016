import vector

VECTOR_DOMAIN_1 = [
  (0, 2), (1, 2), (2, 2),
  (0, 1), (1, 1), (2, 1),
  (0, 0), (1, 0), (2, 0),
]

POSITION_TO_SYMBOL_MAP_1 = {
  2: "123",
  1: "456",
  0: "789",
}

VECTOR_DOMAIN_2 = [
                  (2, 4),
          (1, 3), (2, 3), (3, 3),
  (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
          (1, 1), (2, 1), (3, 1),
                  (2, 0),
]

POSITION_TO_SYMBOL_MAP_2 = {
  4: "  1  ",
  3: " 234 ",
  2: "56789",
  1: " ABC ",
  0: "  D  ",
}

def main():
  with open('input') as f:
    process_input(VECTOR_DOMAIN_1, POSITION_TO_SYMBOL_MAP_1, f.read())
  with open('input') as f:
    process_input(VECTOR_DOMAIN_2, POSITION_TO_SYMBOL_MAP_2, f.read())

def process_input(domain, position_to_symbol_map, input):
  command_lines = input.strip().split('\n')

  v = vector.BoundedVector(vector.Vector(1, 1), vector.AllowedSquares(domain))
  cle = vector.CommandLineExecutor(vector.CommandExecutor(v))

  sequence = []
  for command_line in command_lines:
    cle.execute(command_line)
    position = cle.vector().position()
    sequence.append(position_to_symbol(position, position_to_symbol_map))

  print(''.join(sequence))

def position_to_symbol(position, position_to_symbol_map):
  x = position[0]
  y = position[1]
  return position_to_symbol_map[y][x]

if __name__ == '__main__':
  main()
