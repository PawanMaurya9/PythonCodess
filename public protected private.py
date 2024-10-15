#------Encapsulation-------#
#Public data member within a class
'''class Ex:
    def __init__(self):
        self.x=10
    def m1(self):
        print(self.x)
ob=Ex()
ob.m1()
# Public data member within a child class
class Ex:
    def __init__(self):
        self.x=10
class B(Ex):
    def m1(self):
        print(self.x)
ob=B()
ob.m1()

# Public data member outside the  class
class Ex:
    def __init__(self):
        self.x=10
ob=Ex()
print(ob.x)'''


'''#Protected data member within a class
class Ex:
    def __init__(self):
        self._x=10
    def m1(self):
        print(self._x)
ob=Ex()
ob.m1()
# Protected data member within a child class
class Ex:
    def __init__(self):
        self._x=10
class B(Ex):
    def m1(self):
        print(self._x)
ob=B()
ob.m1()

# Protected  data member outside the  class
class Ex:
    def __init__(self):
        self._x=10
ob=Ex()
print(ob._x)'''



'''#Private data member within a class
class Ex:
    def __init__(self):
        self.__x=10
    def m1(self):
        print(self.__x)
ob=Ex()
ob.m1()
# Private data member within a child class
class Ex:
    def __init__(self):
        self.__x=10
class B(Ex):
    def m1(self):
        print(self.__x)
ob=B()
ob.m1()

# Private data member outside the  class
class Ex:
    def __init__(self):
        self.__x=10
ob=Ex()
print(ob.__x)'''


'''#Public method within a  class
class Ex:
    def pubm(self):
        print('from public method ')
    def show(self):
        self.pubm()
ob=Ex()
ob.show()

#Public method within a  child class

class Ex:
    def pubm(self):
        print('from public method ')
    def show(self):
        self.pubm()
class B(Ex):
    def pubm(self):
        return super().pubm()
ob=Ex()
ob.show()

#Public method outside the   class

class Ex:
    def pubm(self):
        print('from public method ')
ob=Ex()
ob.pubm()


#Protected method within a  class
class Ex:
    def _pubm(self):
        print('from public method ')
    def show(self):
        self._pubm()
ob=Ex()
ob.show()

#Protected method within a  child class

class Ex:
    def _pubm(self):
        print('from public method ')
    def show(self):
        self._pubm()
class B(Ex):
    def _pubm(self):
        return super()._pubm()
ob=Ex()
ob.show()

#Protected method outside the   class

class Ex:
    def _pubm(self):
        print('from public method ')
ob=Ex()
ob._pubm()


#Private method within a  class
class Ex:
    def __pubm(self):
        print('from public method ')
    def show(self):
        self.__pubm()
ob=Ex()
ob.show()

#Private method within a  child class

class Ex:
    def __pubm(self):
        print('from public method ')
    def show(self):
        self.__pubm()
class B(Ex):
    def __pubm(self):
        return super().__pubm()
ob=Ex()
ob.show()

#Private method outside the   class

class Ex:
    def __pubm(self):
        print('from public method ')
ob=Ex()
ob.__pubm()'''

#-------Method--------#
class Std:
    def __init__(self,name,regno,marks):
        self.name=name
        self._regno=regno
        self.__marks=marks
    def display(self):
        print("Student name is: ",self.name)
        print("Student regno is: ",self._regno)
        print("Student marks is: ",self.__marks)
    def __get_marks(self):
        print("Students marks is",self.__marks)
        
ob=Std('pawan',123,50)
ob.display()