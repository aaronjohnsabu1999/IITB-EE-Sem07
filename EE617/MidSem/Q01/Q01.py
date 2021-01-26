# https://datatofish.com/read_excel/
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html
# https://stackoverflow.com/questions/18648626/for-loop-with-two-variables
import math
import numpy as np
import pandas as pd
import random
from matplotlib import pyplot as plt

data = {62.5: [], 100: [], 125: [], 200: [], 250: [], 300: [], 400: []}
df = pd.DataFrame(pd.read_excel('./Q1-midsem2020-EE617.xlsx'), columns = ['Pathogen concentration (pg/ml)','Sensor output (V)']).to_numpy()
for reading in df:
  data[reading[0]].append(round(reading[1], 6))

# https://realpython.com/iterate-through-dictionary-python/
sensitivities = []
for read1 in data:
  for read2 in data:
    if read1 < read2:
      sensitivities.extend([round(abs((i-j)/(read1-read2)), 10) for i in data[read1] for j in data[read2]])
print("Mean      = ", str(np.mean(sensitivities)))
print("Std Dev   = ", str(np.std(sensitivities)))
print("Max Value = ", str(np.max(sensitivities)))
print("Min Value = ", str(np.min(sensitivities)))

# https://realpython.com/python-histograms/
n, bins, patches = plt.hist(x = sensitivities, bins='auto', color='#BB0405')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Sensitivities')
plt.show()

# https://math.stackexchange.com/a/1847633/382882
# https://pynative.com/python-random-choice/
# https://stackoverflow.com/questions/21753841/factorial-in-numpy-and-scipy
# https://stackoverflow.com/questions/27946595/how-to-manage-division-of-huge-numbers-in-python
n = 1000000
r = 10
combos = []
for i in range(n):
  combos.append(np.mean(random.choices(sensitivities, k = 15*r)))
print("Mean               = ", str(np.mean(combos)))
print("Std Dev            = ", str(np.std(combos)))
print("Normed Std Dev     = ", str(np.std(combos)*math.sqrt(15*r)))
print("Max Computed Value = ", str(np.mean(combos)+5.5*np.std(combos)*math.sqrt(r)))

n, bins, patches = plt.hist(x = combos, bins='auto', color='#BB0405')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Average Sensitivities')
plt.show()