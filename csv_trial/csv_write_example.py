'''

You can also write to a CSV file using a writer object and the .write_row() method:
'''


import csv

def function_to_write():
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',')

        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# another method

def function_to_write_as_dictionary():
    with open('employee_file2.csv', mode='w') as csv_file:
        fieldnames = ['emp_name', 'dept', 'birth_month']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
        writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

function_to_write_as_dictionary()
function_to_write()