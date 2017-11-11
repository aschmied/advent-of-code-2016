import unittest

import ipv7

class TestParser(unittest.TestCase):
  def test_parse_sequences(self):
    self.assertEqual(ipv7.Parser('').sequences(), [])
    self.assertEqual(ipv7.Parser('a').sequences(), ['a'])
    self.assertEqual(ipv7.Parser('a[b]').sequences(), ['a'])
    self.assertEqual(ipv7.Parser('a[b]c').sequences(), ['a', 'c'])
    self.assertEqual(ipv7.Parser('a[b][c]d').sequences(), ['a', 'd'])

  def test_parse_hypernet_sequences(self):
    self.assertEqual(ipv7.Parser('').hypernet_sequences(), [])
    self.assertEqual(ipv7.Parser('a').hypernet_sequences(), [])
    self.assertEqual(ipv7.Parser('a[b]').hypernet_sequences(), ['b'])
    self.assertEqual(ipv7.Parser('a[b]c').hypernet_sequences(), ['b'])
    self.assertEqual(ipv7.Parser('a[b][c]d').hypernet_sequences(), ['b', 'c'])

class TestModule(unittest.TestCase):
  def test_is_abba_sequence(self):
    self.assertNotABBA('')
    self.assertNotABBA('abcba')
    self.assertNotABBA('aaaa')
    self.assertIsABBA('abba')

  def assertIsABBA(self, sequence):
    self.assertTrue(ipv7.is_abba_sequence(sequence))

  def assertNotABBA(self, sequence):
    self.assertFalse(ipv7.is_abba_sequence(sequence))
