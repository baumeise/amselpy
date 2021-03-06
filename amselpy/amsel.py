from .connection import Connection
from .skills import Skills
from .utils import Utils

class Amsel(Connection, Skills, Utils):
  
  # Constructor
  def __init__(self, local_ip="192.168.0.100", speed=100):
    Connection.__init__(self, local_ip)
    Skills.__init__(self, speed)

  # Standard return method
  def __str__(self):
    return "A warm 'Griass di!' from Amsel!"
