from Connection import Connection
import time

class Amsel(Connection, Skills):
  
  # Constructor
  def __init__(self, local_ip="192.168.0.100"):
    Connection.__init__(self, local_ip)
    Skills.__init__(self)

  # Standard return method
  def __str__(self):
    return "A warm 'Griaß di!' from Amsel!"
