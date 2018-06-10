"""
@author - Sivaramakrishnan
"""
import numpy as np

class create_data_matrix(object):
    def __init__(self,FILE_NAME):
        self.FILE_NAME = FILE_NAME
        self.data = []
        self.labels = []
        self.start_tag = "<s>"
        self.end_tag = "<e>"
        self.number_of_on_either_side = 1

    def add_start_end_tags(self):
        self.whole_string = [self.start_tag]
        self.whole_labels = ["O"]
        with open(self.FILE_NAME) as f:
            for each_line in f:
                if each_line != "\n":
                    space_count = 0
                    word,tag = each_line.strip().split()
                    self.whole_string.append(word)
                    self.whole_labels.append(tag)
                else:
                    space_count += 1
                    if space_count == 1:
                        self.whole_string.append(self.end_tag)
                        self.whole_labels.append("O")
                    if space_count == 2:
                        self.whole_string.append(self.start_tag)
                        self.whole_labels.append("O")
        self.whole_string = self.whole_string[:-1]
        self.whole_labels = self.whole_labels[:-1]


    def create_matrix(self):
        self.data = []
        self.labels = []
        count = 1
        while(count < (len(self.whole_string) - self.number_of_on_either_side)):
            self.data.append([self.whole_string[count - 1],self.whole_string[count],self.whole_string[count + 1]])
            self.labels.append(self.whole_labels[count])
            count += 1






