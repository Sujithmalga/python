import random as rand

class Sujith:
    def __init__(self):
        self.capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.special = ['@','$','&']
    def new(self):
        list1 = []
        str1 = ""
        for i in range(1):
            i = rand.choice(self.capital)
            list1.append(i)
        for j in range(4):
            j = rand.choice(self.small)
            list1.append(j)
        for k in range(1):
            k = rand.choice(self.special)
            list1.append(k)
        for l in range(4):
            l = rand.randint(0,9)
            list1.append(l)
        for m in list1:
            str1 += str(m)
        rand.shuffle(list1)

        print("we suggest strong password",str1)

obj = Sujith()
obj.new()

