# read the number of rounds by a judge

import csv, os, datetime #argparse


'''parser = argparse.ArgumentParser(description="Identify source folder and folder with full names")
parser.add_argument("-s", "--source", type=str, 
                   help="Folder with raw, downloaded csv files to analyze")

sourceFolderName = args.source
'''

outputFile = open('output.csv', 'w', newline='')
outputWrite = csv.writer(outputFile)
outputWrite.writerow(['Name','Energy Aff', 'Energy Neg', 'War Powers Aff', 'War Powers Neg',  'Legalization Aff', 'Legalization Neg', 'Military Presence Aff', 'Military Presence Neg', 'Emissions Aff', 'Emissions Neg', 'National Health Insurance Aff', 'National Health Insurance Neg', 'Executive Authority Aff', 'Executive Authority Neg', 'Total Aff', 'Total Neg'])

energy = datetime.datetime(2012,9,1)
warPowers = datetime.datetime(2013,9,1)
legalization = datetime.datetime(2014,9,1)
milWithdrawl = datetime.datetime(2015,9,1)
emissions = datetime.datetime(2016,9,1)
insurance = datetime.datetime(2017,9,1)
execAuthority = datetime.datetime(2018,9,1)



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
    affCount = 0
    negCount = 0
    energyAffCount = 0
    energyNegCount = 0
    warAffCount = 0
    warNegCount = 0
    legalizationAffCount = 0
    legalizationNegCount = 0
    milWithdrawAffCount = 0
    milWithdrawNegCount = 0
    emissionsAffCount = 0
    emissionsNegCount = 0
    insuranceAffCount = 0
    insuranceNegCount = 0
    authorityAffCount = 0
    authorityNegCount = 0
    for row in recordlist:
      checkTime = datetime.datetime.strptime(row[1], "%m/%d/%Y")
      if checkTime < warPowers:
        if row[6].startswith('AFF'):
          affCount += 1
          energyAffCount += 1
        elif row[6].startswith('NEG'):
          energyNegCount += 1
          negCount += 1
        else:
          print("ERROR! " + row[1])
      elif (checkTime > warPowers) and (checkTime < legalization):
        if row[6].startswith('AFF'):
          affCount += 1
          warAffCount += 1
        elif row[6].startswith('NEG'):
          warNegCount += 1
          negCount += 1
        else:
          print("ERROR! " + row[1])
      elif (checkTime > legalization) and (checkTime < milWithdrawl):
        if row[6].startswith('AFF'):
          affCount += 1
          legalizationAffCount += 1
        elif row[6].startswith('NEG'):
          legalizationNegCount += 1
          negCount += 1
        else:
          print("ERROR! " + row[1])
      elif (checkTime > milWithdrawl) and (checkTime < emissions):
        if row[6].startswith('AFF'):
          affCount += 1
          milWithdrawAffCount += 1
        elif row[6].startswith('NEG'):
          milWithdrawNegCount += 1
          negCount += 1
        else:
          print("ERROR! " + row[1])
      elif (checkTime > emissions) and (checkTime < insurance):
        if row[6].startswith('AFF'):
          affCount += 1
          emissionsAffCount += 1
        elif row[6].startswith('NEG'):
          emissionsNegCount += 1
          negCount += 1
        else:
          print("ERROR! " + row[1])
      elif (checkTime > insurance) and (checkTime < execAuthority):
        if row[6].startswith('AFF'):
          affCount += 1
          insuranceAffCount += 1
        elif row[6].startswith('NEG'):
          insuranceNegCount += 1
          negCount += 1
        else:
          print("ERROR! " + row[1])
      elif (checkTime > execAuthority):
        if row[6].startswith('AFF'):
          authorityAffCount += 1
          energyAffCount += 1
        elif row[6].startswith('NEG'):
          authorityNegCount += 1
          negCount += 1
        else:
          print("ERROR! " + row[1])
      else:
        print('ERROR!   ' + row[1])

    outputWrite.writerow([recordEntry, energyAffCount, energyNegCount, warAffCount, warNegCount, legalizationAffCount, legalizationNegCount, milWithdrawAffCount, milWithdrawNegCount, emissionsAffCount, emissionsNegCount, insuranceAffCount, insuranceNegCount, authorityAffCount, authorityNegCount, affCount, negCount])

outputFile.close()
