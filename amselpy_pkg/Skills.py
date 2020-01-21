class Skills():

  def __init__(self, speed=100):
    self.speed = speed

  # Set new default speed
  def setSpeed(self, newSpeed):
    self.speed = newSpeed
    print("Amsel CLI uses now %s as default speed" % self.speed)

  # Define movement functions
  def forward(self, speed=self.speed):
    endpoint = "/forward?speed=%s" % speed
    response = self.get(endpoint)
    print(response.status)

  def backward(self, speed=self.speed):
    endpoint = "/reverse?speed=%s" % speed
    response = self.get(endpoint)
    print(response.status)

  def left(self, speed=self.speed):
    endpoint = "/left?speed=%s" % speed
    response = self.get(endpoint)
    print(response.status)

  def right(self, speed=self.speed):
    endpoint = "/right?speed=%s" % speed
    response = self.get(endpoint)
    print(response.status)

  # Stop movement
  def stop(self):
    endpoint = "/stop"
    response = self.get(endpoint)
    print(response.status)

  # Set amsel to sleep for a certain amount of time
  def sleep(self, duration=0):
    time.sleep(duration)
