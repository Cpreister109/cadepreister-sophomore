import csv
import re
contacts = []
only_one = []
every_em = []
em_dict = {}

def new_r():

    with open('input.txt', 'r') as email:

        frm = re.compile('^From ')

        for i in email:
            pattern = frm.search(i)
            if pattern:
                curr_l = i.strip('/n').split()
                del curr_l[0]
                contacts.append(curr_l)

def new_w():

    cont_l = open('output.csv', 'w', newline='')

    cont_l.write('Email,Day,Date,Month,Year,Time\n')

    for i in range(len(contacts)):

        for j in range(len(contacts[i])):

            if contacts[i].index(contacts[i][j]) == 2:

                temp = contacts[i][j]
                contacts[i][j] = contacts[i][j + 1]
                contacts[i][j + 1] = temp

    for i in range(len(contacts)):

        for j in range(len(contacts[i])):

            if contacts[i].index(contacts[i][j]) == 4:

                temp = contacts[i][j]
                contacts[i][j] = contacts[i][j + 1]
                contacts[i][j + 1] = temp

    for i in range(len(contacts)):

        for j in range(len(contacts[i])):

            if contacts[i].index(contacts[i][j]) != 5:

                cont_l.write(f'{contacts[i][j]}, ')

            else:

                cont_l.write(f'{contacts[i][j]}')

        cont_l.write('\n')

    cont_l.close()

def new_ct():

    total = 0

    amount_em = open('output.txt', 'w')

    for i in contacts:

        for j in i:

            if i[0] not in only_one:

                only_one.append(i[0])

        every_em.append(i[0])

    amount_em.write(f'{"Email":40s}- Count\n')

    for em in only_one:

        curr_count = int(every_em.count(em) / 2)
        total += curr_count

        em_dict[em] = curr_count

    for email in em_dict:

        amount_em.write(f'{email:40s}- {em_dict[email]}\n')

    amount_em.write('-' * 48 + f'\n{"Total emails":40s}- {total}')

    amount_em.close()

def main():

    new_r()
    new_r()
    new_ct()

if __name__ == "__main__":

    main()