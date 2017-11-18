def get(protocol_version):
  if protocol_version == 1:
    return Version1Decoder()
  elif protocol_version == 2:
    return Version2Decoder()
  else:
    raise ValueError('Protocol version {} does not exist'.format(protocol_version))

class Version1Decoder(object):
  def decode(self, coded):
    self.init(coded)
    try:
      self._decode_chars()
    except StopIteration:
      pass
    return ''.join(self._decoded_chars)

  def init(self, coded):
    self._coded = coded
    self._citr = iter(coded)
    self._decoded_chars = []

  def _decode_chars(self):
    while True:
      c = self._citr.next()
      if c == '(':
        self._handle_repeat_instruction()
      else:
        self._decoded_chars.append(c)

  def _handle_repeat_instruction(self):
    repeat_command_string = self._scan_repeat_command()
    string_length, repeat_count = _parse_repeat_command(repeat_command_string)
    self._do_repeat(string_length, repeat_count)

  def _scan_repeat_command(self):
    chars = []
    c = self._citr.next()
    while c != ')':
      chars.append(c)
      c = self._citr.next()
    return ''.join(chars)

  def _do_repeat(self, string_length, repeat_count):
    chars = []
    for _ in xrange(string_length):
      c = self._citr.next()
      chars.append(c)
    self._decoded_chars += chars * repeat_count

class Version2Decoder(object):
  def len_decoded(self, coded):
    return self._len_decoded(coded)

  def _len_decoded(self, coded):
    if len(coded) == 0:
      return 0
    head, repeat_command_string, tail = self._split_at_first_repeat_command(coded)
    string_length, repeat_count = _parse_repeat_command(repeat_command_string)
    repeated_string = tail[0:string_length]
    leftover_tail = tail[string_length:]
    return len(head) + repeat_count * self._len_decoded(repeated_string) + self._len_decoded(leftover_tail)

  def _split_at_first_repeat_command(self, coded):
    head, tail = self._split_on_first_occurrence(coded, '(')
    if tail == None:
      return head, '0x0', ''
    repeat_command, leftover_tail = self._split_on_first_occurrence(tail, ')')
    return head, repeat_command, leftover_tail

  def _split_on_first_occurrence(self, string, char):
    l = string.split(char, 1)
    if len(l) == 1:
      return l[0], None
    return l[0], l[1]

def _parse_repeat_command(string):
  string_length_string, repeat_count_string = string.split('x')
  return int(string_length_string), int(repeat_count_string)
