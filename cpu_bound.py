import asyncio
import concurrent.futures
import time


async def cpu_bound(number):
    return sum(i * i for i in range(number))


async def find_sums(numbers):
    tasks = []
    for number in numbers:
        tasks.append(cpu_bound(number))
    await asyncio.gather(*tasks)


def new_find_sums(number):
    return sum(i * i for i in range(number))


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(new_find_sums, numbers)
    #asyncio.run(find_sums(numbers))
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")