# Auto-generated by Gemma

```python
import secrets

def generate_random_hex_id():
  return ''.join(secrets.choice('abcdef0123456789') for _ in range(16))
```