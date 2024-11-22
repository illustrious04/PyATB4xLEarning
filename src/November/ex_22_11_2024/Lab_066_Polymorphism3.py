"""
# Method Overloading:
* Python DOes Not support Method Overloading
*
"""

class MultiUtils(object): # is-A object class if you type (object) or not

    def add(self,a,b):
        return a + b

    def add(self, a,b,c=0):
        return a + b + c

sum = MultiUtils()
opt1 = sum.add(3,5)
print(opt1)

