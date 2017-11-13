import util

ABBA_LENGTH = 4
ABA_LENGTH = 3

class Parser(object):
  def __init__(self, string):
    self._supernet_sequences = []
    self._hypernet_sequences = []
    self._sequence_builder = []
    self._is_hypernet = False
    self._parse(string)

  def _parse(self, string):
    for char in string:
      if char == '[':
        self._start_hypernet_sequence()
      elif char == ']':
        self._end_hypernet_sequence()
      else:
        self._append_char_to_sequence_builder(char)
    self._end_input()

  def _start_hypernet_sequence(self):
    if not self._is_hypernet:
      self._finish_sequence(self._supernet_sequences)
    self._is_hypernet = True

  def _end_hypernet_sequence(self):
    if self._is_hypernet:
      self._finish_sequence(self._hypernet_sequences)
    self._is_hypernet = False

  def _append_char_to_sequence_builder(self, char):
    self._sequence_builder += char

  def _end_input(self):
    if self._is_hypernet:
      self._finish_sequence(self._hypernet_sequences)
    else:
      self._finish_sequence(self._supernet_sequences)

  def _finish_sequence(self, sequences):
    if len(self._sequence_builder) == 0:
      return
    sequences.append(''.join(self._sequence_builder))
    self._sequence_builder = []

  def supernet_sequences(self):
    return self._supernet_sequences

  def hypernet_sequences(self):
    return self._hypernet_sequences

class Address(object):
  @classmethod
  def parse(cls, string):
    parser = Parser(string)
    return cls(parser.supernet_sequences(), parser.hypernet_sequences())

  def __init__(self, supernet_sequences, hypernet_sequences):
    self._supernet_sequences = supernet_sequences
    self._hypernet_sequences = hypernet_sequences
    self._supernet_abba_sequences = util.map_flatten(self._find_abba_sequences, supernet_sequences)
    self._hypernet_abba_sequences = util.map_flatten(self._find_abba_sequences, hypernet_sequences)
    self._supernet_aba_sequences = util.map_flatten(self._find_aba_sequences, supernet_sequences)
    self._hypernet_aba_sequences = util.map_flatten(self._find_aba_sequences, hypernet_sequences)

  def _find_abba_sequences(self, sequence):
    return self._find_subsequences(ABBA_LENGTH, sequence)

  def _find_aba_sequences(self, sequence):
    return self._find_subsequences(ABA_LENGTH, sequence)

  def _find_subsequences(self, subsequence_length, sequence):
    subsequences = []
    n = len(sequence)
    for start_index in xrange(n - subsequence_length + 1):
      end_index = start_index + subsequence_length
      candidate = sequence[start_index:end_index]
      if is_valid_subsequence(subsequence_length, candidate):
        subsequences.append(candidate)
    return subsequences

  def supports_tls(self):
    return len(self._supernet_abba_sequences) > 0 and len(self._hypernet_abba_sequences) == 0

  # Complexity is O(n^2) for aba's stored in lists, but the
  # lists in this problem are short.
  def supports_ssl(self):
    for aba in self._supernet_aba_sequences:
      bab = self.aba_to_bab(aba)
      if bab in self._hypernet_aba_sequences:
        return True
    return False

  def aba_to_bab(self, aba):
    a = aba[0]
    b = aba[1]
    return b + a + b

def is_valid_subsequence(subsequence_length, subsequence):
  return (len(subsequence) == subsequence_length and
      subsequence[0] == subsequence[-1] and
      subsequence[1] == subsequence[-2] and
      subsequence[0] != subsequence[1])
