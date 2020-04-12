import re
import numpy as np
from scipy.spatial.distance import cosine

file = open('sentences.txt', 'r')
data_list = file.readlines() # sentences
n = 0 # rows count
d = 0 # unique words count
my_dict = {} # dictionary for unique words
my_list = [] # all words separated

# matrix which shows the positions of all words in every sentence in my_dict
for line in data_list:
    low_sentence = line.lower()
    row = re.split('[^a-z]', low_sentence)
    row = list(filter(None, row)) # deletes empty lists
    for index in range(len(row)):
        my_list.append(row[index])
    n += 1


# unique words dictionary
for i in range(len(my_list)):
    if my_dict.get(my_list[i]) == None:
        my_dict[my_list[i]] = d
        d += 1


# matrix init zeros
matrix = np.ones((n, d))
for i in range(n):
    for j in range(d):
        matrix[i][j] = 0


# matrix filling
i = 0 # counter for words in a row
for line in data_list:
    low_sentence = line.lower()
    row = re.split('[^a-z]', low_sentence)
    row = list(filter(None, row))
    for word in row:
        entry_count = 0
        j = 0 # counter for keys in my_dict
        for key in my_dict:
            if key == word:
                entry_count += 1
                matrix[i][j] = entry_count
            j += 1
    i += 1


# show matrix
for row in matrix:
    print(' '.join(str(col) for col in row))

# show cosine between rows 0 and i
for i in range(len(matrix)):
     print("row " + str(i))
     print(cosine(matrix[0], matrix[i]))


# end of work
file.close()