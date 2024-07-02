The `sys` module in Python provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. Here are examples of various functions in the `sys` module along with basic, complex, and real-life examples:

### 1. `sys.argv`
- **Basic Example:**
  ```python
  import sys

  print(sys.argv)
  ```
  This prints the list of command-line arguments passed to a script.

- **Complex Example:**
  ```python
  import sys

  if len(sys.argv) != 3:
      print("Usage: script.py <input_file> <output_file>")
      sys.exit(1)

  input_file = sys.argv[1]
  output_file = sys.argv[2]
  print(f"Reading from {input_file} and writing to {output_file}")
  ```

- **Real-Life Example:**
  Command-line tools like a script that reads a log file and outputs filtered data to another file:
  ```python
  import sys

  if len(sys.argv) < 2:
      print("Usage: python script.py <log_file>")
      sys.exit(1)

  log_file = sys.argv[1]
  with open(log_file, 'r') as file:
      for line in file:
          if 'ERROR' in line:
              print(line.strip())
  ```

### 2. `sys.exit`
- **Basic Example:**
  ```python
  import sys

  sys.exit()
  ```

- **Complex Example:**
  ```python
  import sys

  def process_data():
      if error_occurred:
          print("An error occurred!")
          sys.exit(1)

  process_data()
  ```

- **Real-Life Example:**
  A script that exits with a specific code to indicate success or failure, useful in CI/CD pipelines:
  ```python
  import sys

  def main():
      if not perform_checks():
          print("Checks failed!")
          sys.exit(1)
      print("All checks passed.")
      sys.exit(0)

  main()
  ```

### 3. `sys.platform`
- **Basic Example:**
  ```python
  import sys

  print(sys.platform)
  ```

- **Complex Example:**
  ```python
  import sys

  if sys.platform.startswith('win'):
      print("Running on Windows.")
  elif sys.platform.startswith('linux'):
      print("Running on Linux.")
  else:
      print("Unknown platform.")
  ```

- **Real-Life Example:**
  Cross-platform compatibility script:
  ```python
  import sys

  if sys.platform == "win32":
      import os
      os.system("cls")
  elif sys.platform == "linux" or sys.platform == "darwin":
      import os
      os.system("clear")
  ```

### 4. `sys.path`
- **Basic Example:**
  ```python
  import sys

  print(sys.path)
  ```

- **Complex Example:**
  ```python
  import sys

  sys.path.append('/path/to/my/module')
  import my_module
  ```

- **Real-Life Example:**
  Dynamically adding a library path in a production script:
  ```python
  import sys
  import os

  current_dir = os.path.dirname(os.path.abspath(__file__))
  lib_dir = os.path.join(current_dir, 'libs')
  sys.path.append(lib_dir)

  import my_library
  ```

### 5. `sys.stdin`, `sys.stdout`, `sys.stderr`
- **Basic Example:**
  ```python
  import sys

  print("This is standard output", file=sys.stdout)
  print("This is an error message", file=sys.stderr)
  ```

- **Complex Example:**
  ```python
  import sys

  original_stdout = sys.stdout
  with open('output.txt', 'w') as f:
      sys.stdout = f
      print("This will be written to output.txt")
      sys.stdout = original_stdout
  ```

- **Real-Life Example:**
  Logging to a file while maintaining console output:
  ```python
  import sys

  class Logger:
      def __init__(self, file_name):
          self.terminal = sys.stdout
          self.log = open(file_name, "a")

      def write(self, message):
          self.terminal.write(message)
          self.log.write(message)

      def flush(self):
          self.terminal.flush()
          self.log.flush()

  sys.stdout = Logger("output.log")

  print("This will be logged and printed to the console.")
  ```

### 6. `sys.getsizeof`
- **Basic Example:**
  ```python
  import sys

  variable = "Hello, World!"
  print(sys.getsizeof(variable))
  ```

- **Complex Example:**
  ```python
  import sys

  data = [i for i in range(1000)]
  size = sys.getsizeof(data)
  for item in data:
      size += sys.getsizeof(item)
  print(f"Total size of the list: {size} bytes")
  ```

- **Real-Life Example:**
  Profiling memory usage of a data structure in a large-scale application:
  ```python
  import sys

  def get_total_size(obj):
      seen = set()
      total_size = 0

      def sizeof_recursive(o):
          nonlocal total_size
          if id(o) in seen:
              return
          seen.add(id(o))
          total_size += sys.getsizeof(o)

          if isinstance(o, dict):
              for k, v in o.items():
                  sizeof_recursive(k)
                  sizeof_recursive(v)
          elif hasattr(o, '__dict__'):
              sizeof_recursive(o.__dict__)
          elif hasattr(o, '__iter__') and not isinstance(o, (str, bytes, bytearray)):
              for i in o:
                  sizeof_recursive(i)

      sizeof_recursive(obj)
      return total_size

  my_data = {'key': [1, 2, 3, 4], 'value': (5, 6, 7)}
  print(f"Total memory usage: {get_total_size(my_data)} bytes")
  ```

### 7. `sys.version`
- **Basic Example:**
  ```python
  import sys

  print(sys.version)
  ```

- **Complex Example:**
  ```python
  import sys

  version_info = sys.version_info
  if version_info.major < 3:
      print("Python 3 is required!")
      sys.exit(1)
  ```

- **Real-Life Example:**
  Ensuring a script runs with the correct Python version:
  ```python
  import sys

  required_version = (3, 6)
  if sys.version_info < required_version:
      print(f"Python {required_version[0]}.{required_version[1]} or higher is required.")
      sys.exit(1)
  ```

### 8. `sys.modules`
- **Basic Example:**
  ```python
  import sys

  print(sys.modules)
  ```

- **Complex Example:**
  ```python
  import sys

  if 'os' in sys.modules:
      print("os module is already imported")
  ```

- **Real-Life Example:**
  Replacing a module with a mock for testing:
  ```python
  import sys
  from unittest.mock import MagicMock

  original_os = sys.modules['os']
  sys.modules['os'] = MagicMock()

  import os
  os.path.join("a", "b")  # This will use the mock

  sys.modules['os'] = original_os  # Restore the original module
  ```

These examples cover a range of basic, complex, and real-life uses of various functions in the `sys` module.