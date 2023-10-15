class Person:
    def __init__(self,name,place_resident):
        self.name=name
        self.place_resident=place_resident
    def display_attr(self):
        print("Name :",self.name)
        print("Place Of Resident :",self.place_resident)
class Sister(Person):
    def __init__(self,name, place_resident,exam_sub):
        super().__init__(name, place_resident)
        self.exam_sub=exam_sub
    def display_attr(self):
        super().display_attr()
        print(self.exam_sub)
        
class Uncle(Person):
    def __init__(self, name, place_resident,business):
        super().__init__(name, place_resident)
        self.business=business
        print(self.business)
    def display_attr(self):
        super().display_attr()


s1=Sister("Sneha","Pune","Physics")
s1.display_attr()
u1=Uncle("Maria","Mumbai","Tapari")
u1.display_attr()
