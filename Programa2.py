file1 = open("ficheiro1.txt", "r")
file2 = open("ficheiro2.txt", "r")
array1 = []
array2 = []

for num in file1:
    array1.append(int(num.strip('\n')))
for num in file2:
    array2.append(int(num.strip('\n')))
    
lista = sorted(list(array1 + array2))

file3 = open("ficheiro3.txt", 'a')

for num in lista:
    file3.write(str(num) + '\n')
file3.close()

    
