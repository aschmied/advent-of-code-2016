class RoomID(object):
  @classmethod
  def from_string(cls, room_id_string):
    name = RoomID.extract_name(room_id_string)
    sequence_number = int(RoomID.extract_sequence_number(room_id_string))
    checksum = RoomID.extract_checksum(room_id_string)
    return cls(name, sequence_number, checksum)

  @staticmethod
  def extract_name(room_id_string):
    index_of_last_dash = room_id_string.rfind('-')
    return room_id_string[0:index_of_last_dash]

  @staticmethod
  def extract_sequence_number(room_id_string):
    index_of_last_dash = room_id_string.rfind('-')
    index_of_open_square = room_id_string.find('[')
    return room_id_string[index_of_last_dash + 1: index_of_open_square]

  @staticmethod
  def extract_checksum(room_id_string):
    index_of_open_square = room_id_string.find('[')
    index_of_close_square = len(room_id_string) - 1
    return room_id_string[index_of_open_square + 1:index_of_close_square]

  def __init__(self, encrypted_name, sector_id, checksum):
    self.encrypted_name = encrypted_name
    self.sector_id = sector_id
    self.checksum = checksum

  def is_valid(self):
    return self.calculated_checksum() == self.checksum

  def calculated_checksum(self):
    char_counts = self.count_chars(self.encrypted_name)
    del char_counts['-']
    char_count_tuples = zip(char_counts.keys(), char_counts.values())
    sorted_char_count_tuples = self.sort_char_count_tuples(char_count_tuples)
    top_five = sorted_char_count_tuples[0:5]
    return ''.join([char for (char, count) in top_five])

  def count_chars(self, string):
    char_counts = {}
    for char in string:
      if not char in char_counts:
        char_counts[char] = 0
      char_counts[char] += 1
    return char_counts

  def sort_char_count_tuples(self, char_count_tuples):
    def cmp(lhs, rhs):
      lchar = lhs[0]
      rchar = rhs[0]
      lcount = lhs[1]
      rcount = rhs[1]
      if lcount < rcount:
        return 1
      elif lcount > rcount:
        return -1
      if lchar < rchar:
        return -1
      elif lchar > rchar:
        return 1
      return 0
    return sorted(char_count_tuples, cmp)

class ShiftCypher(object):
  _alphabet_length = 26

  def __init__(self, shift_length):
    self._shift_length = shift_length

  def decrypt_string(self, string):
    return ''.join([self.decrypt_char(char) for char in string])

  def decrypt_char(self, char):
    if char == '-':
      return ' '
    encrypted_char_index = self.char_to_int(char)
    decrypted_char_index = (encrypted_char_index + self._shift_length) % self._alphabet_length
    return self.int_to_char(decrypted_char_index)

  def char_to_int(self, char):
    return ord(char) - ord('a')

  def int_to_char(self, int):
    return chr(int + ord('a'))
