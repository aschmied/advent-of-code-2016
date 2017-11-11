import unittest

import ipv7

class TestPacketParser(unittest.TestCase):
  def test_parse_sequences(self):
    self.assertEqual(ipv7.Parser('').sequences(), [])
    self.assertEqual(ipv7.Parser('a').sequences(), ['a'])
    self.assertEqual(ipv7.Parser('a[b]').sequences(), ['a'])
    self.assertEqual(ipv7.Parser('a[b]c').sequences(), ['a', 'c'])
    self.assertEqual(ipv7.Parser('a[b][c]d').sequences(), ['a', 'd'])

  def test_parse_hypertext_sequences(self):
    self.assertEqual(ipv7.Parser('').hypertext_sequences(), [])
    self.assertEqual(ipv7.Parser('a').hypertext_sequences(), [])
    self.assertEqual(ipv7.Parser('a[b]').hypertext_sequences(), ['b'])
    self.assertEqual(ipv7.Parser('a[b]c').hypertext_sequences(), ['b'])
    self.assertEqual(ipv7.Parser('a[b][c]d').hypertext_sequences(), ['b', 'c'])
