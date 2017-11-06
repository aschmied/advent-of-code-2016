import vector

def parse_commands_from_input(input):
  split = input.split(',')
  return map(lambda s: s.strip(), split)

if __name__ == '__main__':
  with open('input') as f:
    input = f.read()
  commands = parse_commands_from_input(input)

  v = vector.VectorWithPathHistory(vector.Vector())
  ce = vector.CommandExecutor(v)
  for command in commands:
    ce.execute(command)

  print(vector.manhattan_distance_from_origin(v.position()))
  print(vector.manhattan_distance_from_origin(v.first_position_visited_twice()))