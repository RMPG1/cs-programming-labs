kod = input()
category = kod[:3]
year = kod[4:8]
number = kod[-4:]
reverse_num = number[::-1]

print('категория:', category)
print('год:', year)
print('номер', number)
print('обратный номер', reverse_num)
