import unittest

import decoder

class TestV1Decoder(unittest.TestCase):
  def setUp(self):
    self.protocol_version = 1
    self.decoder = decoder.get(self.protocol_version)

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
    self.assertEqual(self.decoder.decode(coded), decoded)

class TestV2Decoder(unittest.TestCase):
  def setUp(self):
    self.protocol_version = 2
    self.decoder = decoder.get(self.protocol_version)

  def test_len_decoded_base_cases(self):
    self.assertLenDecoded("", 0)
    self.assertLenDecoded("a", 1)
    self.assertLenDecoded("abc", 3)

  def test_len_decoded_singleton_repeats(self):
    self.assertLenDecoded("(0x0)abc", 3)
    self.assertLenDecoded("(0x1)abc", 3)
    self.assertLenDecoded("(1x1)abc", 3)
    self.assertLenDecoded("(2x2)abc", 5)

  def test_len_decoded_nested_repeats(self):
    self.assertLenDecoded("(6x2)(1x2)A", 4)
    self.assertLenDecoded("(6x2)(1x2)ABC(2x2)ZZ", 10)

  def assertLenDecoded(self, coded, len_decoded):
    self.assertEqual(self.decoder.len_decoded(coded), len_decoded)

class TestGet(unittest.TestCase):
  def test_invlid_protocol_version(self):
    with self.assertRaises(ValueError):
      decoder.get(3)
