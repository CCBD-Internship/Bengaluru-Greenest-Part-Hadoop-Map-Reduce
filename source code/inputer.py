import cv2
import numpy as np
import json

js = open("maps.json", 'r')
f = open("input.txt", 'w')

d = json.loads(js.read())
for i in d:
    for j in d[i]:
        print(i, str(j[1]), str(j[0]), sep='-', file=f)

js.close()
f.close()
