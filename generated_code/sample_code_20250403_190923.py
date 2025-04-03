# Auto-generated by Gemma

```python
def factor_median(numbers):
  sorted_numbers = sorted(numbers)
  length = len(sorted_numbers)
  median = sorted_numbers[length // 2]
  factor = 0
  for number in sorted_numbers:
    factor += 1 if number % median == 0 else 0
  return factor / length
```