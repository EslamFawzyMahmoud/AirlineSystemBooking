from AircraftManager import AircraftMassenger
from flightManager import FlightManager
from BookingManager import Bookingmanager
from passengerManager import passengerManager

aircraftManager = AircraftMassenger()
flightManager = FlightManager(aircraftManager)
PassagerManager = passengerManager()
BookingManager =Bookingmanager(flightManager,PassagerManager)

def MainMenu():
    print("Enter 0 to exit")
    print("Enter 1 to Manage Aircraft")
    print("Enter 2 to Manage Flights")
    print("Enter 3 to Manage Bookings")
    print("Enter 4 to Manage Passenger")

def ShowSubMenu(option):
    if option=='1':
        ShowAircraftMenu()
        suboption=input()
        if suboption=='0':
            MainMenu()
        else:
            HandleMAanageAircraftAction(suboption)

    elif option =='2':
        ShowAircraftMenu()
        suboption = input()
        if suboption == '0':
            MainMenu()
        else:
            HandleMAanageFligthAction(suboption)

    elif option =='3':
        ShowBookingrMenu()
        suboption = input()
        if suboption == '0':
            MainMenu()
        else:
            HandleMAanageBookingAction(suboption)

    elif option == '4':
        ShowPassengerMenu()
        suboption=input()
        if suboption=='0':
            MainMenu()
        else:
            HandleMAanagePassengerAction(suboption)

def ShowPassengerMenu():
    print("Enter 0 to return MainMenu")
    print("Enter 1 to List Passenger")
    print("Enter 2 to Create Passenger")
    print("Enter 3 to Update Passenger")
    print("Enter 4 to Delete Passenger")

def ShowBookingrMenu():
    print("Enter 0 to return MainMenu")
    print("Enter 1 to List Booking")
    print("Enter 2 to Create Booking")
    print("Enter 3 to Update Booking")
    print("Enter 4 to Delete Booking")

def ShowFlightMenu():
    print("Enter 0 to return MainMenu")
    print("Enter 1 to List Flight")
    print("Enter 2 to Create Flight")
    print("Enter 3 to Update Flight")
    print("Enter 4 to Delete Flight")

def ShowAircraftMenu():
    print("Enter 0 to return MainMenu")
    print("Enter 1 to List Aircraft")
    print("Enter 2 to Create Aircraft")
    print("Enter 3 to Update Aircraft")
    print("Enter 4 to Delete Aircraft")

def HandleMAanageAircraftAction(suboption):

    if suboption == '1':
        aircraftManager.list()

    elif suboption == '2':
        aircraftno = input("Enter Aircraft No? ")
        capacity = input("Enter Aircraft Capacity? ")
        name = input("Enter Aircraft name? ")
        type = input("Enter Aircraft type?")
        aircraftManager.create(capacity, aircraftno, type, name)
        print("Congrate! your aircraft",aircraftno," is created successfully")
    elif suboption == '3':
        aircraftno = input("Enter Aircraft No? ")
        capacity = input("Enter Aircraft Capacity? ")
        name = input("Enter Aircraft name? ")
        type = input("Enter Aircraft type?")
        aircraftManager.update(capacity, aircraftno, type, name)
        print(aircraftno," is update.")
    else:
        aircraftno = input("Enter Aircraft No? ")
        aircraftManager.delete(aircraftno)
        print(aircraftno,"is Deleted .")

    ShowSubMenu("1")

def HandleMAanageFligthAction(suboption):

    if suboption == '1':
        flightManager.list()

    elif suboption == '2':
        flightno = input("Enter Flight No? ")
        takeofftime = input("Enter takeoffTime? ")
        takepoint = input("Enter takepoint? ")
        registrationNo = input("Enter registartioNo ? ")
        destination = input("Enter your destination? ")
        landingtime = input("Enter landing time? ")
        price = input("Enter price?")
        flightManager.create(flightno,takeofftime,takepoint,registrationNo,destination,landingtime,price)
        print("Congrate! your flight",flightno," is created successfully")

    elif suboption == '3':
        flightno = input("Enter Flight No? ")
        takeofftime = input("Enter takeoffTime? ")
        takepoint = input("Enter takepoint? ")
        registrationNo = input("Enter registartioNo ? ")
        destination = input("Enter your destination? ")
        landingtime = input("Enter landing time? ")
        price = input("Enter price?")
        flightManager.update(flightno,takeofftime,takepoint,registrationNo,destination,landingtime,price)
        print(flightno," is update.")

    else:
        flightno = input("Enter Flight No? ")
        flightManager.delete(flightno)
        print(flightno,"is Deleted .")

    ShowSubMenu("2")

def HandleMAanageBookingAction(suboption):

    if suboption == '1':
        BookingManager.list()

    elif suboption == '2':
        name = input("Enter name? ")
        SitNumber = input("Enter SiteNumber? ")
        Price = input("Enter price? ")
        TypeOfFlight = input("Enter Type Of Flight?")
        TimeOfFlight = input("Enter Time of flight?")
        destination = input("Enter destination?")
        avalFlight = input("Enter the Flight number")
        PhoneNo = input("Enter the Phone number")
        BookingManager.create(destination,TimeOfFlight,TypeOfFlight,SitNumber,name,Price,avalFlight,PhoneNo)

        print("Congrate! your Booking",name," is created successfully")

    elif suboption == '3':
        fname = input("Enter name? ")
        SitNumber = input("Enter SiteNumber? ")
        Price = input("Enter price? ")
        TypeOfFlight = input("Enter Type Of Flight?")
        TimeOfFlight = input("Enter Time of flight?")
        destination = input("Enter destination?")
        avalFlight = input("Enter the Flight number")
        PhoneNo = input("Enter the Phone number")
        BookingManager.update(destination,TimeOfFlight,TypeOfFlight,SitNumber,fname,Price,avalFlight,PhoneNo)

        print("Information for ",fname," is update.")

    else:
        SitNumber = input("Enter SiteNumber? ")
        BookingManager.remove(SitNumber)
    ShowSubMenu("3")

def HandleMAanagePassengerAction(suboption):

    if suboption == '1':
        PassagerManager.list()

    elif suboption == '2':
        name = input("Enter Name of Passanger? ")
        age = input("Enter Passanger age? ")
        PhoneNo = input("Enter passangers Phone number? ")
        Email = input("Enter Email?")
        Street = input("Enter Street?")
        City = input("Enter City?")
        Country = input("Enter Country?")
        PassagerManager.create(name, age, PhoneNo, Email, Street, City, Country)
        print("Congrats!", name, "is a passanger on a flight")

    elif suboption == '3':
        name = input("Enter Name of Passanger? ")
        age = input("Enter Passanger age? ")
        PhoneNo = input("Enter passangers Phone number? ")
        Email = input("Enter Email?")
        Street = input("Enter Street?")
        City = input("Enter City?")
        Country = input("Enter Country?")
        PassagerManager.update(name,age,PhoneNo,Email,Street,City,Country)
        print(PhoneNo, "updated")

    else:
        PhoneNo = input("Enter passangers Phone number? ")
        PassagerManager.remove(PhoneNo)
    ShowSubMenu("4")


def main():
    Flag=True
    while Flag:
        MainMenu()
        option=input()
        if option == '0':
            Flag=False
        else:
            ShowSubMenu(option)

if __name__ == '__main__':
    main()