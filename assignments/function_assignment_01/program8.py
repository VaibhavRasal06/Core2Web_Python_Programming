class Biencaps:

    total_employee = 20

    def __init__(self):
        self.developer = 16
        self.editor = 2
        self.teacher = 2

    def comp_info(self):
        print("total developers at Biencaps is: ",self.developer)
        print("total editors at Biencaps is: ",self.editor)     
        print("total teachers at Biencaps is: ",self.teacher)

obj = Biencaps()
obj.comp_info()
print("total employee at Biencaps is: ",Biencaps.total_employee)
