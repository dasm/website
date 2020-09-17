Title: General Purpose Registers
Date: 2020-09-16
Category: Learning
Tags: learning, fundamentals, ptp

# Basics

There are 8 generic purpose registers:

Naming convention      | Name | Purpose
-|-|-
EAX | Accumulator   | Used in arithmetic operations
EBX | Base Pointer  | Used as a pointer to data
ECX | Counter       | Used in shift/rotate instructions and loops
EDX | Data           | Used in arithmetic operations and I/O
ESP | Stack Pointer | Pointer to the top of the stack
EBP | Base Pointer (Stack Base Pointer, Frame Pointer )| Pointer to the base of the stack
ESI | Source Index | Used as a pointer to a source in stream operation
EDI | Destination | Used as a pointer to a destination in stream operation

Additionally, exists *EIP* (Instruction Pointer) which controls the program execution. It contains the address of the **next** instruction to be exetucted (it tells the CPU where the next instruction is).

# Program Memory

Running process is usually organized in 2 sections: read-only and read/write.

* .text - address space where program's executable instructions is stored.
* .data - global and static variables which have pre-defined value and can be modified.
* BSS (Block Started by Symbol) - uninitialized data, is usually adjacent to .data segment. Contains all global and static variables which are initialized to zero or do not have specific explicit initialization in source code.
* Heap - area commonly begins at the end of BSS and .data segments. and grows to larger addresses from there. This area is managed by *malloc*, *realloc* and *free*. This area is shared by all threads, shared libraries, and dynamically loaded modules in a process.
* Stack - typically located in the higher parts of memory. ESP tracks the top of the stack.


Heap grows towards higher memory addresses. Stack grows towards lower memory addresses.

Lower address | .text | .data | BSS | Heap -> ... <- Stack | Higher address

## Stack

The Stack is Last-in First-out (**LIFO**). It is array for saving addresses, passing function arguments, and storing local variables.
There are two operations *PUSH/POP* to work with stack. With each operation, *ESP* is updated. Because stack grows towards lower addresses of memory, when we *PUSH* something on stack, stack pointer is reduced `ESP-4` (-4 for 32 bits, -8 for 64 bits). When we remove something from stack by *POP*ing it, ESP changes address again `ESP+4`.

*PUSH*ed data is written to the stack memory, and later ESP address is updated `ESP-4`.
*POP*ped data is read from the stack and written to given register `POP EAX`

Values *POP*ed from stack are not deleted/removed. They stay in stack until another instruction overwrites it.

## Additional resources:

* [GPR naming - WikiBooks](https://en.wikibooks.org/wiki/X86_Assembly/X86_Architecture#General-Purpose_Registers_(GPR)_-_16-bit_naming_conventions)
* [Data segment - Wikipedia](https://en.wikipedia.org/wiki/Data_segment)
* [Call stack - Wikipedia](https://en.wikipedia.org/wiki/Call_stack)
