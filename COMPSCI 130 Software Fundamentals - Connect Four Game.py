"""
Name: Electra Bree
UPI: rbre269

This program is an implementation of the Connect Four game.
"""

class GameBoard:
    def __init__(self, size):
        self.size = size
        self.num_entries = [0] * size
        self.items = [[0] * size for i in range(size)]
        self.points = [0] * 2

    #returns number of free positions in a column
    def num_free_positions_in_column(self, column):
        return self.size - self.num_entries[column]

    #determines if game is over based on number of free positions in each column
    def game_over(self):
        for column_num in range(len(self.num_entries)):
            if self.num_free_positions_in_column(column_num) > 0:
                #if there's any free positions left, then game isn't over
                return False
        return True
    
    #displays the game board
    def display(self):
        for row in range(self.size - 1, -1, -1):
            row_string = ""
            for column in self.items[row]:
                if column == 0: #empty slot
                    row_string += "  "
                elif column == 1: #player 1's slot
                    row_string += "o "
                else: #player 2's slot
                    row_string += "x "
            print(row_string[:-1])
        print("-" * (self.size * 2 - 1))

        #print out column numbers
        column_string = ""
        for number in range(self.size):
            column_string += str(number) + " "
        print(column_string[:-1])
        print("Points player 1: {}".format(self.points[0]))
        print("Points player 2: {}".format(self.points[1]))

        #get points from player since last move
    #by calculating 4-in-a-row sequences that inserted disk made
    def num_new_points(self, row, column, player):
        points = 0
        #horizontal case
        for step in range(1,5):
            try:
                if self.items[row][column - 4 + step: column + step] == [player] * 4:
                    points += 1
            except IndexError:
                points += 0
        for case in range(3):
            for increment in range(1,5):
                count = 0
                for step in range(-4 + increment, 0 + increment):
                    try:
                        #vertical case
                        if case == 0 and self.items[row + step][column] == player:
                            count += 1
                        #diagonal case - left
                        if case == 1 and self.items[row + step][column + step] == player:
                            count += 1
                        #diagonal case - right
                        if case == 2 and self.items[row + step][column - step] == player:
                            count += 1
                    except IndexError:
                        count += 0
                if count == 4:
                    points += 1                    
        return points

    #adds new disk into column            
    def add(self, column, player):
        if column < 0 or column >= self.size or self.num_free_positions_in_column(column) == 0:
            #check if column is not valid or is full
            return False
        row = self.num_entries[column]
        self.items[row][column] = player
        self.num_entries[column] +=1
        self.points[player - 1] += self.num_new_points(row, column, player)
        return True

    #returns a list of columns with free slots
    #list is in order of distance closest to middle
    def free_slots_as_close_to_middle_as_possible(self):
        column_list = [column for column in range(self.size)]
        free_slots = []
        while column_list != []:
            mid = len(column_list) // 2
            if len(column_list) % 2 == 0:
                mid -= 1
            if self.num_free_positions_in_column(column_list[mid]) != 0:
                free_slots.append(column_list[mid])
            column_list.pop(mid)
        return free_slots
    
    #determine which column results in max number of points   
    def column_resulting_in_max_points(self, player):
        free_slots = self.free_slots_as_close_to_middle_as_possible()
        max_points = 0
        for column in free_slots:
            if self.num_free_positions_in_column(column) > 0: #consider only free slots
                row = self.num_entries[column]
                self.items[row][column] = player #add disk in slot
                points_to_earn = self.num_new_points(row, column, player)
                if points_to_earn > max_points:
                    #if slot will earn more points than previously, slice out the left part of free_slots list
                    #assuming that the previous columns are lower than this one
                    max_points = points_to_earn
                    free_slots = free_slots[free_slots.index(column):]
                elif points_to_earn < max_points: #otherwise if the opposite, just pop the column
                    free_slots.pop(free_slots.index(column))
                self.items[row][column] = 0 #remove disk from slot
        slot_number_for_max_points = free_slots[0]
        return (slot_number_for_max_points, max_points)


