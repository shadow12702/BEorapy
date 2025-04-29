from concurrent.futures import ThreadPoolExecutor, as_completed


class MultiThreads:
    def __init__(self, max_threads:int = 8):        
        self.max_threads = max_threads

    def execute(self, tasks, callback=None):
        total_tasks = len(tasks)
        completed_tasks = 0

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            future_to_task = {
                executor.submit(func, *args, **kwargs): (func, args)
                for func, args, kwargs in tasks
            }

            for future in as_completed(future_to_task):
                func, _ = future_to_task[future]
                try:
                    result = future.result()
                    if callback:
                        callback(func.__name__, result)
                except Exception as e:                    
                    if callback:
                        callback(func.__name__, f"Error: {e}")
                
                completed_tasks += 1
                progress_percentage = (completed_tasks / total_tasks) * 100
                print(f"Progress: {progress_percentage:.2f}% - Completed task: {func.__name__}")

    def run_tasks(self, tasks_with_args, callback=None):
        """
        Executes the given tasks concurrently.
        
        :param tasks_with_args: List of tuples where each tuple contains a function and its arguments.
        :param callback: Optional callback function to process results.
        :return: Dictionary of task names to their results.
        """
        results = {}
        
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            futures = {
                executor.submit(func, *args): name for name, (func, args) in tasks_with_args.items()}
            
            for future in as_completed(futures):
                task_name = futures[future]
                try:
                    result = future.result()
                    results[task_name] = result
                    
                    # Invoke the callback if provided
                    if callback:
                        callback(task_name, result)
                
                except Exception as e:
                    print(f"Error in task {task_name}: {e}")
                    results[task_name] = None  # Or handle the error as needed

        return results