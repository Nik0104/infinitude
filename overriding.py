class Test :
    def __init__(self, model):
        self.model = model


    def Car(self):
        print("car Model is :", self.model)

class Test1(Test):
    def __init__(self, model):
        self.model = model

    def car(self):
        print("new car model is :", self.model)
obj=(Test1("SUV"))
obj.car()