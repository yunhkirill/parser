# parser

## Пример использования:
```python
from parser import Parser

parser = Parser()
netlist, reports = parser.load_netlist_from_file("test.netlist")
parser.save_netlist_to_file("new.netlist", netlist)
```
