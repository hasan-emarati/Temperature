import datetime
import numpy as np
class Data_Frame():
    def __init__(self):
        self.Dataframe = ""
        
    def Date_Time(self):
        # print(self.Dataframe)
        start_date = datetime.datetime(2022, 1, 1, 0, 0, 0)
        end_date = start_date + datetime.timedelta(days=365)
        current_time = start_date

        while current_time < end_date:
            self.DataFrame = current_time.strftime("%Y-%m-%d %H:%M:%S,")
            print (self.DataFrame)
            current_time += datetime.timedelta(hours=1)

    def temperature(self):
        return 

if __name__ == '__main__':
    Run = Data_Frame()
    Run.Date_Time()
    # Run.temperature()