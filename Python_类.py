class Bird:
    name = ''
    def sing(self):
        print("The bird sings")
    def drink(self):
        print("The bird drinks")


class Eagle(Bird):
    def show_name(self):
        print("This is an eagle")
    
baby_eagle = Eagle()
baby_eagle.drink()
baby_eagle.show_name()


# 类
class Student:  # 继承
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    # setters and getters
    def set_name(self,string):
        self.name = string
    def set_gender(self,string):
        self.gender = string
    
    def get_name(self):
        print(self.name)
    def get_gender(self):
        print(self.gender)


student1 = Student("John","male")
student2 = Student("Amy","female")
student1.set_gender("female")
student1.get_gender()
'''
student1.set_name("John")
student1.set_gender("male")
student2.set_name("Amy")
student2.set_gender("female")
'''


'''
# 类实例化为对象
counter1 = Counter(1)
counter2 = Counter(2)
counter1.most_common()
counter2.most_common()
'''


