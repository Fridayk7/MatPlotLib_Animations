import matplotlib.pyplot as plt
import random
fig, ax=plt.subplots()

def bubbleSort(arr):
    plt.bar(x, arr, label="MyBar", color='blue')
    n= len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                plt.clf()
                plt.bar(x, arr, label="MyBar", color='blue')
                plt.bar(x,arr)[j+1].set_color('g')
                plt.pause(0.00001)
    bar = plt.bar(x,arr)
    for i in bar:
        i.set_color('g')
        plt.pause(0.01)
    print(arr)
    plt.show()


x = [i for i in range(1,51)]
y = [i for i in range(1,51)]
random.shuffle(y)

bubbleSort(y)
