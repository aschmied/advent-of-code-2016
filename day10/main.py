import chipbot

def main():
  input = read_input('input')
  parser = chipbot.Parser(input)
  net = chipbot.Net()

  for instruction in parser.give_instructions():
    instruction.execute(net)

  for instruction in parser.value_instructions():
    instruction.execute(net)

  print(find_the_special_bot(net).number())
  print(product_of_chip_numbers_for_outputs(net, [0, 1, 2]))

def read_input(filename):
  with open(filename) as f:
    return f.read()

def find_the_special_bot(net):
  for bot in net.bots():
    if bot.chips() == [17, 61]:
      return bot

def product_of_chip_numbers_for_outputs(net, output_numbers):
  product_of_chip_numbers = 1
  for output_number in output_numbers:
    output = net.get_output(output_number)
    product_of_chip_numbers *= output.chips()[0]
  return product_of_chip_numbers

if __name__ == '__main__':
  main()
