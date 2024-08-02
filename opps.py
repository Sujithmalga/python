
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def new(self):
#         print("first class",self.a,self.b)
# class akshith(sujith):
#         def __init__(self, a, b):
#             super().__init__(a, b)
#         def new3(self):
#             print("second class",self.a,self.b)
#         # print("secoond:",a,b)
# if __name__ == "__main__":
#   obj = akshith(2,3)
#   obj.new3()
#   obj.new()



class sujith:
      def __init__(self,a,b):
          self.a = a
          self.b = b
      def anagram(self):
          if len(self.a) != len(self.b):
              print("not anagram")
          c = {}
          d = {}
          for i in self.a:
              if i in c:
                  c[i] += 1
              else:
                  c[i] = 1
          for j in b:
              if j in d:
                  d[j] += 1
              else:
                  d[j] = 1
          return c == d
      def check_fuc(self):
          if self.anagram():
              print("angram")
          else:
              print("not angram")

if __name__ == "__main__":
  a  = input("ener the word")
  b = input("enetr the word2")

obj = sujith(a,b)
obj.check_fuc()

          
  
              