class Lights():

  def __init__(self):
    self.led_state = 0
  
  # Turn LED on(1)/off(0)
  def LED(self, status):
    self.led_state = status
    path = "/led?state=%s" % self.led_state

    response = self.get(path)
    print(response.status)
