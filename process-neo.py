import os

print("hello world")

FILENAME='neodata-oct24-2022.csv'

count=0
line=''
f = open(FILENAME, 'r')
while True:
  count += 1
  line = f.readline()
  print(line)
  if not line:
    break

print('Total number of lines:', count)
