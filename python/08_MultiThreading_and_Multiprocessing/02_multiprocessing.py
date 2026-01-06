## Processess that runs in parallel
## When to use
## CPU bound tasks (e.g. mathematical compution, or data processing)
## Parallel execution- Multiple cores of CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i*i*i}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    start = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Finished in {time.time() - start:.2f} seconds")


# You are on Windows.

# On Windows, multiprocessing uses spawn, not fork.

# That means:

# Every new process re-imports your Python file from the top.

# Because your process-creation code is at top level, this happens:

# Python starts the script

# p1.start() is executed

# A new process is spawned

# The new process re-runs the entire file

# It again reaches p1.start()

# Infinite spawning → 💥 RuntimeError

# Python stops you to prevent your system from exploding.

# ✅ The correct fix (THIS IS MANDATORY)

# Wrap process creation and .start() calls inside:

# if __name__ == "__main__":

    # On Windows:

    # New process imports your script

    # Code outside if __name__ == "__main__" runs again

    # That causes recursive process creation

    # if __name__ == "__main__" means:

    # “Only run this code when this file is executed directly — NOT when imported.”

    # Child processes import, they don’t execute directly.

    # So they skip the process-creation block.