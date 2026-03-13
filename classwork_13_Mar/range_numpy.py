import numpy as np
#creating arange array
array1=np.arange(200,600,10)
print("arange array of order (200,600,10) :")
print(array1)
print("------------------")
#creating eye array
array=np.eye(4)
print(array)

#to generate unit matrix of order 5 of int type
array2=np.eye(5,dtype=int)
print(array2)

'''output
arange array of order (200,600,10) :
[200 210 220 230 240 250 260 270 280 290 300 310 320 330 340 350 360 370
 380 390 400 410 420 430 440 450 460 470 480 490 500 510 520 530 540 550
 560 570 580 590]
------------------
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
[[1 0 0 0 0]
 [0 1 0 0 0]
 [0 0 1 0 0]
 [0 0 0 1 0]
 [0 0 0 0 1]]
'''