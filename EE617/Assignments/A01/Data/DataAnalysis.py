import numpy as np
from os import listdir
from os.path import isfile, join
from matplotlib import pyplot as plt
directory = '.\Readings_Set_02\\'
realG = 9.78068

def fileListGen(dir):
    fileList = []
    for file in listdir(dir):
        if isfile(join(dir, file)) and file.endswith('.txt'):
            fileList.append(file)
    return fileList

def fileRead(file):
    with open(directory + file) as f:
        content = f.readlines()
    content = content[4:]        # Remove description
    content = content[200:1000]  # Remove corrupted data
    length = len(content)
    
    t, x, y, z, r, h, p = ([] for i in range(7))
    for i in range(length):
        iter = 0
        data = []
        temp = ''
        for iter in content[i]:
            if iter == ',':
                data.append(temp)
                temp = ''
            else:
                temp += iter
        t.append(float(data[0]))    # Time (s)
        z.append(float(data[3]))    # Z (m/s^2)
        # x.append(data[1])  # X (m/s^2)
        # y.append(data[2])  # Y (m/s^2)
        # r.append(data[4])  # R (m/s^2)
        # h.append(data[5])  # Theta (deg)
        # p.append(data[6])  # Phi (deg)
    return t, z


files = fileListGen(directory)
# print(files)
T, Z, Means, StdDev = ([] for i in range(4))
for file in files:
    # print(file[39:])
    t, z = fileRead(file)
    T.append(t)
    Z.append(z)
    Means.append(np.mean(z))
    StdDev.append(np.std(z))
    # plt.plot(t, z)
    # plt.show()

## Display means and standard deviations in report format
# for i in range(10):
    # print("\t\t" + str(i+1) + " & " + str(round(Means[i],5)) + " & " + str(round(StdDev[i],5)) + " & " + str(i+11) + " & " + str(round(Means[i+10],5)) + " & " + str(round(StdDev[i+10],5)) + " & " + str(i+21) + " & " + str(round(Means[i+20],5)) + " & " + str(round(StdDev[i+20],5)) + " \\\\")

print("For all values:")
print("Mean = " + str(np.mean(Means)) + "; Standard Deviation = " + str(np.std(Means)) + "; Offset = " + str(np.mean(Means)-realG))
print()
print("Excluding possibly erroneous values:")
CorrectedMeans = [Means[i] for i in range(len(Means)) if i != 19]
print("Mean = " + str(np.mean(CorrectedMeans)) + "; Standard Deviation = " + str(np.std(CorrectedMeans)) + "; Offset = " + str(np.mean(CorrectedMeans)-realG))
plt.hist(Means)
plt.show()
plt.hist(CorrectedMeans)
plt.show()
