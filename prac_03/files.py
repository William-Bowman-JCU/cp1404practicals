name = input('Enter name: ')
out_file = open('./prac_03/name.txt', 'w')
print(name, file=out_file)
out_file.close()

in_file = open('./prac_03/name.txt', 'r')
name = in_file.readline().strip()
in_file.close()
print(f'Hi {name}!')

with open('./prac_03/numbers.txt', 'r') as in_file:
  number1 = int(in_file.readline())
  number2 = int(in_file.readline())
  print(number1 + number2)

total = 0
with open('./prac_03/numbers.txt', 'r') as in_file:
  for line in in_file:
    total += int(line)
  print(total) 