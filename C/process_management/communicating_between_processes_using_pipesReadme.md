# Documentation: Pipe Communication Example

## Overview

This C program demonstrates the use of pipes for inter-process communication (IPC) between a parent process and its child process. The parent process sends data to the child process through the pipe, and the child process receives and processes the data.

## Usage

To compile and run the program:

```bash
gcc communicating_between_processes_using_pipes.c -o pipe_output
./pipe_output
```

## Code Description

### Header Files

`stdio.h`: Standard input-output operations.

`unistd.h`: Provides access to POSIX system calls, including `fork()` and `pipe()`.

`stdlib.h`: Standard library functions like memory allocation.

## main() Function

### Functionality

Creates a pipe using the `pipe()` system call, which returns two file descriptors representing the `read` and `write` ends of the pipe.

Calls `fork()` to create a child process.

In the child process `(id == 0)`:
Closes the read end of the pipe using `close(fd[0])`.

Prompts the user to input a number.

Writes the input number to the pipe using `write(fd[1], &x, sizeof(int))`.

Closes the write end of the pipe using `close(fd[1])`.

In the parent process `(id > 0)`:

Closes the write end of the pipe using `close(fd[1])`.'

Reads data from the pipe into a variable using `read(fd[0], &y, sizeof(int))`.

Closes the read end of the pipe using `close(fd[0])`.

Prints the data received from the child process.

**Return Value**: Exits with status 0.

## Example Output

When executed

```bash
Input a number 
40
We got from the child process 40
```
