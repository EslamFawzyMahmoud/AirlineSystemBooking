class Aircraft():

    def __init__(self,capacity,registrationNo,types,name):
        self.capacity=capacity
        self.registrationNo=registrationNo
        self.types=types
        self.name=name

    def parse(line:str):
        capacity,registrationNo,types,name=line.split("\n")
        capacity=int(capacity)
        return Aircraft(capacity,registrationNo,types,name)

    def __str__(self):
        return f"{self.capacity}\t\t{self.registrationNo}\t\t{self.types}\t\t{self.name}"
