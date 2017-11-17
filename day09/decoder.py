class Decoder(object):
  def __init__(self, coded):
    self._coded = coded
    self._citr = iter(coded)
    self._decoded_chars = []

  def decode(self):
    try:
      self._decode_chars()
    except StopIteration:
      pass
    return ''.join(self._decoded_chars)

  def _decode_chars(self):
    while True:
      c = self._citr.next()
      if c == '(':
        self._handle_repeat_instruction()
      else:
        self._decoded_chars.append(c)

  def _handle_repeat_instruction(self):
    repeat_command_string = self._scan_repeat_command()
    string_length, repeat_count = self._parse_repeat_command(repeat_command_string)
    self._do_repeat(string_length, repeat_count)

  def _scan_repeat_command(self):
    chars = []
    c = self._citr.next()
    while c != ')':
      chars.append(c)
      c = self._citr.next()
    return ''.join(chars)

  def _parse_repeat_command(self, string):
    string_length_string, repeat_count_string = string.split('x')
    return int(string_length_string), int(repeat_count_string)

  def _do_repeat(self, string_length, repeat_count):
    chars = []
    for _ in xrange(string_length):
      c = self._citr.next()
      chars.append(c)
    self._decoded_chars += chars * repeat_count
