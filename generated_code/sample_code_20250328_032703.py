# Auto-generated by Gemma

```python
import re

def remove_leader_trailing_zeros(string):
  return re.sub(r'(\d)\1{2,}', '', string)
```