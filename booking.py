class Booking:

    def __init__(self,destination,TimeOfFlight,TypeOfFlight,Price,SitNumber,name):
        self.name=name
        self.TimeOfFlight=TimeOfFlight
        self.TypeOfFlight=TypeOfFlight
        self.Price=Price
        self.SitNumber=SitNumber
        self.destination=destination

    def __str__(self):
        return f"{self.name}\t\t{self.SitNumber}\t\t{self.destination}\t\t{self.TimeOfFlight}\t\t{self.TypeOfFlight}\t\t{self.Price}"

    def parse(line:str):
        name,SitNumber,destination,TimeOfFlight,TypeOfFlight,Price=line.split('\n')

        return Booking(name,SitNumber,destination,TimeOfFlight,TypeOfFlight,Price)

