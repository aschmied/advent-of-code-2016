import vector

def parse_commands(string):
  split = string.split(',')
  return map(lambda s: s.strip(), split)

def main():
  with open('input') as f:
    input = f.read()
  commands = parse_commands(input)

  v = vector.VectorWithPathHistory(vector.Vector())
  ce = vector.CommandExecutor(v)
  for command in commands:
    ce.execute(command)

  print(vector.manhattan_distance_from_origin(v.position()))
  print(vector.manhattan_distance_from_origin(v.first_position_visited_twice()))

if __name__ == '__main__':
  main()
