from booking import Booking

class Bookingmanager():
    Bookings=[]

    def __init__(self,flightmg,passangermg):
        self.flightmg=flightmg
        self.passangermg=passangermg

    def list(self):
        for info in self.Bookings:
            self.show(info)

    def show(self):
        print("Name\tSitNumber\tDestination\tTimeOfFlight\tTypeOfFlight\tPrice")
        print(self.name," ",self.SitNumber," ",self.destination," ",self.TimeOfFlight," ",self.TypeOfFlight," ",self.Price)

    def find(self, SitNumber):
        for info in self.Bookings:
            if info.SitNumber == SitNumber:
                return info

    def create(self,destination,TimeOfFlight,TypeOfFlight,Price,SitNumber,name,flightno,PhoneNo):
        avalfligth=self.flightmg.find(flightno)
        avalpassenger=self.passangermg.find(PhoneNo)

        if avalpassenger ==None:
            print("Passenger Not Valid")
            return False
        else:
            if avalfligth==None:
                print("Flight Not Valid")
                return False

            else:
                info=Booking(destination,TimeOfFlight,TypeOfFlight,Price,SitNumber,name)
                self.Bookings.append(info)
                return True

    def remove(self,SitNumber):
        info=self.find(SitNumber)
        self.Bookings.remove(info)

    def update(self,destination,TimeOfFlight,TypeOfFlight,Price,SitNumber,name):
        info=self.find(SitNumber)

        info.name = name
        info.TimeOfFlight = TimeOfFlight
        info.TypeOfFlight = TypeOfFlight
        info.Price = Price
        info.SitNumber = SitNumber
        info.destination = destination