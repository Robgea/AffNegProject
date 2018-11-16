# read the number of rounds by a judge

import csv, os, datetime #argparse


'''parser = argparse.ArgumentParser(description="Identify source folder and folder with full names")
parser.add_argument("-s", "--source", type=str, 
                   help="Folder with raw, downloaded csv files to analyze")

sourceFolderName = args.source
'''

outputFile = open('output.csv', 'w', newline='')
outputWrite = csv.writer(outputFile)
outputWrite.writerow(['Name','Transport Aff', 'Transport Neg', 'Latin America Aff', 'Latin America Neg',  'Oceans Aff', 'Oceans Neg', 'Surveillance Aff', 'Surveillance Neg', 'China Aff', 'China Neg', 'Education Aff', 'Education Neg', 'Immigration Aff', 'Immigration Neg', 'Total Aff', 'Total Neg'])

transport = datetime.datetime(2012,9,1)
latinAm = datetime.datetime(2013,9,1)
oceans = datetime.datetime(2014,9,1)
surveillance = datetime.datetime(2015,9,1)
china = datetime.datetime(2016,9,1)
education = datetime.datetime(2017,9,1)
immigration = datetime.datetime(2018,9,1)



for judgeRecord in os.listdir('.'):
  if not judgeRecord.endswith('.csv'):
    print('Skipping...' + judgeRecord)
    continue
  elif judgeRecord == 'output.csv':
    continue
  else:
    print("Counting judge record for..." + judgeRecord)
    csvFileObj = open(judgeRecord)
    recordReader = csv.reader(csvFileObj)
    recordEntry = judgeRecord[:-4]
    recordlist = list(recordReader)
    #recordlist.pop(0)
    affCount = 0
    negCount = 0
    transportAffCount = 0
    transportNegCount = 0
    LAAffCount = 0
    LANegCount = 0
    oceanAffCount = 0
    oceanNegCount = 0
    surveilAffCount = 0
    surveilNegCount = 0
    chinaAffCount = 0
    chinaNegCount = 0
    educAffCount = 0
    educNegCount = 0
    immAffCount = 0
    immNegCount = 0
    print("Number of rows: {}".format(len(recordlist)) )
    numRows = 0
    for row in recordlist:
      try:
        checkTime = datetime.datetime.strptime(row[1], "%m/%d/%Y")
      except:
        continue
      if (checkTime > transport) and (checkTime < latinAm):
        if row[6].startswith('AFF'):
          affCount += 1
          transportAffCount += 1
        elif row[6].startswith('NEG'):
          transportNegCount += 1
          negCount += 1
        else:
          print("ERROR in Transport! " + row[1])
      elif (checkTime > latinAm) and (checkTime < oceans):
        if row[6].startswith('AFF'):
          affCount += 1
          LAAffCount += 1
        elif row[6].startswith('NEG'):
          LANegCount += 1
          negCount += 1
        else:
          print("ERROR in Latin America! " + row[1])
      elif (checkTime > oceans) and (checkTime < surveillance):
        if row[6].startswith('AFF'):
          affCount += 1
          oceanAffCount += 1
        elif row[6].startswith('NEG'):
          oceanNegCount += 1
          negCount += 1
        else:
          print("ERROR in Oceans! " + row[1])
      elif (checkTime > surveillance) and (checkTime < china):
        if row[6].startswith('AFF'):
          affCount += 1
          surveilAffCount += 1
        elif row[6].startswith('NEG'):
          surveilNegCount += 1
          negCount += 1
        else:
          print("ERROR in Surveillance! " + row[1])
      elif (checkTime > china) and (checkTime < education):
        if row[6].startswith('AFF'):
          affCount += 1
          chinaAffCount += 1
        elif row[6].startswith('NEG'):
          chinaNegCount += 1
          negCount += 1
        else:
          print("ERROR in CHINA!" + row[1])
      elif (checkTime > education) and (checkTime < immigration):
        if row[6].startswith('AFF'):
          affCount += 1
          educAffCount += 1
        elif row[6].startswith('NEG'):
          educNegCount += 1
          negCount += 1
        else:
          print("ERROR in Education! " + row[1])
      elif (checkTime > immigration):
        if row[6].startswith('AFF'):
          immAffCount += 1
          affCount += 1
        elif row[6].startswith('NEG'):
          immNegCount += 1
          negCount += 1
        else:
          print("ERROR in Immigration! " + row[1])
      else:
        print('ERROR! Everything is a disaster!' + row[1])


    outputWrite.writerow([recordEntry, transportAffCount, transportNegCount, LAAffCount, LANegCount, oceanAffCount, oceanNegCount, surveilAffCount, surveilNegCount, chinaAffCount, chinaNegCount, educAffCount, educNegCount, immAffCount, immNegCount, affCount, negCount])

outputFile.close()
