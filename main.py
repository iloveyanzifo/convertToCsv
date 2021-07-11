import csv
import os


def Barracuda(path):
    f = open(path, 'r')

    fileName = ''
    index = 1
    csvHead = []
    csvBody = []
    csvResult = []
    for line in f.readlines():
        row = line.split(',')[0:-1]
        if line.startswith('LOTID'):
            fileName = line.split(':')[1].strip()
        if line.startswith('Device'):
            csvHead = row
        else:
            if index >= 10 & len(row) > 1:
                csvBody.append(row)
        index += 1
    f.close()
    csvResult.append(csvHead)
    for row in csvBody:
        csvResult.append(row)
    with open('result/' + fileName + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=',')
        writer.writerows(csvResult)


if __name__ == '__main__':
    rawDataList = os.listdir('data/Barracuda')
    for target in rawDataList:
        if target.endswith('.log'):
            Barracuda('data/Barracuda/' + str(target))
