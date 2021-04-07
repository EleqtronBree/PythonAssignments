"""
Author: Electra Bree

Gets the longest word in a list containing e
"""

def get_longest_e_word(words_list):
    longest_word = ''
    e_word_list = []
    longest_word = ""
    for word in words_list:
        if len(word) > 5:
            if 'E' in word or 'e' in word:
                e_word_list.append(word)
    for word in e_word_list:
        if (len(word) > len(longest_word)) or (len(word) == len(longest_word)):
            longest_word = word
    return longest_word


print("1.", get_longest_e_word(["Melissa", "Jessie", "Kath", "Amity", "Raeann"]))
print("2.", get_longest_e_word(["Jo", "Jessie", "Penelope", "Jin", "Raeann", "Pamelita"]))
print("3.", get_longest_e_word(["Alan", "Melita", "Amity", "Rosalia", "Rositta", "LeeAnne"]))
print("4. ", "***", get_longest_e_word(["Jo", "Jai", "Jen", "Jing", "Joey", "Jess"]), "***", sep = "")
print("5. ", "***", get_longest_e_word([]), "***", sep = "")
print("6.", "***" + get_longest_e_word([""]) + "***")
                
