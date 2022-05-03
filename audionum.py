from scipy.io.wavfile import read
import numpy as np

arr = read('FILENAME')
arr = np.array(arr[1],dtype=float)

print('writing...')

id = 0
l = open("left.txt", "w")
r = open("right.txt", "w")
for i in arr:
    l.write(str(arr[id][0]))
    r.write(str(arr[id][1]))
    l.write('\n')
    r.write('\n')
    id+=1
    if id%8000 == 0:
        print("+1s")

print(arr)
l.close()
r.close()
