class Flight():

    def __init__(self,flightno,takeofftime,takepoint,destination,landingtime,price):
        self.flightno=flightno
        self.takeofftime=takeofftime
        self.takepoint=takepoint
        self.destination=destination
        self.landingtime=landingtime
        self.price=price

    def parse(line:str):
        flightno, takeofftime, takepoint, destination, landingtime, price=line.split("\n")

        return Flight(flightno,takeofftime,takepoint,destination,landingtime,price)

    def __str__(self):
        return f"{self.flightno}\t\t{self.takeofftime}\t\t{self.takepoint}\t\t{self.destination}\t\t{self.landingtime}\t\t{self.price}"