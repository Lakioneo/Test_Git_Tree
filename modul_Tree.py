class Tree ():
    def __init__(self) -> None:
        main = None
        left = None
        right = None
    
    def add_point(self, num):
        if self.main == None:
            self.main = num
            return
        
        if self.main < num:
            if self.left == None:
                self.left = Tree().main = num
            else:
                self.left.add_point(num)
                
        else:
            if self.right == None:
                self.right = Tree().main = num
            else:
                self.right.add_point(num)

    def print_tree(self):
        pass