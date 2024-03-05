import os.path
import csv

emails = []
times = []
nums = []

def find_file():

    try:

        user = input('Input file name: ').strip()

        with open(user, 'r') as infile:

            for line in infile:

                if 'From: ' in line:

                    emails.append(line[6:].strip('\n'))

                elif 'X-DSPAM-Processed: ' in line:

                    times.append(line[30:38].strip('\n'))

                elif 'X-DSPAM-Confidence: ' in line:

                    nums.append(line[20:].strip('\n'))

    except FileNotFoundError:

        print('File does not exist!')
        find_file()

def csv_rows():

    global content

    content = emails[:]

    for i in range(len(emails)):

        content[i] = [emails[i], times[i], nums[i]]

def avg():

    total = 0

    for num in nums:

        total += float(num)

    average = total / len(nums)
    average = f'{average:.4f}'
    avg_str = ['','Average',str(average)]

    with open(user, 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(avg_str)

def out_file():

    global user

    user = input('Output file name: ')

    if os.path.isfile(user):

        over_write = input('Overwrite existing file (y/n): ').strip().lower()

        while over_write != 'y' and over_write != 'n':

            over_write = input('Enter(y/n): ').strip().lower()

        if over_write == 'n':

            new_file()

    with open(user, 'w', newline='') as outfile:

        parameter = ['Email', 'Time', 'Confidence']
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(parameter)

        for contact in content:

            writer.writerow(contact)

def new_file():

    global user

    diff_file = 'files/' + input('New output file name: ').strip()

    while os.path.isfile(diff_file):

        over_write = input('Overwrite existing file (y/n): ').strip().lower()

        while over_write != 'y' and over_write != 'n':

            over_write = input('Enter(y/n): ').strip().lower()

        if over_write == 'n':

            new_file()

    user = diff_file

    with open(user, 'w') as outfile:

        parameter = ['Email', 'Time', 'Confidence']
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(parameter)

        for contact in content:

            writer.writerow(contact)

    avg()

def main():

    find_file()
    csv_rows()
    out_file()
    avg()
    print('Data stored!')

if __name__ == "__main__":

    main()