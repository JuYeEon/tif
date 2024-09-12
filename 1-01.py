num1 = []
num2 = []
result = 'False'
for i in range(3):
  num1.append(int(input('num1 : )))
for i in range(3):
  num2.append(int(input('num2 : ')))
target = int(input('target : '))
for i in range(0, 3):
  for j in range(0, 3):
    if num1[i] + num2[j] == target:
      result = 'True'
      break
print(result)
