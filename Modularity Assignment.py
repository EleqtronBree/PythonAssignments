"""
Author: Electra Bree

Reads contents of a text file, analyzes tags used in a sentence and draws a histogram of results
"""

import random

def read_content(filename):
    file = open(filename)
    # read lines and save into a list
    lines = file.readlines()
    
    # remove \n and empty elements
    for index in range(len(lines) -1, -1, -1):
        if "\n" in lines[index]:
            lines[index] = lines[index][:lines[index].rfind("/")]
        if lines[index] == "":
            lines.pop(index)
    file.close()
    return lines

def get_tag_words(line):
    # separate tag from words
    tag_word_list = line.split(":") 
    tag = tag_word_list[0]
    words = tag_word_list[1]
    
    # make a sorted list of words
    words = sorted(words.split()) # split by whitespace
    
    # make a tuple and return it
    return (tag, words)

def create_tags_dictionary(filename):
    list_of_lines = read_content(filename)
    tags_dictionary = {}
    for line in list_of_lines:
        tags_tuple = get_tag_words(line)
        tag = tags_tuple[0]
        words = tags_tuple[1]
        tags_dictionary[tag] = words
    return tags_dictionary

def get_sorted_unique_words_list(sentence):
    # convert sentence to lowercase
    word_list = sentence.lower().split()
    # add to unique list
    unique_list = []
    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)
    # returns sorted & unique lowercase
    return sorted(unique_list)

def get_word_tag_tuple(tags_dictionary, search_word):
    for key in tags_dictionary.keys():
        if search_word in tags_dictionary[key]:
            return (search_word,key)

def get_tag_tuple_list(tags_dictionary, sentence):
    tag_tuple_list = []
    unique_word_list = get_sorted_unique_words_list(sentence)
    for search_word in unique_word_list:
        word_tuple = get_word_tag_tuple(tags_dictionary, search_word)
        tag_tuple_list.append(word_tuple)
    return tag_tuple_list

def filtering(list_of_tuples, filter_list):
    filtered_tuple_list = []
    for word_tag_tuple in list_of_tuples:
        if word_tag_tuple[1] in filter_list:
            filtered_tuple_list.append(word_tag_tuple)
    return filtered_tuple_list

def grouping(list_of_tuples, new_tag, grouping_list):
    new_tuple_list = []
    for word_tuple in list_of_tuples:
        if word_tuple[1] in grouping_list:
            new_tuple = (word_tuple[0], new_tag)
            new_tuple_list.append(new_tuple)
        else:
            new_tuple_list.append(word_tuple)
    return new_tuple_list

def get_tags_frequency(list_of_tuples):
    tags_frequency_dictionary = {}
    # loop through each tag and count frequency of them
    for word_tag_tuple in list_of_tuples:
        if word_tag_tuple[1] not in tags_frequency_dictionary:
            tags_frequency_dictionary[word_tag_tuple[1]] = 1
        else:
            tags_frequency_dictionary[word_tag_tuple[1]] += 1
    return tags_frequency_dictionary

def display_histogram(tags_freq):
    for tag, frequency in sorted(tags_freq.items()):
        number_of_x = "X" * frequency
        print("{:4}|{}".format(tag, number_of_x))

def create_my_tags_dictionary(list_of_tags):
    tags_dictionary = {}
    for a_tuple in list_of_tags:
        tag = a_tuple[1]
        word = a_tuple[0]
        if tag not in tags_dictionary:
            tags_dictionary[tag] = [word]
        else:
            tags_dictionary[tag] += [word]
            tags_dictionary[tag].sort()
    return tags_dictionary

def make_phrases(my_tags_dictionary):
    for article in my_tags_dictionary["DT"]:
        DT = article
        for adjective in my_tags_dictionary["JJ"]:
            JJ = adjective
            for noun in my_tags_dictionary["NN"]:
                NN = noun
                print(DT, JJ, NN)

def main():
    filename = input("Enter a filename: ")
    sentence = input("Enter a sentence: ")
    tags_dictionary = create_tags_dictionary(filename)
    list_of_tags = get_tag_tuple_list(tags_dictionary, sentence)
    filter_list = ['DT','NN','NNS','NNP','NNPS','JJ','JJR','JJS']
    list_of_tags = filtering(list_of_tags, filter_list)
    list_of_tags = grouping(list_of_tags, 'NN', ['NN','NNS','NNP','NNPS'])
    list_of_tags = grouping(list_of_tags, 'JJ', ['JJ','JJR','JJS'])
    tags_freq = get_tags_frequency(list_of_tags)
    display_histogram(tags_freq)
    my_tags_dictionary = create_my_tags_dictionary(list_of_tags)
    make_phrases(my_tags_dictionary)
    
main()
