#3
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __getattr__(self, item):
        return "This attribute is not available"



#4
class Rectangle:
    def __init__(self, width, height):
        super().__setattr__('width', width)
        super().__setattr__('height', height)

    def __setattr__(self, name, value):
        if not hasattr(self, name):
            raise AttributeError("Local attributes are not allowed")
        super().__setattr__(name, value)

