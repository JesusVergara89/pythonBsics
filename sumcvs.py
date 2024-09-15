import csv

def read_csv(path):
   with open(path, 'r') as file:
      reader = csv.reader(file, delimiter=',')
      sum_ = []
      for row in reader:
         sum_.append(int(row[1]))
      return sum(sum_)


response = read_csv('./dt.csv')
print(response)
