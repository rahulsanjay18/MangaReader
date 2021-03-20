class Manga:
    def __init__(self, ch_list, ch_num):
        self.ch_list = ch_list
        self.ch_num = ch_num

    def move_one_ch_forward(self):
        self.ch_num += 1

    def move_one_ch_back(self):
        self.ch_num -= -1
