# Documentation: Waiting for process to finish

## Overview

This C program demonstrates the use of the `fork()` system call to create a new process, known as a child process, from an existing process, known as the parent process.Where we use the wait function to wait for the child process to complete then the parent process will procced

## Usage

To compile and run the program:

```bash
gcc Process_wait.c -o read
./read
```

## Code Description

### Header Files

`stdio.h`: Standard input-output operations.
`stdlib.h`: Standard library functions like memory allocation.

`unistd.h`: Provides access to POSIX system calls, including fork().

`time.h`: Provides functions for measuring time (used in this example).

### Functionality

Calls `fork()` to create a new process.

The parent process assigns `n` a value of `6`, while the child process assigns `n` a value of `1`.

The parent process waits for the child process to finish execution.

Both the parent and child processes print a sequence of five numbers to the standard output, starting from the assigned value of `n`.

**Return Value**: Exits with status 0.

## Example Output

When executed, the program produces output similar to the following:

```bash
6 7 8 9 10
1 2 3 4 5
```
