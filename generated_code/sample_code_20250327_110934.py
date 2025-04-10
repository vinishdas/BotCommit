# Auto-generated by Gemma

```python
import random

def random_maze_generation(rows, cols):
  maze = [['#' for _ in range(cols)] for _ in range(rows)]
  def check_neighbours(x, y):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      nx, ny = x + dx, y + dy
      if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '#':
        return True
    return False
  
  def generate_cell(x, y):
    if random.random() < 0.5:
      maze[x][y] = ' '
    else:
      maze[x][y] = '#'

  for x in range(rows):
    for y in range(cols):
      generate_cell(x, y)
      if random.random() < 0.5 and check_neighbours(x, y):
        generate_cell(x, y)

  return maze 
```