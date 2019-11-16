## AmselPy
The python package for the Amsel learning robot

### Usage
Clone this repository into your projects directory: 
``` shell
git clone git@github.com:moritzgvt/AmselPy.git
```
Start unsing it:
``` python
# import library
from amselpy import Amsel

# create instance
amsel = Amsel()

# set request adress
amsel.use("192.168.0.100")

# control movements
amsel.forward()
amsel.sleep(5)
amsel.stop()
```
### Documentation
For further information read the [documentation](https://moritzgvt.github.io/amsel/docs).

### License
MIT Licensed | Copyright 2019 © Moritz Gut (moritzgvt)
