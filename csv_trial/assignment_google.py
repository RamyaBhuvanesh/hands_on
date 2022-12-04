import csv

def function_to_read():
    import csv

    with open('google_example.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(
                    f'Column names are {", ".join(row)}')
                line_count += 1
            print(f"\t{row['website_name']} has the title {row['title_of_the_page']}.")
            line_count += 1
            print(f'length of the file is  {line_count} lines.')

function_to_read()