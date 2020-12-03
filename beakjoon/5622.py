#5622

import sys

alphabet = input()
num_word = ['','','ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']


time = len(alphabet)

for i in alphabet:
    for j in range(len(num_word)):
        if i in num_word[j]:
            time += j

print(time)