import unittest

import room

class TestRoomID(unittest.TestCase):
  def test_from_string(self):
    room_id = room.RoomID.from_string('aaaaa-bbb-z-y-x-123[abxyz]')
    self.assertEqual('aaaaa-bbb-z-y-x', room_id.encrypted_name)
    self.assertEqual(123, room_id.sector_id)
    self.assertEqual('abxyz', room_id.checksum)

  def test_is_valid_for_valid_room(self):
    room_id = room.RoomID.from_string('aaaaa-bbb-z-y-x-123[abxyz]')
    self.assertTrue(room_id.is_valid())

  def test_is_valid_for_invalid_room(self):
    room_id = room.RoomID.from_string('zzz-kdkdlsfj-123[abxyz]')
    self.assertFalse(room_id.is_valid())

class TestShiftCypher(unittest.TestCase):
  def setUp(self):
    self.cypher = room.ShiftCypher(1)

  def test_decrypt(self):
    self.assertEqual(self.cypher.decrypt_string('xyz-'), 'yza ')
