'''

CSV file (Comma Separated Values file)
type of plain text file
CSV files use a comma to separate each specific data value.
the separator character is called a delimiter
Other popular delimiters include the tab (\t), colon (:) and semi-colon (;) characters.

 TEXT_FILE:(csv)
   column 1 name,column 2 name, column 3 name
   first row data 1,first row data 2,first row data 3
   second row data 1,second row data 2,second row data 3


 used:
 export data from spreadsheets and databases as well as import or use it in other programs.

The csv library contains objects and other code to read, write, and process data from and to CSV files.

advantage:
 Rather than deal with a list of individual String elements, you can read CSV data directly into a dictionary

'''


"""
Reading CSV Files With csv
"""

import csv

def function_to_read():

 with open(file='employee_birthday.txt', mode='r') as csv_file: #syntax

    # object of reader
    # object    = function (iterable, delimiter)
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    print(f'this is the o/p ={csv_reader}') # object
    # iterating object

    # next method

    # built in method used over an iterable remove the heading and skip to data part
    #next(csv_file)

    for row in csv_reader:
        # print(row) everything in reader is list
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')


function_to_read()