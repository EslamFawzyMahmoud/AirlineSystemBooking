class Passenger():

    def __init__(self,name,age,PhoneNo,Email,Street,City,Country):
        self.name=name
        self.age= age
        self.PhoneNo=PhoneNo
        self.Email=Email
        self.Street=Street
        self.City=City
        self.Country=Country

    def __str__(self):
        return f"{self.name}\t{self.age}\t{self.PhoneNo}\t{self.Email}\t{self.Street}\t{self.City}\t{self.Country}"

    def parse(line:str):
        name, age, PhoneNo, Email, Street, City, Country=line.split('\n')
        return Passenger(name, age, PhoneNo, Email, Street, City, Country)