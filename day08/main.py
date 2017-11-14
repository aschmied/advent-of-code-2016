import screen

def main():
  with open('input') as f:
    input = f.read()
  
  parser = screen.ScriptParser(input)

  s = screen.Screen(50, 6)
  for instruction in parser.instructions():
    instruction.execute(s)

  s.draw()
  print(s.count_enabled())

if __name__ == '__main__':
  main()
