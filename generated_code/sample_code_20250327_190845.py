# Auto-generated by Gemma

```python
import random

def generate_random_passphrase(length=12):
  return "".join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))
```