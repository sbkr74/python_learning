The `os` module in Python provides a way of using operating system-dependent functionality like reading or writing to the file system. Below, I'll provide examples for some of the most commonly used functions, including basic, complex, and real-life scenarios:

### 1. `os.getcwd()`
Gets the current working directory.

- **Basic Example**:
  ```python
  import os
  print(os.getcwd())
  ```

- **Complex Example**:
  ```python
  import os
  def print_current_directory():
      current_directory = os.getcwd()
      print(f"Current directory: {current_directory}")

  print_current_directory()
  ```

- **Real-life Example**:
  ```python
  import os
  def log_current_directory():
      current_directory = os.getcwd()
      with open('log.txt', 'a') as log_file:
          log_file.write(f"Checked current directory: {current_directory}\n")

  log_current_directory()
  ```

### 2. `os.chdir()`
Changes the current working directory.

- **Basic Example**:
  ```python
  import os
  os.chdir('/path/to/new/directory')
  print(os.getcwd())
  ```

- **Complex Example**:
  ```python
  import os
  def change_directory(path):
      try:
          os.chdir(path)
          print(f"Changed directory to: {os.getcwd()}")
      except FileNotFoundError:
          print(f"Directory not found: {path}")

  change_directory('/path/to/new/directory')
  ```

- **Real-life Example**:
  ```python
  import os
  def change_directory_and_list_files(path):
      try:
          os.chdir(path)
          print(f"Files in {os.getcwd()}: {os.listdir()}")
      except FileNotFoundError:
          print(f"Directory not found: {path}")

  change_directory_and_list_files('/path/to/new/directory')
  ```

### 3. `os.listdir()`
Lists all files and directories in the specified directory.

- **Basic Example**:
  ```python
  import os
  print(os.listdir('.'))
  ```

- **Complex Example**:
  ```python
  import os
  def list_files(directory):
      try:
          files = os.listdir(directory)
          for file in files:
              print(file)
      except FileNotFoundError:
          print(f"Directory not found: {directory}")

  list_files('.')
  ```

- **Real-life Example**:
  ```python
  import os
  def list_python_files(directory):
      try:
          files = os.listdir(directory)
          python_files = [file for file in files if file.endswith('.py')]
          for python_file in python_files:
              print(python_file)
      except FileNotFoundError:
          print(f"Directory not found: {directory}")

  list_python_files('.')
  ```

### 4. `os.mkdir()`
Creates a new directory.

- **Basic Example**:
  ```python
  import os
  os.mkdir('new_directory')
  ```

- **Complex Example**:
  ```python
  import os
  def create_directory(directory):
      try:
          os.mkdir(directory)
          print(f"Directory created: {directory}")
      except FileExistsError:
          print(f"Directory already exists: {directory}")

  create_directory('new_directory')
  ```

- **Real-life Example**:
  ```python
  import os
  def create_project_structure(project_name):
      try:
          os.mkdir(project_name)
          os.mkdir(os.path.join(project_name, 'src'))
          os.mkdir(os.path.join(project_name, 'tests'))
          print(f"Project structure created for {project_name}")
      except FileExistsError:
          print(f"Project {project_name} already exists")

  create_project_structure('my_project')
  ```

### 5. `os.remove()`
Removes a file.

- **Basic Example**:
  ```python
  import os
  os.remove('file_to_remove.txt')
  ```

- **Complex Example**:
  ```python
  import os
  def remove_file(file_path):
      try:
          os.remove(file_path)
          print(f"File removed: {file_path}")
      except FileNotFoundError:
          print(f"File not found: {file_path}")

  remove_file('file_to_remove.txt')
  ```

- **Real-life Example**:
  ```python
  import os
  def remove_temp_files(directory):
      try:
          files = os.listdir(directory)
          temp_files = [file for file in files if file.endswith('.tmp')]
          for temp_file in temp_files:
              os.remove(os.path.join(directory, temp_file))
              print(f"Removed temporary file: {temp_file}")
      except FileNotFoundError:
          print(f"Directory not found: {directory}")

  remove_temp_files('.')
  ```

### 6. `os.rmdir()`
Removes an empty directory.

- **Basic Example**:
  ```python
  import os
  os.rmdir('empty_directory')
  ```

