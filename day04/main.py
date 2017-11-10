import room

def main():
  with open('input') as f:
    lines = f.readlines()
  
  sector_id_sum = 0
  northpole_storage_room = None

  for line in lines:
    room_id = room.RoomID.from_string(line.strip())
    if room_id.is_valid():
      sector_id_sum += room_id.sector_id
      decrypted_name = decrypted_room_name(room_id)
      if is_northpole_object_storage_room(decrypted_name):
        northpole_storage_room_id = room_id

  print(sector_id_sum)
  print(northpole_storage_room_id.sector_id)

def decrypted_room_name(room_id):
  cypher = room.ShiftCypher(room_id.sector_id)
  return cypher.decrypt_string(room_id.encrypted_name)

def is_northpole_object_storage_room(decrypted_name):
  return decrypted_name == 'northpole object storage'

if __name__ == '__main__':
  main()
