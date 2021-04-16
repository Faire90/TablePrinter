
def printTable(listList):
#First part of the function determines the column widths and longest column.
#This is done by iterating through each list and checking the length of the
#list and width of the words.  The longest word in each list and longest list will be stored.
    colWidths = []
    longestColumn = 0

    for list in listList:
        widest = 0
        columnLength = len(list)
        if columnLength > longestColumn:
            longestColumn = columnLength
        for word in list:
            width = len(word)
            if width > widest:
                widest = width

        colWidths.append(widest)

#Next, the function iterates through the lists.  The range is based on the longest
#list to ensure it keeps going.
#The function checks if the given list has enough elements to print and if not,
#it will print a blank.
    for x in range(longestColumn):
        output = ''
        for y in range(len(listList)):
            if x < len(listList[y]):
                output += str(listList[y][x]).rjust((colWidths[y]+1))
            else:
                output += ''.rjust((colWidths[y] + 1))
        print(output)


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David', 'Brad'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)