send-carbon
===========

Simple class to send metrics to carbon-cache using the plaintext protocol.

Example:
```python
#!/usr/bin/python
from send_carbon import CarbonClient

carbon = CarbonClient('127.0.0.1', '2003')
carbon.sendcarbon('testhost.testvalue.test', float(3000))
```
