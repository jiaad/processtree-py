# About The Project
- This project is a small program designed to visualize MacOS and Linux processes. It serves as a tiny version of the pstree utility, providing a hierarchical view of the processes.

## Requirements
- python

## Installation
- Clone the repo
   ```sh
    git clone https://github.com/jiaad/pstree-python
   ```

<!-- USAGE EXAMPLES -->
## Usage
```
  ps -a -x -o pid,ppid,comm | python3 ps.py
```

## Thoughts
    Initializes and prints the hierarchical process tree starting from the launchd process.

    1. Reads process data from standard input.
    2. Parses the data and constructs a tree of process objects.
    3. Handles any missing parent processes by creating placeholder nodes.
    4. Prints the process tree starting from the launchd process (PID 1) in a hierarchical format.

    - The data is represented like this:

  ```python
  data Process
    pid: string
    ppid: string
    childrens: Process[]
  
  ``` 
