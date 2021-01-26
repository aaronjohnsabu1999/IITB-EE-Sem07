import csv
import math
import numpy as np
from datetime import date
from matplotlib import pyplot as plt
from pandas.plotting import autocorrelation_plot

files = ['BSESN', 'INFY.BO', 'RELIANCE.BO', 'TATAMOTORS.BO', 'USD-INR']
data  = {}
for file in files:
  # https://docs.python.org/3/library/csv.html
  # https://evanhahn.com/python-skip-header-csv-reader/
  # https://docs.python.org/3/library/datetime.html
  with open(file + '.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(reader)
    first      = next(reader)
    initdate   = date.fromisoformat(first[0][0:10])
    value1     = float(first[0][10:].split(',')[1])
    data[file] = []
    for row in reader:
      diffdate = (date.fromisoformat(row[0][0:10]) - initdate).days
      LEN      = len(data[file])
      try:
        value2 = float(row[0][10:].split(',')[1])
      except:
        continue
      intermed = [value1 + (value2 - value1)*i/(diffdate - LEN) for i in range(diffdate - LEN)]
      for i in range(len(intermed)-1):
        data[file].append(abs(round(math.log(intermed[i+1])-math.log(intermed[i]), 6)))
        # data[file].append(round(math.log(intermed[i+1])-math.log(intermed[i]), 6))
        value1 = intermed[i+1]
      data[file].append(abs(math.log(value2) - math.log(value1)))
      # data[file].append(math.log(value2) - math.log(value1))
      value1   = value2

  print("Mean      = ", str(np.mean(data[file])))
  print("Std Dev   = ", str(np.std(data[file])))
  
  autocorrelation_plot(data[file])
  plt.title('Autocorrelation for ' + file)
  plt.show()