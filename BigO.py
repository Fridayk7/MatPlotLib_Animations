import matplotlib.pyplot as plt
import math
import numpy

x = [i for i in numpy.arange(1,10,0.1)]
Ologn= [math.log2(i) for i in numpy.arange(1,10,0.1)]
On = [i for i in numpy.arange(1,10,0.1)]
Onlogn=[i*math.log2(i)for i in numpy.arange(1,10,0.1)]
On2 = [i**2 for i in numpy.arange(1,10,0.1)]
O2n = [2**i for i in numpy.arange(1,10,0.1)]
Ofactn = [math.gamma(i)for i in numpy.arange(1,10,0.1) ]

plt.plot(x[0],Ologn[0],'c',label='Log(N)')
plt.plot(x[0], On[0],'b', label="N")
plt.plot(x[0], Onlogn[0],'g', label="N*Log(N)")
plt.plot(x[0], On2[0],'y',label="N^2")
plt.plot(x[0], O2n[0],'k', label="2^N")
plt.plot(x[0], Ofactn[0],'r', label="N!")
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Big O ")
plt.legend()

for i in range(1,52):
    plt.plot([],[])
    plt.plot(x[i], Ologn[i],'co')
    plt.plot(x[i], On[i],'bo')
    plt.plot(x[i], Onlogn[i],'go')
    plt.plot(x[i], On2[i],'yo')
    plt.plot(x[i], O2n[i],'ko')
    plt.plot(x[i], Ofactn[i],'ro')
    plt.pause(0.0001)
plt.show()