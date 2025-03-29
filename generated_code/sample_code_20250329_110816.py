# Auto-generated by Gemma

```python
def prime_digits_count(n):
  count = 0
  for digit in str(n):
    if int(digit) > 1:
      if all(i % prime for i in prime_digits(int(digit))):
        count += 1
  return count

def prime_digits(num):
  if num <= 1:
    return []
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  if num < 10:
    return primes
  for i in primes:
    if num % i == 0:
      return primes
  return []
```