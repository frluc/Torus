class Group():

    def __init__(self, group_name):
        
        self.group_name = group_name
        self.bot_list = list()

    def display_group(self):
        print("group "+self.group_name+":")
        for x in self.bot_list:
            x.print_stats()

    def size_group(self):
        return len(self.bot_list)

    def add_bot(self, bottoadd):

        if self.size_group() < 10:
            self.bot_list.append(bottoadd)
            print(bottoadd.name+" added to "+self.group_name)
        else:
            print("group already full")

    def remove_bot(self, bottoremove):

        if self.bot_list.count(bottoremove) > 0:
            self.bot_list.remove(bottoremove)
            print(bottoremove.name+" removed from "+self.group_name)
        else:
            print(bottoremove.name+" not in group")

    def pool_statforgroup(self, stattopool):

        pass
