class Car:
    def __init__(self,color, model, year,owner):
        self.color = color
        self.model = model
        self.year = year
        self.__owner = owner    #定义以双下划线命名的为（私有属性）
#私有方法也可以利用这个命名方式
#没有真正的私有化 _+类名+私有属性就可以调用了
    def start(self):
        print(self.color)
        print(self.model)
        print(self.year)

    def get_owner(self):
        return self.__owner[0] + "**"
    #在类的外部可以利用这个方法得到私有属性

    def charge(self):
        print(f"{self.model}正在补充燃料")

#继承父类的公共属性和方法
class electricCar(Car):
    def charge(self):
        #调用父类中的方法两种方式
        #方式一 :
        #类名.方法名(self) Car.charge(self)
        super().charge()
        print(f"{self.model}正在充电")

class aiDriving:
    def __init__(self,urban,rural):
        self.urban = urban
        self.rural = rural

#多继承 MRO ->方法解析顺序
class teslaCar(Car,aiDriving):#优先采用前面的属性和方法
    pass

#多态
def charge (car: Car): #函数参数类型注解 -> 指定的是父类
    # 传参的时候可以用子类 调用的也是子类的方法
    car.charge()
#鸭子类型：只关注对象的行为，而不是对象的类型 不存在继承关系

if __name__ =='__main__':
    car = electricCar("red", "Mercedes", 1999, "yu")
    print(car.get_owner())
    car.charge()
    print(teslaCar.__mro__)#显示解析顺序