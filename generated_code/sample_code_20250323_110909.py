# Auto-generated by Gemma

```python
import random

def most_frequent_word(text):
  words = text.lower().split()
  frequency = {}
  for word in words:
    if word in frequency:
      frequency[word] += 1
    else:
      frequency[word] = 1
  return max(frequency, key=frequency.get)
```