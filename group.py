class Group():

    def __init__(self, group_name):
        
        self.group_name = group_name
        self.bot_list = list()

    def groupdisplay(self):
        print("group "+self.group_name+":")
        for x in self.bot_list:
            x.print_stats()

    def groupsize(self):
        return len(self.bot_list)

    def addbot(self, bottoadd):

        if self.groupsize() < 10:
            self.bot_list.append(bottoadd)
            print(bottoadd.name+" added to "+self.group_name)
        else:
            print("group already full")

    def removebot(self, bottoremove):

        if self.bot_list.count(bottoremove) > 0:
            self.bot_list.remove(bottoremove)
            print(bottoremove.name+" removed from "+self.group_name)
        else:
            print(bottoremove.name+" not in group")
