#Threading in Python
#Single process has multiple threads of execution
#They share code, data and files but have different registers and stacks
#Threading is used to run multiple threads (tasks, function calls) at the same time
#Single core CPU is handling one thread at a time, but it can switch between threads to give the illusion of parallelism
#Multi-core CPU can run multiple threads in parallel

import threading 
from time import sleep, time

start_time = time() 
def something(id):
    print(f'Thread {id} starting')
    sleep(1)
    print(f'Thread {id} completed')

threads = [ threading.Thread(target=something, args=[i]) for i in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join() #Wait for all threads to complete.If we don't join the threads, the main thread will exit before the worker threads complete their tasks, which can lead to incomplete execution and unexpected behavior. By calling join() on each thread, we ensure that the main thread waits for all worker threads to finish before proceeding.

print(f'Total time taken: {time() - start_time:.2f} seconds')

#If we were running on single thread it would take 10 seconds to complete all tasks, but with threading it takes around 1 second because all threads are running concurrently.

balance = 200

def deposit(amount,times):
    global balance
    for _ in range(times):
        balance += amount


def withdraw(amount,times):
    global balance

    for _ in range(times):
        balance -= amount

deposit_thread = threading.Thread(target=deposit, args=[1, 100000])
withdraw_thread = threading.Thread(target=withdraw, args=[1, 100000])

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
print(f'Final balance: {balance}')

#In the balance example if we have multiple threads modifying the same balance variable without proper synchronization, we can end up with a race condition where the final balance is incorrect due to interleaving of thread execution(the system processes only one of the deposit or withdraw thread request). To prevent this, we can use a lock to ensure that only one thread can modify the balance at a time. This way, we can maintain the integrity of the balance variable and avoid race conditions. Here's an example of how to use a lock to synchronize access to the balance variable:

lock = threading.lock()

def deposit(amount,times,lock):
    global balance
    for _ in range(times):
        lock.acquire() #Acquire the lock before modifying the balance
        balance += amount #Critical section where the balance is modified, only one thread can execute this at a time
        lock.release() #Release the lock after modifying the balance


def withdraw(amount,times,lock):
    global balance

    for _ in range(times):
        lock.acquire() #Acquire the lock before modifying the balance
        balance -= amount #Critical section where the balance is modified, only one thread can execute this at a time
        lock.release() #Release the lock after modifying the balance

deposit_thread = threading.Thread(target=deposit, args=[1, 100000,lock])
withdraw_thread = threading.Thread(target=withdraw, args=[1, 100000,lock])

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
print(f'Final balance: {balance}')

#The above way is an old implementation. We now use Thread Pool Executor from concurrent.futures module which provides a high-level interface for asynchronously executing callables using threads. It abstracts away the low-level details of thread management and allows us to easily submit tasks to be executed in separate threads.

#Thread creation time is more than the context switching time, so for small tasks, using threads may not be efficient. However, for I/O-bound tasks or tasks that involve waiting (like network requests), threading can help improve performance by allowing other threads to run while one thread is waiting.

#The number of threads is manually defined, and we need to manage the threads ourselves (starting, joining, etc.). This can lead to issues like race conditions if not handled properly. In contrast, using a thread pool can help manage the threads more efficiently and reduce the chances of race conditions. Additionally, thread pools can help improve performance by reusing threads for multiple tasks, reducing the overhead of thread creation and destruction.

#Threads are not reusable, once a thread has completed its task, it cannot be restarted. If we need to perform another task, we would need to create a new thread. This can lead to increased overhead if we need to perform many tasks in quick succession. In contrast, using a thread pool allows us to reuse threads for multiple tasks, which can help improve performance and reduce overhead.

#We create a pool of threads where they sit as workers waiting for tasks to be assigned to them. When a task is submitted to the thread pool, it is added to a queue, and one of the worker threads picks it up and executes it. Once the task is completed, the worker thread goes back to waiting for the next task. This allows us to efficiently manage a large number of tasks without having to create and manage individual threads for each task.

from concurrent.futures import ThreadPoolExecutor,as_completed

def something(id):
    print(f'Thread {id} starting')
    sleep(1)
    print(f'Thread {id} completed')

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(something, i) for i in range(10)]
    for future in as_completed(futures):
        future.result() #Wait for each future to complete and get the result. This returns us the result irrespective of the order in which the tasks were submitted. The as_completed function returns an iterator that yields futures as they complete, allowing us to process the results as soon as they are available.

#The main thread will wait for all the worker threads to complete their tasks before proceeding, ensuring that all tasks are completed before the program exits.

#Using map function with ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(something, range(10)) #The map function will block until all tasks are completed, so we don't need to call future.result() for each task.
    for result in results:
        print(result) #The map function returns an iterator that yields the results of the tasks in the order they were submitted, so we can simply iterate over the results to get the output of each task.