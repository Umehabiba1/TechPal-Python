class Company:
    def __init__(self, name, proj):
        self.name = name      # name (name of company) is public
        self._proj = proj      # proj (current project) is protected
    
    def show(self):
        print("The code of the company is =", self.name)

class Emp(Company):
    
    def __init__(self, e_name, sal, c_name, proj):
        # Calling parent class constructor
        super().__init__(c_name, proj)
        self.name = e_name   # Public member variable
        self.__sal = sal     # Private member variable
    
    def show_sal(self):
        print("The salary of", self.name, "is", self.__sal)

c = Company("Software", "Web project")
e = Emp("Ali", 25000, c.name, c._proj)

print("Welcome to", c.name)
print("Here", e.name, "is working on", e._proj)
e.show_sal()
