# import pandas as pd
# from matplotlib import pyplot as plt

# x =[1,2,3]
# y =[1,4,9]

# plt.plot(x,y)
# plt.title('test plot')
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

from cardiovascular.heart import Heart
import time   

ht = Heart(heart_rate=75, stroke_volume=70)

for i in range(20):
    ht.pump()
    time.sleep(3)

