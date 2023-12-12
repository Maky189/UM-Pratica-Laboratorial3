file1 = open("texto.txt", 'r')

alpha = {'a': 0, 'e':0, 'i':0, 'o':0, 'u':0}

for linha in file1:
    for char in linha:
        if char in alpha:
            alpha[char] += 1

print(alpha)