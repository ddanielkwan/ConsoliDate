from modules.Data import Data
from ics import Calendar, Event
import os

class ICS(Data):
   def __init__(self, title, Events):
       super().__init__(title, Events)
       
   def writeICS(self, path):
       calendar = Calendar()
       for event in self.Events:
            e = Event()
            e.name = self.title +" - " +event.name
            e.begin = event.date
            e.make_all_day()
            calendar.events.add(e)
            calendar.events
       with open(path +"/"+ self.title, 'w') as f:
            f.write(str(calendar))
       f.close()
       return os.path.abspath(path+"\\"+self.title)
