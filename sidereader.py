# read the number of rounds by a judge

import csv, os,  datetime #argparse

'''parser = argparse.ArgumentParser(description="Identify source folder and folder with full names")
parser.add_argument("-s", "--source", type=str, 
                   help="Folder with raw, downloaded csv files to analyze")

sourceFolderName = args.source
'''

outputFile = open('output.csv', 'w', newline='')
outputWrite = csv.writer(outputFile)
outputWrite.writerow(['Name','Energy', 'War Powers', 'Legalization', 'Military Presence', 'Emissions', 'National Health Insurance', 'Executive Authority'])

energy = datetime.date(2012,9,01)
warPowers = datetime.date(2013,9,01)
legalization = datetime.date(2014,9,01)
milWithdrawl = datetime.date(2015,9,01)
emissions = datetime.date(2016,9,01)
insurance = datetime.date(2017,9,01)
execAuthority = datetime.date(2018,9,01)



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
    energyCount = 0
    warCount = 0
    legalizationCount = 0
    milWithdrawCount = 0
    emissionsCount = 0
    insuranceCount = 0
    authorityCount = 0
    for row in recordlist:
      '''if row[6].startswith('AFF'):
        affCount += 1
      elif row[6].startswith('NEG'):
        negCount += 1
      else:
        continue
    judgeVote = negCount + affCount'''
    outputWrite.writerow([recordEntry, judgeVote, affCount, negCount])

outputFile.close()
