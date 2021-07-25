import csv
import os
from pathlib import Path


def Barracuda(path, deviceName):
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
                blockId = row[6]
                row[6] = getBlockId(blockId)
                row.append('\n')
                csvBody.append(row)
        index += 1
    f.close()
    csvHead.insert(6, 'blockId')
    csvResult.append(csvHead)
    for row in csvBody:
        csvResult.append(row)
    Path("result/" + deviceName + '/').mkdir(parents=True, exist_ok=True)
    with open('result/' + deviceName + '/' + fileName + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=',')
        writer.writerows(csvResult)
    print(fileName + '.csv done')


def Ceres(path, deviceName):
    f = open(path, 'r')

    fileName = ''
    index = ''
    csvHead = []
    csvBody = []
    csvResult = []

    for line in f.readlines():
        row = line.split(',')
        if line.startswith('File') | line.startswith('\n'):
            continue
        if line.startswith('LOTID'):
            fileName = line.split(':')[1].strip()
            index = fileName.split('_')[0]
        if line.startswith('Device'):
            csvHead = row
        if line.startswith(index):
            blockId = row[7]
            row[7] = getBlockId(blockId)
            row.append('\n')
            csvBody.append(row)
    f.close()
    csvHead.insert(5, ' ')
    csvHead.insert(7, 'blockId')
    csvHead.insert(8, 'NumBer of Block')
    csvHead.insert(9, 'Block Size')
    csvResult.append(csvHead)
    for row in csvBody:
        csvResult.append(row)
    Path("result/" + deviceName + '/').mkdir(parents=True, exist_ok=True)
    with open('result/' + deviceName + '/' + fileName + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=',')
        writer.writerows(csvResult)
    print(fileName + '.csv done')


def EOS(path, deviceName):
    f = open(path, 'r')

    fileName = ''
    index = ''
    csvHead = []
    csvBody = []
    csvResult = []

    for line in f.readlines():
        row = line.split(',')
        if line.startswith('File') | line.startswith('\n'):
            continue
        if line.startswith('LOTID'):
            fileName = line.split(':')[1].strip()
            index = fileName.split('_')[0]
        if line.startswith('Device'):
            csvHead = row
        if line.startswith(index):
            blockId = row[7]
            row[7] = getBlockId(blockId)
            row.append('\n')
            csvBody.append(row)
    f.close()
    csvHead.insert(5, ' ')
    csvHead.insert(7, 'blockId')
    csvHead.insert(8, 'NumBer of Block')
    csvHead.insert(9, 'Block Size')
    csvResult.append(csvHead)
    for row in csvBody:
        csvResult.append(row)
    Path("result/" + deviceName + '/').mkdir(parents=True, exist_ok=True)
    with open('result/' + deviceName + '/' + fileName + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=',')
        writer.writerows(csvResult)
    print(fileName + '.csv done')


def getBlockId(blockId):
    result = blockId
    if blockId.__eq__('8411'):
        result = 'ResultTX_8411_Temperature_Tj'
    if blockId.__eq__('8412'):
        result = 'ResultTX_8412_Temperature_Tj'
    if blockId.__eq__('8413'):
        result = 'ResultTX_8413_Temperature_Tj'
    if blockId.__eq__('8414'):
        result = 'ResultTX_8414_Temperature_Tj'
    if blockId == '8015':
        result = 'ResultStatus_Error_Code'
    if blockId == '2016':
        result = 'Result_Voltage_Current'
    if blockId == '1010100':
        result = 'BinResult'
    if blockId == '1111111':
        result = 'PSVoltageResult'
    if blockId == '1212121':
        result = 'PSCurrentResult'
    if blockId == '1313130':
        result = 'TJResult'
    if blockId == '1414140':
        result = 'RSSIResult'
    if blockId == '1515150':
        result = 'VDDPAResult'
    if blockId == '1616160':
        result = 'VDDCResult'
    if blockId == '1717170':
        result = 'VDDAResult'
    if blockId == '1818180':
        result = 'VREFResult'
    if blockId == '1919190':
        result = 'DieId'
    return result


if __name__ == '__main__':
    for dirPath, dirNames, fileNames in os.walk("data/"):

        for file in fileNames:
            os.path.join(dirPath, file)
            if file.endswith('.log'):
                device = dirPath.split('/')[1]
                if device == 'Barracuda':
                    print('start converting Barracuda : ' + str(file) + '')
                    Barracuda('data/' + device + '/' + file, device)
                if device == 'Ceres':
                    print('start converting Ceres : ' + str(file) + '')
                    Ceres('data/' + device + '/' + file, device)
                if device == 'EOS':
                    print('start converting EOS : ' + str(file) + '')
                    EOS('data/' + device + '/' + file, device)
                if device == 'Vulcan':
                    print('start converting Vulcan : ' + str(file) + '')
                    EOS('data/' + device + '/' + file, device)
