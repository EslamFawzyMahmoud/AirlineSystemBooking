# from AircraftManager import AircraftMassenger
# from flightManager import FlightManager
# from BookingManager import Bookingmanager
# from passengerManager import passengerManager
#
# aircraftManager = AircraftMassenger()
# flightManager = FlightManager(aircraftManager)
# PassagerManager = passengerManager()
# BookingManager =Bookingmanager(flightManager,PassagerManager)
#
# def MainMenu():
#     print("Enter 0 to exit")
#     print("Enter 1 to Manage Aircraft")
#     print("Enter 2 to Manage ")
#     print("Enter 3 to Manage ")
#     print("Enter 4 to Manage ")
#
# def ShowSubMenu(option):
#     if option=='1':
#         ShowAircraftMenu()
#         suboption=input()
#         if suboption=='0':
#             MainMenu()
#         else:
#             pass
#     elif option =='2':
#         pass
#     elif option =='3':
#         pass
#     elif option == '4':
#         pass
#
# def ShowAircraftMenu():
#     print("Enter 0 to return MainMenu")
#     print("Enter 1 to List Aircraft")
#     print("Enter 2 to Create Aircraft")
#     print("Enter 3 to Update Aircraft")
#     print("Enter 4 to Delete Aircraft")
#
# def HandleMAanageAircraft(suboption):
#     if suboption == '1':
#         aircraftManager.list()
#     elif suboption == '2':
#
#         aircraftManager.create()
#     elif suboption == '3':
#         pass
#     else:
