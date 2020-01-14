## AmselPy
The python package for the Amsel learning robot

### Usage
Clone this repository into your projects directory: 
``` shell
git clone git@github.com:baumeise/AmselPy.git
```
Start unsing it:
``` python
# import library
from amselpy import Amsel

# create instance
amsel = Amsel()

# set adress
amsel.use("<YOUR-AMSELS-IP>")

# control movements
amsel.forward()
amsel.sleep(5)
amsel.stop()
```
### Documentation
For further information read the [documentation](https://baumeise.github.io/amsel/docs).

### License
[MIT License](https://github.com/baumeise/amselpy/blob/master/LICENSE) | Copyright © 2019 Moritz Gut (moritzgvt)
