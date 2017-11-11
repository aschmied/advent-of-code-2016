import dcc  

def main():
  calculator = dcc.DoorCodeCalculator('ojvtpuvg', dcc.md5_hash)
  calculator.calculate()
  print(calculator.first_door_code())
  print(calculator.second_door_code())


if __name__ == '__main__':
  main()
