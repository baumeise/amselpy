class Skills():

  def __init__(self, speed=100):
    self.speed = speed
    
    def setSpeed(self, newSpeed):
      self.speed = newSpeed
      print("Amsel CLI uses now %s as default speed" % self.speed)

    def forward(self, speed=self.speed):
      path = "/forward?speed=%s" % speed

      response = self.get(path)
      print(response.status)

    def backward(self, speed=self.speed):
      path = "/reverse?speed=%s" % speed

      response = self.get(path)
      print(response.status)

    def left(self, speed=self.speed):
      path = "/left?speed=%s" % speed

      response = self.get(path)
      print(response.status)

    def right(self, speed=self.speed):
      path = "/right?speed=%s" % speed

      response = self.get(path)
      print(response.status)