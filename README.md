# Prueba de concepto

> Python 3.6+

```
pip install kewer
```

Lanzar wordcount
```
python launch.py wordcount.py WordCount
```

Lanzar count
```
python launch.py count.py Count
```


Esqueleto de un script
```python
from kewer import Kernel, Drawer
 
 
class MyScript(Kernel):
 
    def setup(self):
        pass
 
    def transform(self, value):
        pass
 
    def finish(self):
        drawer = Drawer()
        return drawer
```
