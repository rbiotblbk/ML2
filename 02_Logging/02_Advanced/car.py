import logging 


logger = logging.getLogger()

 
class Car:

    def __init__(self) -> None:

        logger.info("A class Car instance is created")
        self.km_stand = 0



    def drive(self, km):
        logger.info("Drive method is called")
        self.km_stand += km
        print("The car is driving ")


    def __repr__(self):
        return f"My KM_Stand is: {self.km_stand}"