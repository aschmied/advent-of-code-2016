import vector

def parse_commands_from_input(input):
  split = input.split(',')
  return map(lambda s: s.strip(), split)

if __name__ == '__main__':
  with open('input') as f:
    input = f.read()
  commands = parse_commands_from_input(input)

  v = vector.Vector()
  m = vector.Mover(v)
  for command in commands:
    m.execute_command(command)

  print(vector.manhattan_distance_from_origin(v))  
