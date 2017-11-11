class Parser(object):
  def __init__(self, string):
    self._sequences = []
    self._hypertext_sequences = []
    self._sequence_builder = []
    self._is_hypertext = False
    self._parse(string)

  def _parse(self, string):
    for char in string:
      if char == '[':
        if not self._is_hypertext:
          self._finish_sequence(self._sequences)
        self._is_hypertext = True
      elif char == ']':
        if self._is_hypertext:
          self._finish_sequence(self._hypertext_sequences)
        self._is_hypertext = False
      else:
        self._append_char_to_sequence_builder(char)
    
    if self._is_hypertext:
      self._finish_sequence(self._hypertext_sequences)
    else:
      self._finish_sequence(self._sequences)

  def _finish_sequence(self, sequences):
    if len(self._sequence_builder) == 0:
      return
    sequences.append(''.join(self._sequence_builder))
    self._sequence_builder = []

  def _append_char_to_sequence_builder(self, char):
    self._sequence_builder += char

  def sequences(self):
    return self._sequences

  def hypertext_sequences(self):
    return self._hypertext_sequences
