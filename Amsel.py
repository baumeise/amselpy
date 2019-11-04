from Connection import Connection
from Lights import Lights
import time

class Amsel(Connection, Lights):
  
  # Constructor
  def __init__(self, local_ip="192.168.0.100"):
    Connection.__init__(self, local_ip)
    Lights.__init__(self)
    

  # Set amsel to sleep for a certain amount of time
  def sleep(self, duration):
    time.sleep(duration)

  # Standard return method
  def __str__(self):
    return "Hello from Amsel!"
