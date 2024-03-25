# Documentation: Forking Example

## Overview

This C program demonstrates the use of the `fork()` system call to create a new process, known as a child process, from an existing process, known as the parent process. The child process and the parent process each print a message to the standard output to indicate their respective identities.

## Usage

To compile and run the program:

```bash
gcc main.c -o read
./read
```
## Code Description
#### Header Files


`stdio.h`: Standard input-output operations.


`string.h`:String manipulation functions ( used in this example).


`stdlib.h`: Standard library functions like memory allocation (used in this example).


`unistd.h`: Provides access to POSIX system calls, including fork().


### main() Function
#### Parameters:

`argc`: Number of command-line arguments.


`argv[]`: Array of strings representing command-line arguments.


## Functionality:

Calls `fork()` to create a new process.

The parent process (`id > 0`) prints "Hello, world from main".

The child process (`id == 0`) prints "Hello, world from child".

**Return Value**: Exits with status 0.
## Example Output
When executed, the program produces output similar to the following:

```bash
Hello, world from main
Hello, world from child
```
