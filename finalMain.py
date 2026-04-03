#Student Name: Kyran    
#Program Title: PROG1700-Logic And Programming
#Description: Final Project

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    import csv
    import finalModule as mod
    
    print('\n\nWelcome to the NHL Draft Database!')

    print('\n-----------------------------------\n')

    while True:
        print('What would you like to know?')
        print('a) Nationalities')
        print('b) Positions')
        print('c) Draft Years')
        print('d) Teams')
        choice = None

        filteredData = []

        while choice == None:
            decision = input('Please select an option. (type done to exit): ')          

            if decision.lower() == 'a':
                choice = 'a'

                print('\nWhen choosing a nation, please input the two-letter abbreviation for the country')
                print('Example: CA = Canada, US = United States, SE = Sweden\n')

                countryInputted = None

                while countryInputted == None:
                    country = input('Please input the nation: ')

                    if len(country) == 2:
                        countryInputted = country.upper()

                        dataList,c,lw,rw,d,g = mod.retrieveNationPlayers(countryInputted)

                        if len(dataList) == 0:
                            print('No data on this country was found. Please select another country.')
                            countryInputted = None
                        else:
                            
                            print('\nRetrieving Data\n')
                            print('PLAYER NAME, POSITION, TEAM, YEAR, DRAFT PICK')
                            print('-----------------------------------------------------')
                            for row in dataList:
                                print((f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, Pick {row[4]}'))
                            print(f'\nTotal Players: {len(dataList)}')
                            print(f'Centers: {c}')
                            print(f'Left Wings: {lw}')
                            print(f'Right Wings: {rw}')
                            print(f'Defenders: {d}')
                            print(f'Goalies: {g}')
                            filteredData = dataList
                    else:
                        print("Please input a country's two-letter abbreviation.")
                        countryInputted = None
            elif decision.lower() == 'b':
                choice = 'b'

                positions = ['C', 'LW', 'RW', 'D', 'G']

                print('\nPlease choose from the 5 main positions (C,LW,RW,D,G)')

                posInputted = None

                while posInputted == None:
                    position = input('Please input a position: ')

                    for i in range(len(positions)):
                        if positions[i].upper() == position.upper():
                            posInputted = positions[i]

                    if posInputted != None:
                        dataList = mod.retrievePositionPlayers(posInputted)
                            
                        print('\nRetrieving Data\n')

                        print('PLAYER NAME, TEAM, NATIONALITY, YEAR, DRAFT PICK')
                        for row in dataList:
                            print((f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, Pick {row[4]}'))
                        print(f'\nTotal Players: {len(dataList)}')
                        filteredData = dataList
                    else:
                        print('Please input a valid position.')
            elif decision.lower() == 'c':
                choice = 'b'

                print('\nPlease select a year to view.')

                yearInputted = None

                while yearInputted == None:
                    year = None

                    
                    while year == None:
                        yearString = input('Please input a year: ')

                        try:
                            year = int(yearString)
                        except ValueError:
                            print('Please input a valid year.')
                        

                    if year > 0:
                        yearInputted = year

                        dataList,c,lw,rw,d,g = mod.retrieveYearPlayers(year)
                            
                        print('\nRetrieving Data\n')

                        if len(dataList) > 0:

                            print('PLAYER NAME, POSITION, NATIONALITY, TEAM, DRAFT PICK')
                            print('-----------------------------------------------------')
                            for row in dataList:
                                print((f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, Pick {row[4]}'))
                            filteredData = dataList
                            print(f'\nTotal Players: {len(dataList)}')
                            print(f'Centers: {c}')
                            print(f'Left Wings: {lw}')
                            print(f'Right Wings: {rw}')
                            print(f'Defenders: {d}')
                            print(f'Goalies: {g}')
                        else:
                            print('No data entries for this year. Please reinput a valid year.')
                            yearInputted = None                     
                    else:
                        print('Please input a valid year.')
            elif decision.lower() == 'd':
                choice = 'd'

                teams = mod.getTeams()
                
                print('\n--- TEAM IDS ---')
                for i in range(len(teams)):
                    print(f'{i+1}) {teams[i]}')
                
                teamChoice = None
                print('')
                while teamChoice == None:
                    team = None

                    while team == None:
                        teamString = input('Please input an ID: ')

                        try:
                            team = int(teamString)
                        except ValueError:
                            print('Please input a valid ID.')

                    if team > 0 and team <= len(teams):
                        teamChoice = team

                        teamName = teams[teamChoice-1]

                        dataList,c,lw,rw,d,g = mod.retrieveTeamPlayers(teamName)
                            
                        print('\nRetrieving Data\n')

                        if len(dataList) > 0:

                            print('PLAYER NAME, NATIONALITY, POSITION, YEAR, DRAFT PICK')
                            print('-----------------------------------------------------')
                            for row in dataList:
                                print((f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, Pick {row[4]}'))
                            print(f'\nTotal Players: {len(dataList)}')
                            print(f'Centers: {c}')
                            print(f'Left Wings: {lw}')
                            print(f'Right Wings: {rw}')
                            print(f'Defenders: {d}')
                            print(f'Goalies: {g}')
                            filteredData = dataList
                        else:
                            print('No data entries for this team. Please reinput a valid team.')
                            yearInputted = None                     
                    else:
                        print('Please input a valid ID.')
            elif decision.lower() == 'done':

                print('\nClosing program now.\n\n')
                return
            else: 
                print('Please choose a proper option.')
                choice == None

        saveChosen = None
 
        print('\n-----------------------------------\n')

        while saveChosen == None:
            saveOption = input('Would you like to save your filtered data? (Y/N): ')

            if saveOption.lower() == 'y':
                saveChosen = 'y'
                fileNameInput = input('Please input the name of your file: ')

                fileName = (f'{fileNameInput}.csv')

                print('Saving..')
                mod.saveData(fileName,filteredData,choice)
                print('Save complete!')
            elif saveOption.lower() == 'n':
                break
            else:
                print('Please choose a proper option.')
 
        print('\n-----------------------------------\n')

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()