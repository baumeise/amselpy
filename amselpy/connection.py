class Connection():

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
    return self.local_address

  # Log into network
  def login(self, ssid, passphrase):
    self.get("/login?ssid=" + ssid + "&pass=" + passphrase);
