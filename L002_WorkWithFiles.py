# Лекция 2

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)  # разделителей не будет
data.close()
# redgreenblue / первый запуск, создан файл file.txt, добавлен список
# redgreenblueredgreenblue / второй запуск, дозаписывание, и так далее

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors)
data.close()
# redgreenblue / произошла перезапись, пересоздание файла

data = open('file.txt', 'a')
data.write('LINE 132\n')
data.write('LINE 133\n')
data.close()

with open('file.txt', 'a') as data:
    data.write('line 111\n')
    data.write('line 222\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
