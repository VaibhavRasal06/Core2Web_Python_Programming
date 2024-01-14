
class A:

    def a(self):
        print("A")

class B1(A):

    def b1(self):
        print("B1")

class B2(A):

    def b2(self):
        print("B2")

class B3(A):

    def b3(self):
        print("B3")

class C1(B1,B2):

    def c1(self):
        print("C1")

class C2(B1,B3):

    def c2(self):
        print("C2")

class D(C2,C1):
    pass

print(D.mro())

