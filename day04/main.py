import room

def main():
  with open('input') as f:
    lines = f.readlines()
  
  sector_id_sum = 0
  for line in lines:
    room_id = room.RoomID.from_string(line.strip())
    if room_id.is_valid():
      sector_id_sum += room_id.sector_id

  print(sector_id_sum)

if __name__ == '__main__':
  main()
