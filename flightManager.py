from flight import Flight

class FlightManager():
    Flight=[]
    file = open("Flight.txt","a+")

    def __init__(self,acmgr):
        self.acmgr=acmgr
        self.file.seek(0)
        for Flight_line in self.file:
            self.Flight.append(Flight.parse(Flight_line))

    def create(self, flightno, takeofftime, takepoint, registrationNo, destination, landingtime, price):
        aircraft = self.acmgr.find(registrationNo)
        if aircraft == None:
            print("Aircraft", registrationNo, "is not available")
            return False
        else:
            avalFlight = Flight(flightno, takeofftime, takepoint, destination, landingtime, price)
            self.Flight.append(avalFlight)
            self.file.write(f"{str(avalFlight)}\n")
            self.file.flush()
            return True

    def list(self):
        for info in self.Flight:
            self.show(info)

    def show(self,info):
        print(info.flightno," ",info.takeofftime," ",info.takepoint," ",info.destination," ",info.landingtime," ",info.price)

    def update(self,flightno,takeofftime,takepoint,aircraft,destination,landingtime,price):
        info =self.find(flightno)

        info.flightno=flightno
        info.takeofftime=takeofftime
        info.takepoint=takepoint
        info.aircraft=aircraft
        info.destinatio=destination
        info.landingtime=landingtime
        info.price=price
        self.__refreshfile()

    def delete(self,flightno):
        info = self.find(flightno)
        self.Flight.remove(info)
        self.__refreshfile()

    def find(self,flightno):
        for info in self.Flight:
            if info.flightno==flightno:
                return info

    def __refreshfile(self):
        self.file = open("Flight.txt", "w")
        for info in self.Flight:
            self.file.write(f"{str(info)}\n")
            self.file.write("\n")