# Documentation: File Copy Program

## Overview

This C program copies the contents of one file to another file. It opens the source file for reading and the destination file for writing. It then reads data from the source file in chunks and writes it to the destination file until the entire source file is copied.

## Usage

To compile and run the program:

```bash
gcc file_copy.c -o file_copy
./file_copy source_file destination_file
```

Replace `source_file` with the path to the file you want to copy from, and `destination_file` with the path where you want to copy the file to.

## Code Description

### Header Files

`stdio.h`: Standard input-output operations

`fcntl.h`: File control options (used for file manipulation).

`errno.h`: Header file for error handling.

`stdlib.h`: Standard library functions like memory allocation.

`unistd.h`: Provides access to POSIX system calls, including file I/O.

### main() Function

#### Parameter

`argc`: Number of command-line arguments.
`argv[]`: Array of strings representing command-line arguments.
Functionality:

Opens the source file specified in `argv[1]` for reading (`O_RDONLY`).

Checks if the source file was opened successfully. If not, it prints an error message and exits.

Opens the destination file specified in `argv[2]` for writing (`O_WRONLY|O_CREAT|O_EXCL`).

Checks if the destination file was opened successfully. If not, it prints an error message and exits.

Reads data from the source file in chunks and writes it to the destination file until the end of the file is reached.

Closes both the source and destination files.

**Return Value**: Exits with status 0 on successful execution, and non-zero status on error.

## Example Output

```bash
┌──(algebra㉿kali)-[~/Documents/units/Sem_2.2_Units/comp225]
└─$ cat file1    
Chelsea
Arsenal
Man united
Man CITY
Liverpool
  
                                                                                                                                                                       
┌──(algebra㉿kali)-[~/Documents/units/Sem_2.2_Units/comp225]
└─$ ./file_copy.c file1  file2
Successful opened the source file
successful opened the destination file
                                                                                                                                                                       
┌──(algebra㉿kali)-[~/Documents/units/Sem_2.2_Units/comp225]
└─$ cat file2 
Chelsea
Arsenal
Man united
Man CITY
Liverpool

```
