word_dict = {}
every_word = []
first_char = []
def make_dict():

    global sorted_word_dict

    with open('data.txt', 'r') as infile:

        content = infile.readlines()

        for line in range(len(content)):

            content[line] = content[line].split()

            for key in content[line]:

                key = key.lower()
                every_word.append(key)
                word_dict[key] = every_word.count(key)

                sorted_word_dict = {key: word_dict[key] for key in sorted(word_dict)}

def long_short_avg():

    global key_list

    with open('81747884.txt', 'w') as outfile:

        key_list = sorted_word_dict.keys()
        curr_max = 0
        curr_min = 10
        total = 0

        for key in key_list:

            if len(key) >= curr_max:

                curr_max = len(key)
                longest = key

            if len(key) <= curr_min:

                curr_min = len(key)
                shortest = key.upper()

        for word in every_word:

            total += len(word)

        total = total / len(every_word)

        outfile.write(f'Longest Word: {longest}\nShortest Word: {shortest}\nAverage Word Length: {total}\n')

def most_common_char():

    with open('81747884.txt', 'a') as outfile:
        char_val = 0

        for char in every_word:

            first_char.append(char[0])

        for i in first_char:

            if first_char.count(i) >= char_val:

                char_val = first_char.count(i)
                answer = i

        outfile.write(f'Most Common Starting Letter: {answer}\n\n')

def show_dict():

    with open('81747884.txt', 'a') as outfile:

        for val in sorted_word_dict:

            outfile.write(f'{val}: {sorted_word_dict[val]}\n')

def main():

    make_dict()
    long_short_avg()
    most_common_char()
    show_dict()

if __name__ == "__main__":

    main()

