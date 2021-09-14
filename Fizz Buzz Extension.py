# A script to run Fizz Buzz with user input
i = 0
while i != 'quit':
    i = input('Enter the number that you would like to be FizzBuzzed or type \'quit\': ')
    if i != 'quit':         # not very clean but does prevent an error message when typing 'quit' (seems to continue
                            # running loop even after condition has been met?)
        i = int(i)

        Flag_3 = 'n'
        Flag_5 = 'n'
        Flag_7 = 'n'
        Flag_11 = 'n'
        Flag_13 = 'n'
        Flag_17 = 'n'

        Flag_3 = input('Would you like to implement the rule on 3\'s? (y/n): ')
        Flag_5 = input('Would you like to implement the rule on 5\'s? (y/n): ')
        Flag_7 = input('Would you like to implement the rule on 7\'s? (y/n): ')
        Flag_11 = input('Would you like to implement the rule on 11\'s? (y/n): ')
        Flag_13 = input('Would you like to implement the rule on 13\'s? (y/n): ')
        Flag_17 = input('Would you like to implement the rule on 17\'s? (y/n): ')

        Statement = ''
        if i % 3 == 0 and Flag_3 == 'y':
            Statement += 'Fizz'
        if i % 5 == 0 and Flag_5 == 'y':
            Statement += 'Buzz'
        if i % 7 == 0 and Flag_7 == 'y':
            Statement += 'Bang'
        if i % 11 == 0 and Flag_11 == 'y':
            Statement = 'Bong'
        if i % 13 == 0 and Flag_13 == 'y':
            if Statement == '':
                Statement = 'Fezz'
            else:
                Statement_Length = len(Statement)
                String_Index = Statement.find('B', 0, Statement_Length)  # find index of position of first 'B'
                Statement_Start = str(Statement[0:String_Index])  # split string and insert 'Fezz' before the first B
                Statement_End = str(Statement[String_Index:Statement_Length])
                Statement = Statement_Start + 'Fezz' + Statement_End
        if i % 17 == 0 and Flag_17 == 'y':
            if Statement != '':
                Statement_Length = len(Statement)
                No_Words = int(Statement_Length / 4)  # find length of additions (multiple of 4)
                # split into strings of 4 and rearrange in reverse order
                New_Statement = ''
                for j in range(1, No_Words + 1):
                    Index_End = int(Statement_Length-((j-1)*4))
                    Index_Start = int(Index_End - 4)
                    New_Statement += str(Statement[Index_Start:Index_End])
                Statement = New_Statement
        if Statement == '':
            print(i)            # print just the number if no rules have been applied
        else:
            print(Statement)    # print the string of words as per the rules