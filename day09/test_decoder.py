import unittest

import decoder

class TestDecoder(unittest.TestCase):
  def test_decode(self):
    self.assertDecoded("", "")
    self.assertDecoded("a", "a")
    self.assertDecoded("(0x0)abc", "abc")
    self.assertDecoded("(1x0)abc", "bc")
    self.assertDecoded("(0x1)abc", "abc")
    self.assertDecoded("(5x2)(2x2)", "(2x2)(2x2)")
    self.assertDecoded("aa(5x2)(2x2)d", "aa(2x2)(2x2)d")
    self.assertDecoded("(3x2)(2x2)", "(2x(2x2)")

  def assertDecoded(self, coded, decoded):
    self.assertEqual(decoder.Decoder(coded).decode(), decoded)
