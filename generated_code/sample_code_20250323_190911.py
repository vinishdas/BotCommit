# Auto-generated by Gemma

```python
def find_longest_substring_containing_exactly_one_duplicate(s):
  n = len(s)
  if n <= 1:
    return ""
  
  start = 0
  max_length = 0
  seen = set()
  
  for i in range(n):
    if s[i] in seen:
      continue
    
    if i - start + 1 > max_length:
      max_length = i - start + 1
    
    seen.add(s[i])
      
  return s[start:start + max_length]
```