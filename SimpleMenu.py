from MenuItem import MenuItem
class SimpleMenuItem(MenuItem):
    def __init__(self,number,title,command):
        super().__init__(number, title)
        #self.number=number
        #self.title=title
        self.command=command
    def get_title(self):
        return self.title
    def execute(self):
        self.command()