import unittest

import ipv7

class TestParser(unittest.TestCase):
  def test_parse_supernet_sequences(self):
    self.assertEqual(ipv7.Parser('').supernet_sequences(), [])
    self.assertEqual(ipv7.Parser('a').supernet_sequences(), ['a'])
    self.assertEqual(ipv7.Parser('a[b]').supernet_sequences(), ['a'])
    self.assertEqual(ipv7.Parser('a[b]c').supernet_sequences(), ['a', 'c'])
    self.assertEqual(ipv7.Parser('a[b][c]d').supernet_sequences(), ['a', 'd'])

  def test_parse_hypernet_sequences(self):
    self.assertEqual(ipv7.Parser('').hypernet_sequences(), [])
    self.assertEqual(ipv7.Parser('a').hypernet_sequences(), [])
    self.assertEqual(ipv7.Parser('a[b]').hypernet_sequences(), ['b'])
    self.assertEqual(ipv7.Parser('a[b]c').hypernet_sequences(), ['b'])
    self.assertEqual(ipv7.Parser('a[b][c]d').hypernet_sequences(), ['b', 'c'])

class TestModule(unittest.TestCase):
  def test_is_abba_sequence(self):
    self.assertNotABBA('')
    self.assertNotABBA('bcba')
    self.assertNotABBA('aaaa')
    self.assertIsABBA('abba')

  def test_is_aba_sequence(self):
    self.assertNotABA('')
    self.assertNotABA('aaa')
    self.assertNotABA('bba')
    self.assertIsABA('bcb')

  def assertIsABA(self, sequence):
    self.assertTrue(ipv7.is_valid_subsequence(ipv7.ABA_LENGTH, sequence))

  def assertNotABA(self, sequence):
    self.assertFalse(ipv7.is_valid_subsequence(ipv7.ABA_LENGTH, sequence))

  def assertIsABBA(self, sequence):
    self.assertTrue(ipv7.is_valid_subsequence(ipv7.ABBA_LENGTH, sequence))

  def assertNotABBA(self, sequence):
    self.assertFalse(ipv7.is_valid_subsequence(ipv7.ABBA_LENGTH, sequence))

class TestAddress(unittest.TestCase):
  def test_supports_tls(self):
    self.assertSupportsTLS(['abba', 'kdj'], ['aabbc', 'xyz'])
    self.assertNotSupportsTLS(['abba', 'baab'], ['abba'])

  def assertSupportsTLS(self, supernet_sequences, hypernet_sequences):
    self.assertTrue(ipv7.Address(supernet_sequences, hypernet_sequences).supports_tls())

  def assertNotSupportsTLS(self, supernet_sequences, hypernet_sequences):
    self.assertFalse(ipv7.Address(supernet_sequences, hypernet_sequences).supports_tls())
