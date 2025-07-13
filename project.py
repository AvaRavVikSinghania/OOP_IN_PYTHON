import requests

#API :http://indianrailapi.com/api/v2/TrainSchedule/apikey/54850cd098d34640b904f668a51e9643/TrainNumber/<TrainNumber>/

class IRCTC:

    def __init__(self):
        user_input = input("""
        1. Enter 1 to check live train status
        2. Enter 2 to check PNR
        3. Enter 3 to check train schedule
                            """)
        if user_input == "1":
            print("Live Location")
        elif user_input == "2":
            print("Check PNR Status")
        else:
            self.train_schedule()

    def train_schedule(self):
        train_number = input("Enter the train no")
        self.fetch_data(train_number)

    def fetch_data(self,train_number):
        url = f"http://indianrailapi.com/api/v2/TrainSchedule/apikey/54850cd098d34640b904f668a51e9643/TrainNumber/{train_number}"
        data = requests.get(url)
        data = data.json()
        # print(data["route"])
        for station in data["Route"]:
            print(station["StationName"])
         

irctc =IRCTC()
