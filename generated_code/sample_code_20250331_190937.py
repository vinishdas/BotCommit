# Auto-generated by Gemma

```python
import random

def generate_random_passphrase(length=12):
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
  passphrase = ''.join(random.choices(characters, k=length))
  return passphrase
```