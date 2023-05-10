line = input('line: ')
line_2 = ''
for elements in line:
    if elements.isupper():
        line_2 += elements
print(line_2)
