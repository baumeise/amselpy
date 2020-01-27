import time
import random

class Skills():

  def __init__(self, speed=100):
    self.speed = speed

  # Define movement functions.for
  def forward(self, speed=0):
    if not speed: speed = self.speed
    endpoint = "/forward?speed=%s" % speed
    response = self.get(endpoint)

  def backward(self, speed=0):
    if not speed: speed = self.speed
    endpoint = "/reverse?speed=%s" % speed
    response = self.get(endpoint)

  def left(self, speed=0):
    if not speed: speed = self.speed
    endpoint = "/left?speed=%s" % speed
    response = self.get(endpoint)

  def right(self, speed=0):
    if not speed: speed = self.speed
    endpoint = "/right?speed=%s" % speed
    response = self.get(endpoint)

  # Stop movement
  def stop(self):
    endpoint = "/stop"
    response = self.get(endpoint)
    print(response.status_code)

  # Infinite run with obsticle avoidance
  def go(self, speed=100, duration=-1, proximity=30):
    start = time.time()
    now = time.time()

    try:
      while (now - start) < duration or duration == -1:
        self.forward(speed)
        distance = self.getDistance()
        if distance:
          if int(distance) < int(proximity):
            obsticle = True
          else:
            obsticle = False

          if obsticle:
            self.stop()
            randomDirection = random.randint(0, 1)
            randomDuration = random.random()*1
            if randomDirection:
              self.right()
            else:
              self.left()
            self.sleep(randomDuration)
            self.stop()
        else:
          print("Miss")
        self.sleep(0.1)
        now = time.time()
    except KeyboardInterrupt:
      self.stop()
      print("Wow what a run!")
