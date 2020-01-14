from Connection import Connection
from Lights import Lights
import time

class Amsel(Connection, Lights):
  
  # Constructor
  def __init__(self, local_ip="192.168.0.100"):
    Connection.__init__(self, local_ip)
    Skills.__init__(self)
    Lights.__init__(self)
    
  # Set amsel to sleep for a certain amount of time
  def sleep(self, duration=0):
    time.sleep(duration)

  # Standard return method
  def __str__(self):
    return "A warm 'Gruetzi!' from Amsel!"
