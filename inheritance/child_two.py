from parent_class import Parent
class Child_two(Parent):
    def __init__(self,name,grade):
        self.grade=grade
        self.name=name

    def show_details(self):
        print(f"the child details are:Name:{self.name},grade:{self.grade}")
