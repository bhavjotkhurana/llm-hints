import time

def log_performance(task_name, start_time):
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{task_name} took {elapsed_time:.2f} seconds")
