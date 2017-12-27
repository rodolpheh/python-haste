# python-haste

python-haste is a script and a module for python that allows one to send a text or a file to a remote haste server (think "pastebin stuff").

## Usage

### As a script

#### Command line help:

```
% haste.py --help                     
usage: haste.py [-h] [--raw] [--address ADDRESS] [--get key] [<file>]

Upload the content of a file to an hastebin server

positional arguments:
  <file>             The file to upload

optional arguments:
  -h, --help         show this help message and exit
  --raw              Return raw URL (default disabled)
  --address ADDRESS  Address of the hastebin server (with port if necessary)
  --get key          Get the raw content of an haste
```

#### Use in pipes:

```
cat /etc/fstab | haste.py
```

### As a python module

```python
from haste import Haste

newHaste = Haste.add("Text to send")
# newHaste now contains an Haste object
print(newHaste.data) # Returns the content of the haste
print(newHaste.address) # Returns the address of the haste
print(newHaste.raw) # Returns the address for the raw content of the haste
print(newHaste.key) # Returns the haste's key

oldHaste = Haste.get(newHaste.key)
# oldHaste now contains an Haste object. The content is the same as newHaste because we just retrieved the haste associated with newHaste's key
# etc, etc...
```
