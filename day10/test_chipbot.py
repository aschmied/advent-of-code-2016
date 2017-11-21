import unittest

import chipbot

class TestBot(unittest.TestCase):
  def setUp(self):
    self.low_output = chipbot.Output(0)
    self.high_output = chipbot.Output(0)
    self.bot = chipbot.Bot(0)
    self.bot.set_low_chip_dest(self.low_output)
    self.bot.set_high_chip_dest(self.high_output)

  def test_give(self):
    self.bot.give(1)
    self.assertFalse(self.low_output.chips())
    self.assertFalse(self.high_output.chips())
    self.bot.give(0)
    self.assertEqual(self.low_output.chips(), [0])
    self.assertEqual(self.high_output.chips(), [1])

class TestNet(unittest.TestCase):
  def setUp(self):
    self.net = chipbot.Net()

  def test_get(self):
    self.assertBotCount(0)
    self.assertOutputCount(0)
    self.net.get('bot', 3)
    self.assertBotCount(1)
    self.assertOutputCount(0)
    self.net.get('output', 3)
    self.assertBotCount(1)
    self.assertOutputCount(1)

  def test_get_bot(self):
    self.assertBotCount(0)
    self.net.get_bot(0)
    self.assertBotCount(1)
    self.net.get_bot(0)
    self.assertBotCount(1)

  def test_get_output(self):
    self.assertOutputCount(0)
    self.net.get_output(0)
    self.assertOutputCount(1)
    self.net.get_output(0)
    self.assertOutputCount(1)

  def test_bots(self):
    self.assertEqual(self.net.bots(), [])
    self.net.get_bot(0)
    self.assertEqual(self.net.bots()[0].number(), 0)

  def assertBotCount(self, count):
    self.assertEqual(self.net.bot_count(), count)

  def assertOutputCount(self, count):
    self.assertEqual(self.net.output_count(), count)

class TestParser(unittest.TestCase):
  def test_parse(self):
    input = 'value 0 goes to bot 1\nbot 2 gives low to bot 3 and high to bot 4'
    parser = chipbot.Parser(input)
    value_instructions = parser.value_instructions()
    give_instructions = parser.give_instructions()
    self.assertInstance(value_instructions[0], chipbot.ValueInstruction)
    self.assertInstance(give_instructions[0], chipbot.GiveInstruction)

  def assertInstance(self, obj, cls):
    self.assertTrue(isinstance(obj, cls))

class TestValueInstruction(unittest.TestCase):
  def setUp(self):
    args = ['0', 'goes', 'to', 'bot', '1']
    self.instruction = chipbot.ValueInstruction.from_args(args)
    self.net = chipbot.Net()

  def test_execute(self):
    self.instruction.execute(self.net)
    bot = self.net.get_bot(1)
    self.assertEqual(bot.chips(), [0])

class TestGiveInstruction(unittest.TestCase):
  def setUp(self):
    args = ['2', 'gives', 'low', 'to', 'bot', '1', 'and', 'high', 'to', 'output', '0']
    self.instruction = chipbot.GiveInstruction.from_args(args)
    self.net = chipbot.Net()

  def test_execute(self):
    self.instruction.execute(self.net)
    bot = self.net.get_bot(2)
    self.assertTrue(isinstance(bot._low_chip_dest, chipbot.Bot))
    self.assertTrue(isinstance(bot._high_chip_dest, chipbot.Output))
    self.assertEqual(bot._low_chip_dest.number(), 1)
    self.assertEqual(bot._high_chip_dest.number(), 0)
