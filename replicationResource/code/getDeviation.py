```python
import xlrd
import numpy as np
from numpy import *
import xlsxwriter
import sys
import os
sys.dont_write_bytecode = True

formulaList = "The list of all invesitgated SBFL formulas"


programList = ['flex', 'grep', 'gzip', 'sed']

numberList = ['2bug', '3bug', '4bug', '5bug']

typeList = ['TypeA', 'TypeP', 'TypeH']


def calDeviation():
    commonPath = 'D:/file/allFolders/'
    for formulaName in formulaList:

        globals()[formulaName + '_over'] = 0
        globals()[formulaName + '_under'] = 0

        globals()[formulaName + '_Deviation_over'] = 0
        globals()[formulaName + '_Deviation_under'] = 0

        for programName in programList:
            for faultNumber in numberList:
                for typeName in typeList:
                    path = commonPath + programName + '/' + faultNumber + '/' + typeName
                    versionList = os.listdir(path)
                    versionList.sort()
                    totalDirs = []
                    for versionName in versionList:
                        if versionName[0] != 'M':
                            totalDirs.append(path + '/' + versionName + '/clusterAssment/')
                    for indi_dir in totalDirs:
                        resultList = os.listdir(indi_dir)
                        for resultName in resultList:
                            if formulaName in resultName:
                                if '(medoids_over)' in resultName or '(clusters_over)' in resultName:
                                    globals()[formulaName + '_over'] += 1

                                    file = open(indi_dir + resultName)
                                    data = int(file.readline())
                                    deviation = data - int(faultNumber[0])
                                    globals()[formulaName + '_Deviation_over'] += deviation

                                elif '(medoids_under)' in resultName or '(clusters_under)' in resultName:
                                    globals()[formulaName + '_under'] += 1

                                    file = open(indi_dir + resultName)
                                    data = int(file.readline())
                                    deviation = data - int(faultNumber[0])
                                    globals()[formulaName + '_Deviation_under'] += deviation


        print(formulaName + '_over: ' + str(globals()[formulaName + '_over']))
        print(formulaName + '_Deviation_over: ' + str(globals()[formulaName + '_Deviation_over']))

        print(formulaName + '_under: ' + str(globals()[formulaName + '_under']))
        print(formulaName + '_Deviation_under: ' + str(globals()[formulaName + '_Deviation_under']))

        print('\n')
```