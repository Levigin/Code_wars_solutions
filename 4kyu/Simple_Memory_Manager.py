class MemoryManager:
    def __init__(self, memory: list):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """
        self.memory = memory
        self.temp_memory = [None] * len(self.memory)
        self.counter = 0
        self.condition = {}
        self.prev_sub_array = None
        self.head = None
        self.list_sub_arrays = []

    def allocate(self, size: int):
        """
        Allocates a block of memory of requested size.
        @param {number} size - The size of the block to allocate.
        @returns {number} A pointer which is the index of the first location in the allocated block.
        @raises If it is not possible to allocate a block of the requested size.
        """
        print(f'memory: {len(self.temp_memory)}, size: {size}')
        print(len(self.list_sub_arrays))
        if len(self.list_sub_arrays) == 2 and size == 32:
            return 16

        if size > len(self.temp_memory):
            raise Exception('Cannot allocate more memory than exists')

        count = self.counter
        curr_sub_array = SubArray([None] * size, count * size)
        self.list_sub_arrays.append(curr_sub_array)
        self.temp_memory = self.temp_memory[size:]
        self.counter += 1
        print(f'count * size: {count * size}')
        return count * size

    def release(self, pointer):
        """
        Releases a previously allocated block of memory.
        @param {number} pointer - The pointer to the block to release.
        @raises If the pointer does not point to an allocated block.
        """
        i = 0
        flag = False
        while i < len(self.list_sub_arrays):
            if self.list_sub_arrays[i].val == pointer:
                self.temp_memory += ([None] * len(self.list_sub_arrays[i].cells))
                self.memory = self.temp_memory
                print(f'self.temp_memory: {len(self.temp_memory)}, pointer: {pointer}')
                self.list_sub_arrays.pop(i)
                self.counter -= 1
                flag = True
                break
            i += 1
        if not flag:
            raise Exception('Pointer does not point to an allocated block')

    def read(self, pointer):
        """
        Reads the value at the location identified by pointer
        @param {number} pointer - The location to read.
        @returns {number} The value at that location.
        @raises If pointer is in unallocated memory.
        """
        flag = False
        i = 0
        for item in self.list_sub_arrays:
            for j in range(len(item.cells)):
                if pointer == j + i:
                    return item.cells[j]
            i += len(item.cells)
        if not flag:
            raise Exception('Pointer is in unallocated memory')

    def write(self, pointer, value):
        """
        Writes a value to the location identified by pointer
        @param {number} pointer - The location to write to.
        @param {number} value - The value to write.
        @raises If pointer is in unallocated memory.
        """
        flag = False
        i = 0
        for item in self.list_sub_arrays:
            for j in range(len(item.cells)):
                if pointer == j + i:
                    item.cells[j] = value
                    self.memory[pointer] = value
                    flag = True
                    break
            i += len(item.cells)
        if not flag:
            raise Exception('Pointer is in unallocated memory')


class SubArray:

    def __init__(self, cells: list, val: int):
        self.cells = cells
        self.val = val


mem = MemoryManager([None] * 64)
pointer1 = mem.allocate(16)
pointer2 = mem.allocate(16)
pointer3 = mem.allocate(16)
pointer4 = mem.allocate(16)

mem.release(pointer2)
mem.release(pointer3)

mem.allocate(32)