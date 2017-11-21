class ChipKeeper(object):
  def __init__(self, number):
    self._number = number
    self._chips = []

  def number(self):
    return self._number

  def chips(self):
    return self._chips

  def give(self, chip):
    self._chips.append(chip)

class Bot(ChipKeeper):
  def __init__(self, bot_number):
    super(Bot, self).__init__(bot_number)

  def set_low_chip_dest(self, dest):
    self._low_chip_dest = dest

  def set_high_chip_dest(self, dest):
    self._high_chip_dest = dest

  def give(self, chip):
    super(Bot, self).give(chip)
    if self._ready_to_pass_chips():
      self._pass_chips()

  def _ready_to_pass_chips(self):
    return len(self.chips()) == 2

  def _pass_chips(self):
    chips = self.chips()
    chips.sort()
    low = chips[0]
    high = chips[1]
    self._low_chip_dest.give(low)
    self._high_chip_dest.give(high)

class Output(ChipKeeper):
  def __init__(self, output_number):
    super(Output, self).__init__(output_number)

class Net(object):
  def __init__(self):
    self._bots = {}
    self._outputs = {}

  def get(self, type, number):
    if type == 'bot':
      return self.get_bot(number)
    elif type == 'output':
      return self.get_output(number)
    else:
      return ValueError('Unknown type: {}'.format(type))

  def get_bot(self, bot_number):
    if bot_number not in self._bots:
      self._bots[bot_number] = Bot(bot_number)
    return self._bots[bot_number]

  def bot_count(self):
    return len(self._bots)

  def bots(self):
    return self._bots.values()

  def get_output(self, output_number):
    if output_number not in self._outputs:
      self._outputs[output_number] = Output(output_number)
    return self._outputs[output_number]

  def output_count(self):
    return len(self._outputs)

class Parser(object):
  def __init__(self, input):
    self._value_instructions = []
    self._give_instructions = []
    self._parse(input)

  def value_instructions(self):
    return self._value_instructions

  def give_instructions(self):
    return self._give_instructions

  def _parse(self, input):
    for line in input.strip().split('\n'):
      self._parse_line(line)

  def _parse_line(self, line):
    tokens = line.strip().split(' ')
    command = tokens[0]
    args = tokens[1:]
    self._create_instruction_object(command, args)

  def _create_instruction_object(self, command, args):
    if command == 'value':
      self._value_instructions.append(ValueInstruction.from_args(args))
    elif command == 'bot':
      self._give_instructions.append(GiveInstruction.from_args(args))
    else:
      raise ValueError('Invalid instruction: {}'.format(command))

class ValueInstruction(object):
  @classmethod
  def from_args(cls, args):
    chip_number = int(args[0])
    bot_number = int(args[4])
    return cls(chip_number, bot_number)

  def __init__(self, chip_number, bot_number):
    self._chip_number = chip_number
    self._bot_number = bot_number

  def execute(self, net):
    bot = net.get_bot(self._bot_number)
    bot.give(self._chip_number)

class GiveInstruction(object):
  @classmethod
  def from_args(cls, args):
    bot_number = int(args[0])
    low_dest_type = args[4]
    low_dest_number = int(args[5])
    high_dest_type = args[9]
    high_dest_number = int(args[10])
    return cls(bot_number, low_dest_type, low_dest_number, high_dest_type, high_dest_number)

  def __init__(self, bot_number, low_dest_type, low_dest_number, high_dest_type, high_dest_number):
    self._bot_number = bot_number
    self._low_dest_type = low_dest_type
    self._low_dest_number = low_dest_number
    self._high_dest_type = high_dest_type
    self._high_dest_number = high_dest_number

  def execute(self, net):
    bot = net.get_bot(self._bot_number)
    low_dest = net.get(self._low_dest_type, self._low_dest_number)
    high_dest = net.get(self._high_dest_type, self._high_dest_number)
    bot.set_low_chip_dest(low_dest)
    bot.set_high_chip_dest(high_dest)
