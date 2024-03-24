# Documentation: Forking, Process IDs, and Waiting Example

## Overview

This C program demonstrates the use of the `fork()` system call to create a new process, obtaining process IDs (`PID` and `PPID`), and using `wait()` to wait for child processes to finish execution. The program prints the process ID (`PID`) and the parent process ID (`PPID`) of each process and waits for the child process to finish execution before continuing.

## Usage

To compile and run the program:

```bash
gcc process_pid.c -o read
./read
```
## Code Description
### Header Files
`stdio.h`: Standard input-output operations.
`stdlib.h`: Standard library functions like memory allocation.

`unistd.h`: Provides access to POSIX system calls, including fork(), sleep(), and getpid().

`string.h`: String manipulation functions (not used in this example).

`sys/wait.h`: Header file for wait() system call.
### main() Function
#### Parameters:

`argc`: Number of command-line arguments.(Not used in this example).

`argv[]`: Array of strings representing command-line arguments.
### Functionality:

Calls fork() to create a new process.
The child process (`id == 0`) sleeps for 1 second.

Both the parent and child processes print their process ID (PID) and parent process ID (PPID) using `getpid()` and `getppid()` functions.

The parent process waits for the child process to finish execution using the `wait()` system call.

If there are no child processes to wait for, it prints `"No children to wait for."`
**Return Value**: Exits with status 0.

### Example Output
When executed, the program produces output similar to the following:
```bash
The currentID is 559305  and the parentID is 532347
The currentID is 559306  and the parentID is 559305
No children to wait for
559306 finished execution
```