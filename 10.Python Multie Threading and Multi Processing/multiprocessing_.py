# Multiprocessing allows you to create processes that run in parallel

# CPU-Bound Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing)

# Parallel execution - Multiple cores of the CPU

import multiprocessing

import time


def square_numers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")


def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i**3}")


if __name__ == "__main__":

    # create 2 Processes

    p1 = multiprocessing.Process(target=square_numers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()
    # start the process
    p1.start()
    p2.start()

    # wait for process to complete
    p1.join()
    p2.join()

    finished_time = time.time()-t
    print(finished_time)
