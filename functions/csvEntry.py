import csv

def createCSV(name):
    header = ['Method', 'Number of Inputs', 'Number of Outputs', 'Input Size', 'Output Size','Process Time','Target']
    with open(name, 'w', encoding='UTF8', newline='') as f:
       writer = csv.writer(f)
       writer.writerow(header)
    f.close()

def addLine(name, line):
    with open(name, 'a') as f:
       f.write(line)
       f.write("\n")
    f.close()