num1 = []
num2 = []
result = 'False'
for i in range(3):
  n = int(input('num1 : ))
  num1.append(n)
for i in range(3):
  n = int(input('num2 : '))
  num2.append(n)
target = int(input())
for i in range(0, 3):
  for j in range(0, 3):
    if num1[i] + num2[j] == target:
      result = 'True'
      break
print(result)
