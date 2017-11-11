import hashlib

def md5_hash(string):
  return hashlib.md5(string).hexdigest()

class DoorCodeCalculator(object):
  DOOR_CODE_LENGTH = 8
  UNSET_DOOR_CODE_SYMBOL = " "
  def __init__(self, plaintext_prefix, hash_function):
    self._plaintext_prefix = plaintext_prefix
    self._hash_function = hash_function
    self._hash_index = -1
    
    self._first_door_code = []
    self._second_door_code = [self.UNSET_DOOR_CODE_SYMBOL] * self.DOOR_CODE_LENGTH

  def calculate(self):
    while not self.door_codes_complete():
      hashtext = self.next_hash()
      if self.is_usable_hash(hashtext):
        self.update_first_door_code_from_hash(hashtext)
        self.update_second_door_code_from_hash(hashtext)

  def door_codes_complete(self):
    # The second door code requires at least as many iterations to solve as the first.
    return self.UNSET_DOOR_CODE_SYMBOL not in self._second_door_code

  def next_hash(self):
    self._hash_index += 1
    return self._hash_function(self._plaintext_prefix + str(self._hash_index))

  def is_usable_hash(self, hash):
    return hash.startswith('00000')

  def update_first_door_code_from_hash(self, hash):
    if len(self._first_door_code) < 8:
      self._first_door_code += hash[5]

  def update_second_door_code_from_hash(self, hash):
    try:
      index = self.parse_door_code_index(hash[5])
      byte = hash[6]
      if self.is_door_code_index_unset(index):
        self._second_door_code[index] = byte
    except ValueError:
      pass

  def parse_door_code_index(self, string):
    index = int(string)
    if index >= self.DOOR_CODE_LENGTH:
      raise ValueError()
    return index

  def is_door_code_index_unset(self, index):
    return self._second_door_code[index] == self.UNSET_DOOR_CODE_SYMBOL

  def first_door_code(self):
    return ''.join(self._first_door_code)

  def second_door_code(self):
    return ''.join(self._second_door_code)
