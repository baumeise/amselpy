import httplib

class Connection(object):

  def __init__(self, local_ip):
    self.local_ip = local_ip
    self.local_address = "amsel.local"

  # Set IP
  def use(self, newIP):
    self.local_ip = newIP
    print("Amsel CLI uses %s as IP" % self.local_ip)

  # Return IP
  def IP(self):
    print("Amsel CLI uses %s as IP" % self.local_ip)
    return self.local_ip

  # Return address
  def address(self):
    print("Amsel CLI uses %s as network address" % self.local_address)
    return amsel.local_address

  # Establish http connection to device
  def enableHTTPConnection(self):
    return httplib.HTTPConnection(self.local_ip)

  # Perform get request and return status
  def get(self, path):
    connection = self.enableHTTPConnection()
    connection.request("HEAD", path)
    response = connection.getresponse()
    return response
