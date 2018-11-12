# read the number of rounds by a judge

import csv, os,datetime #argparse

'''parser = argparse.ArgumentParser(description="Identify source folder and folder with full names")
parser.add_argument("-s", "--source", type=str, 
                   help="Folder with raw, downloaded csv files to analyze")

sourceFolderName = args.source
'''

outputFile = open('output.csv', 'w', newline='')
outputWrite = csv.writer(outputFile)
outputWrite.writerow(['Name','Rounds Judged', 'Aff Ballots', 'Neg Ballots'])


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
    affCount = 0
    negCount = 0
    recordlist = list(recordReader)
    for row in recordlist:
      if row[6].startswith('AFF'):
        affCount += 1
      elif row[6].startswith('NEG'):
        negCount += 1
      else:
        continue
    judgeVote = negCount + affCount
    outputWrite.writerow([recordEntry, judgeVote, affCount, negCount])

outputFile.close()
