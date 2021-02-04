from passenger import Passenger

class passengerManager():
    passengers=[]
    file=open("passangers.txt",'a+')
    def __init__(self):
        self.file.seek(0)
        for Passenger_line in self.file:
            self.passengers.append(Passenger.parse(Passenger_line))

    def list(self):
        for info in self.passengers:
            self.show(info)

    def show(self,info):
        print("Name\tAge\tPhoneNumber\tEmail\tStreet\tCity\tCountry")
        print(info.name," ", info.age," ", info.PhoneNo," ", info.Email," ", info.Street," ",info.City," ",info.Country)

    def find(self,PhoneNo):
        for info in self.passengers:
            if info.PhoneNo == PhoneNo:
                return info

    def remove(self,PhoneNo):
        info = self.find(PhoneNo)
        self.passengers.remove(info)
        self.__refreshfile()

    def __refreshfile(self):
        self.file=open("passangers.txt","w")
        for info in self.passengers:
            self.file.write(f"{str(info)}\n")
            self.file.write("\n")

    def update(self,name,age,PhoneNo,Email,Street,City,Country):
        info = self.find(PhoneNo)
        info.name=name
        info.age=age
        info.PhoneNo=PhoneNo
        info.Email=Email
        info.Street=Street
        info.City=City
        info.Country=Country
        self.__refreshfile()

    def create(self,name,age,PhoneNo,Email,Street,City,Country):
        info=self.passengers(name,age,PhoneNo,Email,Street,City,Country)
        self.passengers.append(info)
        self.file.write(f"{str(info)}\n")
        self.file.flush()