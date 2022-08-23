class Tree ():
    def __init__(self) -> None:
        self.main = None
        self.left = None
        self.right = None
    
    def add_point(self, num):
        if self.main == None:
            self.main = num
            return
        
        if self.main < num:
            if self.left == None:
                self.left = Tree()
                self.left.main = num
            else:
                self.left.add_point(num)
                return
                
        else:
            if self.right == None:
                self.right = Tree()
                self.right.main = num
            else:
                self.right.add_point(num)
                return

    def print_tree(self):
        if self.main == None:
            print("тут ничего нет!!!")
            return

        tree = [self]
        num_obj = 1
        
        while num_obj != 0:
            new_obj = []
            for obj in tree:
                if obj != None:
                    new_obj.append(obj.main)
                else: 
                    new_obj.append(None)
            print(new_obj)
            
            new_obj = []
            num_obj = 0
            for obj in tree:
                if obj != None:
                    if  obj.right != None:
                        new_obj.append(obj.right) 
                        num_obj += 1
                    else:
                        new_obj.append(obj.right)
                        
                    if  obj.left != None:
                        new_obj.append(obj.left) 
                        num_obj += 1
                    else:
                        new_obj.append(obj.left)
                else:
                    new_obj.append(None)
                    
            tree = new_obj

    def print_max(self):
        print(self.main)

        if self.right == None:
            return
        self.right.print_max()