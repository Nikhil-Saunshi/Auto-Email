import csv
import email_sender


def main(csv_file):
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        print(csv_file, '\n', csv_reader)
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(
                    f'\t{row[0]} email id is \t\t{row[2]} works at \t{row[3]}.')
                line_count += 1
                first_name, email = email_sender.set_content(
                    to_email_id=row[2], first_name=row[0])
                email_sender.send_email(first_name, email)
                if line_count == 2:
                    break
        print(f'Processed {line_count} lines.')


csv_file = 'test.csv'
main(csv_file)
