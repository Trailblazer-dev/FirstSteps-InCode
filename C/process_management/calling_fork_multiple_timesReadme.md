# Documentation: Forking Multiple Processes and Waiting Example

## Overview

This C program demonstrates the use of the `fork()` system call to create multiple child processes and waits for all child processes to finish execution. Each process prints a message to indicate its identity, and the parent process waits for the termination of all child processes using the `wait()` system call.

## Usage

To compile and run the program:

```bash
gcc calling_fork_multiple_times.c -o read
./read
```

## Code Description

### Header Files

`stdio.h`: Standard input-output operations.

`string.h`: String manipulation functions (not used in this example).

`unistd.h`: Provides access to POSIX system calls, including fork().

`stdlib.h`: Standard library functions like memory allocation.
`sys/wait.h`: Header file for wait() system call.
`errno.h`: Header file for error handling.

## main() Function

### Parameters

`argc`: Number of command-line arguments.
`argv[]`: Array of strings representing command-line arguments.

### Functionality

Calls `fork()` twice to create multiple child processes (`y, x, and z`) from the parent process.

Each child process prints a message to indicate its identity.

The parent process waits for the termination of all child processes using the `wait()` system call in a loop.

The loop continues until there are no more child processes left to wait for.
**Return Value**: Exits with status 0.

## Example Output

When executed, the program produces output similar to the following:

```bash
We are process x
We are process y
we are the parent process 
We are process z
Waited for the child process to finish
Waited for the child process to finish
Waited for the child process to finish
Waited for the child process to finish