- **Complex Example**:
  ```python
  import os
  def remove_empty_directory(directory):
      try:
          os.rmdir(directory)
          print(f"Directory removed: {directory}")
      except FileNotFoundError:
          print(f"Directory not found: {directory}")
      except OSError:
          print(f"Directory not empty: {directory}")

  remove_empty_directory('empty_directory')
  ```

- **Real-life Example**:
  ```python
  import os
  def cleanup_empty_directories(directory):
      try:
          subdirectories = [os.path.join(directory, d) for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
          for subdir in subdirectories:
              try:
                  os.rmdir(subdir)
                  print(f"Removed empty directory: {subdir}")
              except OSError:
                  continue
      except FileNotFoundError:
          print(f"Directory not found: {directory}")

  cleanup_empty_directories('.')
  ```

### 7. `os.rename()`
Renames a file or directory.

- **Basic Example**:
  ```python
  import os
  os.rename('old_name.txt', 'new_name.txt')
  ```

- **Complex Example**:
  ```python
  import os
  def rename_file(old_name, new_name):
      try:
          os.rename(old_name, new_name)
          print(f"Renamed {old_name} to {new_name}")
      except FileNotFoundError:
          print(f"File not found: {old_name}")

  rename_file('old_name.txt', 'new_name.txt')
  ```

- **Real-life Example**:
  ```python
  import os
  def batch_rename_files(directory, old_extension, new_extension):
      try:
          files = os.listdir(directory)
          for file in files:
              if file.endswith(old_extension):
                  new_name = file.replace(old_extension, new_extension)
                  os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
                  print(f"Renamed {file} to {new_name}")
      except FileNotFoundError:
          print(f"Directory not found: {directory}")

  batch_rename_files('.', '.txt', '.md')
  ```

### 8. `os.stat()`
Gets the status of a file or directory.

- **Basic Example**:
  ```python
  import os
  file_status = os.stat('file.txt')
  print(file_status)
  ```

- **Complex Example**:
  ```python
  import os
  def print_file_status(file_path):
      try:
          status = os.stat(file_path)
          print(f"File status for {file_path}: {status}")
      except FileNotFoundError:
          print(f"File not found: {file_path}")

  print_file_status('file.txt')
  ```

- **Real-life Example**:
  ```python
  import os
  def log_file_sizes(directory):
      try:
          files = os.listdir(directory)
          with open('file_sizes.log', 'a') as log_file:
              for file in files:
                  if os.path.isfile(os.path.join(directory, file)):
                      size = os.stat(os.path.join(directory, file)).st_size
                      log_file.write(f"File: {file}, Size: {size} bytes\n")
      except FileNotFoundError:
          print(f"Directory not found: {directory}")

  log_file_sizes('.')
  ```

### 9. `os.path.join()`
Joins one or more path components intelligently.

- **Basic Example**:
  ```python
  import os
  path = os.path.join('folder', 'subfolder', 'file.txt')
  print(path)
  ```

- **Complex Example**:
  ```python
  import os
  def create_path(*args):
      path = os.path.join(*args)
      print(f"Created path: {path}")

  create_path('folder', 'subfolder', 'file.txt')
  ```

- **Real-life Example**:
  ```python
  import os
  def create_project_file_path(project_name, file_name):
      return os.path.join('projects', project_name, 'files', file_name)

  project_path = create_project_file_path('my_project', 'README.md')
  print(f"Project file path: {project_path}")
  ```

### 10. `os.path.exists()`
Checks if a path exists.

- **Basic Example**:
  ```python
  import os
  print(os.path.exists('file.txt'))
  ```

- **Complex Example**:
  ```python
  import os
  def check_path_exists(path):
      if os.path.exists(path):
          print(f"Path exists: {path}")
      else

:
          print(f"Path does not exist: {path}")

  check_path_exists('file.txt')
  ```

- **Real-life Example**:
  ```python
  import os
  def ensure_directory_exists(directory):
      if not os.path.exists(directory):
          os.mkdir(directory)
          print(f"Directory created: {directory}")
      else:
          print(f"Directory already exists: {directory}")

  ensure_directory_exists('logs')
  ```

These are just a few examples of the many functions available in the `os` module. The `os` module is powerful and can handle a wide variety of tasks involving the file system and the operating system environment.