ABBA_LENGTH = 4

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

  def supports_tls(self):
    return (any(map(contains_abba_sequence, self._supernet_sequences)) and
        not any(map(contains_abba_sequence, self._hypernet_sequences)))

def contains_abba_sequence(sequence):
  n = len(sequence)
  for start_index in xrange(n - ABBA_LENGTH + 1):
    end_index = start_index + ABBA_LENGTH
    if is_abba_sequence(sequence[start_index:end_index]):
      return True
  return False

def is_abba_sequence(sequence):
  return (len(sequence) == ABBA_LENGTH and
      sequence[0:2] == sequence[3:1:-1] and
      sequence[0] != sequence[1])
