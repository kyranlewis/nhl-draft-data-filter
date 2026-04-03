#Student Name: Kyran    
#Program Title: PROG1700-Logic And Programming
#Description: Final Project Module Script

import csv

fileName = 'nhldraft.csv'
readMode = 'r'
writeMode = 'w'

def retrieveNationPlayers(param):
    with open(fileName,readMode) as myCSVReader:
        csvData = csv.reader(myCSVReader)
        list = []
        c = 0
        lw = 0
        rw = 0
        d = 0
        g = 0
        for row in csvData:
            if row[5].upper() == param.upper():
                list.append([row[4],row[6],row[3],row[1],row[2]])
                if row[6] == 'C':
                    c += 1
                elif row[6] == 'LW':
                    lw += 1
                elif row[6] == 'RW':
                    rw += 1
                elif row[6] == 'D':
                    d += 1
                elif row[6] == 'G':
                    g += 1

        return list,c,lw,rw,d,g   
    
def retrievePositionPlayers(param):
    with open(fileName,readMode) as myCSVReader:
        csvData = csv.reader(myCSVReader)
        list = []
        for row in csvData:
            if row[6].upper() == param.upper():
                list.append([row[4],row[3],row[5],row[1],row[2]])

        return list 
    
def retrieveYearPlayers(param):
    with open(fileName,readMode) as myCSVReader:
        csvData = csv.reader(myCSVReader)
        list = []
        c = 0
        lw = 0
        rw = 0
        d = 0
        g = 0
        for row in csvData:
            if row[1] == str(param):
                list.append([row[4],row[6],row[5],row[3],row[2]])
                if row[6] == 'C':
                    c += 1
                elif row[6] == 'LW':
                    lw += 1
                elif row[6] == 'RW':
                    rw += 1
                elif row[6] == 'D':
                    d += 1
                elif row[6] == 'G':
                    g += 1

        return list,c,lw,rw,d,g
    
def retrieveTeamPlayers(param):
    with open(fileName,readMode) as myCSVReader:
        csvData = csv.reader(myCSVReader)
        list = []
        c = 0
        lw = 0
        rw = 0
        d = 0
        g = 0
        for row in csvData:
            if row[3] == param:
                list.append([row[4],row[5],row[6],row[1],row[2]])
                if row[6] == 'C':
                    c += 1
                elif row[6] == 'LW':
                    lw += 1
                elif row[6] == 'RW':
                    rw += 1
                elif row[6] == 'D':
                    d += 1
                elif row[6] == 'G':
                    g += 1

        return list,c,lw,rw,d,g

def getTeams():
    with open(fileName,readMode) as myCSVReader:
        csvData = csv.reader(myCSVReader)
        dataList = []
        for row in csvData:
            dataList.append(row)
        list = []


        for i in range(len(dataList)):
            if not (i == 0 or dataList[i][3] == ''):
                if not dataList[i][3] in list:
                    list.append(dataList[i][3])

        return list

def saveData(fileName,dataSet,option):
    accessMode = "w"

    newFile = open(fileName,accessMode)

    if option == 'a':
        newFile.write('PLAYER NAME,POSITION,TEAM,YEAR,DRAFT PICK\n')
    elif option == 'b':
        newFile.write('PLAYER NAME,TEAM,NATIONALITY,YEAR,DRAFT PICK\n')
    elif option == 'c':
        newFile.write('PLAYER NAME,POSITION,NATIONALITY,TEAM,DRAFT PICK\n')
    elif option == 'd':
        newFile.write('PLAYER NAME,NATIONALITY,POSITION,YEAR,DRAFT PICK\n')

    for row in dataSet:
        newFile.write(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}\n")

    newFile.close()


    
    
    