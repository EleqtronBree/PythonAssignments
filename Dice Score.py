"""
Author: Electra Bree

Gets the dice score
"""

def get_dice_score(dice_list):
    score = 0
    number = 1
    copy_list = dice_list[::]
    while 1 in copy_list:
        copy_list.pop(copy_list.index(1))
        score += 1
        if 2 in copy_list:
            copy_list.pop(copy_list.index(2))
            score += 2
            if 3 in copy_list:
                copy_list.pop(copy_list.index(3))
                score += 3
                if 4 in copy_list:
                    copy_list.pop(copy_list.index(4))
                    score += 4
                    if 5 in copy_list:
                        copy_list.pop(copy_list.index(5))
                        score += 5
                        if 6 in copy_list:
                            copy_list.pop(copy_list.index(6))
                            score += 6
    return score

def test_get_dice_score():
    print("1.  score: ", get_dice_score([5, 3, 2, 5, 4, 5, 6, 4, 3]))
    print("2.  score: ", get_dice_score([3, 4, 1, 5, 3, 1, 4, 6]))
    print("3.  score: ", get_dice_score([5, 3, 2, 2, 6, 4, 5, 1, 4]))
    print("4.  score: ", get_dice_score([2, 1, 1, 1, 2, 3, 3, 1, 3, 2]))
    print("5.  score: ", get_dice_score([3, 4, 1, 5, 2, 1, 5, 1, 2, 3, 4, 6]))
    print("6.  score: ", get_dice_score([]))

    list1 = [5, 3, 2, 5, 5, 6, 4, 3, 2, 1, 1, 5, 2, 5, 1]
    list1_copy = list1[::]
    list1_copy.sort()
    print("7.  list: ", list1)
    score1 = get_dice_score(list1)
    print("    list_sorted: ", list1_copy)
    print("    score:", score1)
    print()

    list1 = [5, 3, 2, 6, 4, 5, 1, 4, 1, 2, 6, 4]
    list1_copy = list1[::]
    list1_copy.sort()
    print("8.  list: ", list1)
    score1 = get_dice_score(list1)
    print("    list_sorted: ", list1_copy)
    print("    score:", score1)
    print()

    list1 = [2, 1, 1, 1, 2, 3, 3, 2, 3]
    list1_copy = list1[::]
    list1_copy.sort()
    print("9.  list: ", list1)
    score1 = get_dice_score(list1)
    print("    list_sorted: ", list1_copy)
    print("    score:", score1)
    print()

test_get_dice_score()
