from Aircraft import Aircraft
class AircraftMassenger():
    aircraft=[]
    file=open("aircraft.txt","a+")

    def __init__(self):
        self.file.seek(0)
        for Aircraft_line in self.file:
            self.aircraft.append(Aircraft.parse(Aircraft_line))

    def create(self,capacity,registrationNo,types,name):
        info = Aircraft(capacity,registrationNo,types,name)
        self.aircraft.append(info)
        self.file.write(f"{str(info)}\n")
        self.file.flush()

    def list(self):
        for info in self.aircraft:
            self.show(info)

    def find(self,registrationNo):
        for info in self.aircraft:
            if self.registrationNo==registrationNo:
                return info

    def __refreshfile(self):
        self.file = open("aircraft.txt", "w")
        for info in self.aircraft:
            self.file.write(f"{str(info)}\n")
            self.file.write("\n")

    def delete(self,registrationNo):
        info=self.find(registrationNo)
        self.aircraft.remove(info)

        self.__refreshfile()

    def update(self,capacity,registrationNo,types,name):
        info = self.find(registrationNo)
        info.capacity = capacity
        info.registrationNo = registrationNo
        info.types = types
        info.name = name
        self.__refreshfile()

    def show(self):
        print(self.name," ",self.capacity," ",self.registrationNo," ",self.types)