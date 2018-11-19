# read the number of rounds by a judge

import csv, os, datetime #argparse


'''parser = argparse.ArgumentParser(description="Identify source folder and folder with full names")
parser.add_argument("-s", "--source", type=str, 
                   help="Folder with raw, downloaded csv files to analyze")

sourceFolderName = args.source
'''


#Creating the CSV
outputFile = open('output.csv', 'w', newline='')
outputWrite = csv.writer(outputFile)
outputWrite.writerow(['Name','Sep 12', 'Oct 12', 'Nov 12', 'Dec12',  'Jan13', 'Feb13', 'Mar13', 'Apr13 +', 'SepOct13', 'Nov13', 'Dec13', 'Jan14', 'Feb14', 'Mar14', 'Apr14+', 'SepOct14', 'Nov14', 'Dec14', 'Jan15', 'Feb15', 'Mar15', 'Apr15+', 'SepOct15', 'Nov15', 'Dec15', 'Jan16', 'Feb16', 'Mar16', 'Apr16+', 'SepOct16', 'Nov16', 'Dec16', 'Jan17', 'Feb17', 'Mar17', 'Apr17+', 'SepOct17', 'Nov17', 'Dec17', 'Jan18', 'Feb18', 'Mar18', 'Apr18+','SepOct18', 'Nov18' ])


#Datetimes to break things up
sep12 = datetime.datetime(2012,9,1)
oct12 = datetime.datetime(2012,10,1)
nov12 = datetime.datetime(2012,11,1)
dec12 = datetime.datetime(2012,12,1)
jan13 = datetime.datetime(2013,1,1)
feb13 = datetime.datetime(2013,2,1)
mar13 = datetime.datetime(2013,3,1)
apr13 = datetime.datetime(2013,4,1)
sepoct13 = datetime.datetime(2013,8,1)
nov13 = datetime.datetime(2013,11,1)
dec13 = datetime.datetime(2013,12,1)
jan14 = datetime.datetime(2014,1,1)
feb14 = datetime.datetime(2014,2,1)
mar14 = datetime.datetime(2014,3,1)
apr14 = datetime.datetime(2014,4,1)
sepoct14 = datetime.datetime(2014,8,1)
nov14 = datetime.datetime(2014,11,1)
dec14 = datetime.datetime(2014,12,1)
jan15 = datetime.datetime(2015,1,1)
feb15 = datetime.datetime(2015,2,1)
mar15 = datetime.datetime(2015,3,1)
apr15 = datetime.datetime(2015,4,1)
sepoct15 = datetime.datetime(2015,8,1)
nov15 = datetime.datetime(2015,11,1)
dec15 = datetime.datetime(2015,12,1)
jan16 = datetime.datetime(2016,1,1)
feb16 = datetime.datetime(2016,2,1)
mar16 = datetime.datetime(2016,3,1)
apr16 = datetime.datetime(2016,4,1)
sepoct16 = datetime.datetime(2016,8,1)
nov16 = datetime.datetime(2016,11,1)
dec16 = datetime.datetime(2016,12,1)
jan17 = datetime.datetime(2017,1,1)
feb17 = datetime.datetime(2017,2,1)
mar17 = datetime.datetime(2017,3,1)
apr17 = datetime.datetime(2017,4,1)
sepoct17 = datetime.datetime(2017,8,1)
nov17 = datetime.datetime(2017,11,1)
dec17 = datetime.datetime(2017,12,1)
jan18 = datetime.datetime(2018,1,1)
feb18 = datetime.datetime(2018,2,1)
mar18 = datetime.datetime(2018,3,1)
apr18 = datetime.datetime(2018,4,1)
sepoct18 = datetime.datetime(2018,8,1)
nov18 = datetime.datetime(2018,11,1)
dec18 = datetime.datetime(2018,12,1)


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
    # Aff Neg Tracking Variables
    affCount = 0
    negCount = 0
    sep12Aff = 0 
    oct12Aff = 0 
    nov12Aff = 0 
    dec12Aff = 0 
    jan13Aff = 0 
    feb13Aff = 0 
    mar13Aff = 0 
    apr13Aff = 0 
    sepoct13Aff = 0 
    nov13Aff = 0 
    dec13Aff = 0 
    jan14Aff = 0 
    feb14Aff = 0 
    mar14Aff = 0 
    apr14Aff = 0 
    sepoct14Aff = 0 
    nov14Aff = 0 
    dec14Aff = 0 
    jan15Aff = 0 
    feb15Aff = 0 
    mar15Aff = 0 
    apr15Aff = 0 
    sepoct15Aff = 0 
    nov15Aff = 0 
    dec15Aff = 0 
    jan16Aff = 0 
    feb16Aff = 0 
    mar16Aff = 0 
    apr16Aff = 0 
    sepoct16Aff = 0 
    nov16Aff = 0 
    dec16Aff = 0 
    jan17Aff = 0 
    feb17Aff = 0 
    mar17Aff = 0 
    apr17Aff = 0 
    sepoct17Aff = 0 
    nov17Aff = 0 
    dec17Aff = 0 
    jan18Aff = 0 
    feb18Aff = 0 
    mar18Aff = 0 
    apr18Aff = 0 
    sepoct18Aff = 0 
    nov18Aff = 0 
    dec18Aff = 0 
    sep12Neg = 0 
    oct12Neg = 0 
    nov12Neg = 0 
    dec12Neg = 0 
    jan13Neg = 0 
    feb13Neg = 0 
    mar13Neg = 0 
    apr13Neg = 0 
    sepoct13Neg = 0 
    nov13Neg = 0 
    dec13Neg = 0 
    jan14Neg = 0 
    feb14Neg = 0 
    mar14Neg = 0 
    apr14Neg = 0 
    sepoct14Neg = 0 
    nov14Neg = 0 
    dec14Neg = 0 
    jan15Neg = 0 
    feb15Neg = 0 
    mar15Neg = 0 
    apr15Neg = 0 
    sepoct15Neg = 0 
    nov15Neg = 0 
    dec15Neg = 0 
    jan16Neg = 0 
    feb16Neg = 0 
    mar16Neg = 0 
    apr16Neg = 0 
    sepoct16Neg = 0 
    nov16Neg = 0 
    dec16Neg = 0 
    jan17Neg = 0 
    feb17Neg = 0 
    mar17Neg = 0 
    apr17Neg = 0 
    sepoct17Neg = 0 
    nov17Neg = 0 
    dec17Neg = 0 
    jan18Neg = 0 
    feb18Neg = 0 
    mar18Neg = 0 
    apr18Neg = 0 
    sepoct18Neg = 0 
    nov18Neg = 0 
    dec18Neg = 0 
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
