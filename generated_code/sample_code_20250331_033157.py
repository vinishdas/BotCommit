# Auto-generated by Gemma

```python
import random

def unique_string_generator(length):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  return "".join(random.choice(alphabet) for _ in range(length))
```