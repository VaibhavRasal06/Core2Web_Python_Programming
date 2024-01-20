
class Add:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x > self.y

x_num = int(input("Enter a value of x: "))
y_num = int(input("Enter a value of y: "))

obj = Add(x_num,y_num)
result = obj.addition()
print(result)
