# https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

# make a list from a to z
alphabet = []
for letter in range(97, 123):
    alphabet.append(chr(letter))

# return a value for a lowercase letter
def lettertovalue(l):
    return alphabet.index(l) + 1

# returns sum of a word
def lettersum(word):
    sum = 0
    for letter in word:
        sum += lettertovalue(letter)
    return sum

# put words from enable1.txt into a list
lines = []
with open('enable1.txt') as file:
    lines = file.readlines()
    # strip white spaces at the end of the string
    lines = [line.rstrip() for line in lines]

def has_no_letters_in_common(word1, word2):
    for letter in word1:
        if letter in word2:
            return False
    return True


def main_challenge():
    print('\n### main challenge ###\n')

    print(lettersum(""))
    print(lettersum("a"))
    print(lettersum("z"))
    print(lettersum("cab"))
    print(lettersum("excellent"))
    print(lettersum("microspectrophotometries"))


def bonus_1():
    print('\n### optional bonus 1 ###\n')
    # find a word using a lettersum
    result = ''
    for line in lines:
        if lettersum(line) == 319 :
            result = line
    print(result, 'is the only word with a lettersum of 319')


def bonus_2():
    print('\n### optional bonus 2 ###\n')
    oddwordcounter = 0
    for x in lines:
        if lettersum(x) % 2 == 1 :
            oddwordcounter += 1

    print('there are', oddwordcounter, 'words with an odd letter sum')


def bonus_3():
    print('\n### optional bonus 3 ###\n')
    
    mostcommonlettersum = 0
    wordcount = 0
    
    # dictionary with: 
    # key = lettersum
    # value = number of words
    dict_sum_count = {}

    for line in lines:
        sum = lettersum(line)
        # if lettersum is in dict: set to 1, else add 1 
        if sum in dict_sum_count.keys():
            dict_sum_count[sum] += 1
        else:
            dict_sum_count[sum] = 1
        # set most common letter sum
        if dict_sum_count[sum] > wordcount:
            wordcount = dict_sum_count[sum]
            mostcommonlettersum = sum

    print('the most common lettersum is', mostcommonlettersum, 'and there are' , wordcount, 'words with that lettersum')


def bonus_4():
    print('\n### optional bonus 4 ###\n')

    # dictionary with:
    # key = lettersum 
    # value = pair of words
    pairofwords= {}

    # dictionary with:
    # key = lettersum 
    # value = list of words
    dict_list_words_with_sum = {}
    
    for line in lines:
        sum = lettersum(line)
        if  sum in dict_list_words_with_sum.keys():
            dict_list_words_with_sum[sum] += [line]
        else:
            dict_list_words_with_sum[sum] = [line]
    
    for sum in dict_list_words_with_sum.keys():
        # make dict with key=word and value=length of word, words have same lettersum
        dict_lenword = {}
        for word in dict_list_words_with_sum[sum]:
            dict_lenword[word] = len(word)
        for word in dict_lenword.keys():
            max_length = dict_lenword[word] + 11
            min_length = dict_lenword[word] - 11
            # search for another word with a length difference of 11
            if max_length in dict_lenword.values() or min_length in dict_lenword.values():
                # add the word in the 'pairofwords' dict
                if sum in pairofwords.keys():
                    pairofwords[sum] += [word]
                else:
                    pairofwords[sum] = [word]

    print("pair of words with the same letter sum and a length difference of 11:\n")
    for key in pairofwords.keys():
        print(pairofwords[key], "\n")


def bonus_5():
    print('\n### optional bonus 5 ###\n')

    # dictionary with:
    # key = lettersum greater than 188
    # value = list of words
    dict_list_words_with_sum = {}    
    
    for line in lines:
        sum = lettersum(line)
        if sum in dict_list_words_with_sum.keys() and sum > 188:
            dict_list_words_with_sum[sum] += [line]
        elif sum > 188:
            dict_list_words_with_sum[sum] = [line]
            
    lst_solution = []
    
    # search for the pairs
    for sum in dict_list_words_with_sum.keys():
        # list of words with same lettersum
        list_words = dict_list_words_with_sum[sum]
        for index1 in range(0, len(list_words)):
            word1 = list_words[index1]
            for index2 in range(0, len(list_words)):
                word2 = list_words[index2]
                # append pair if it has no letters in common and if the pair is not already in the list
                if has_no_letters_in_common(word1, word2) and [word2, word1] not in lst_solution:
                    lst_solution.append([word1, word2])
    
    print("pair of words with no letters in common and same lettersum, which is greater than 188:\n", lst_solution)


# sort both in descending order of word length, and ascending order of letter sum
def sort_by_length_and_sum(w):
     return (len(w) * -1, lettersum(w))


# very slow
def bonus_6():
    print('\n### optional bonus 6 ###\n')

    lines_sorted_by_length = lines.copy()
    lines_sorted_by_length.sort(key = sort_by_length_and_sum)
    winning_solution = []

    unique_lengths = []
    # make list of all distinct lengths
    for line in lines_sorted_by_length:
        if len(line) not in unique_lengths:
            unique_lengths.append(len(line))
    

    # go through all different distinct lengths
    for length in unique_lengths:
        solution = []
        # add a first word to solution
        first_element = next(filter(lambda first_word: len(first_word) == length, lines_sorted_by_length), None)
        solution.append(first_element)

        # add words if its length is smaller than the last element and its lettersum is bigger than the last element
        for lijn in lines_sorted_by_length:
            len_current_line = len(lijn)
            len_latest_line = len(solution[len(solution)-1])
            sum_current_line = lettersum(lijn)
            sum_latest_line = lettersum(solution[len(solution)-1])
            if len_current_line < len_latest_line and sum_current_line > sum_latest_line:
                solution.append(lijn)
        # set the longest list
        if len(solution) > len(winning_solution):
            winning_solution = solution.copy()
    
    print(winning_solution)



main_challenge()
bonus_1()
bonus_2()
bonus_3()
bonus_4()
bonus_5()
bonus_6()