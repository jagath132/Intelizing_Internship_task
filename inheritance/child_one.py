from parent_class import Parent
class Child_one(Parent):
    def __init__(self,name,age):
        self.age=age
        self.name=name
    
    def show_details(self):
        print(f"the child details are:Name:{self.name},Age:{self.age}")
