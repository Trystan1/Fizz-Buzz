# A script to run Fizz Buzz
for i in range(1, 1786):
    Statement = ''
    if i % 3 == 0:
        Statement += 'Fizz'
    if i % 5 == 0:
        Statement += 'Buzz'
    if i % 7 == 0:
        Statement += 'Bang'
    if i % 11 == 0:
        Statement = 'Bong'
    if i % 13 == 0:
        if Statement == '':
            Statement = 'Fezz'
        else:
            Statement_Length = len(Statement)
            String_Index = Statement.find('B', 0, Statement_Length)  # find index of position of first 'B'
            Statement_Start = str(Statement[0:String_Index])  # split string and insert 'Fezz' before the first B
            Statement_End = str(Statement[String_Index:Statement_Length])
            Statement = Statement_Start + 'Fezz' + Statement_End
    if i % 17 == 0:
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

# This works fine but could be shortened by using lists rather than manually appending to a long string
# Statement = [] # is how you make an empty list
# then Statement.append('string')
# Statement.clear() # to empty the list for 11
# Statement.reverse() # as a much easier version of 17
# 13 actually doesn't get much shorter though