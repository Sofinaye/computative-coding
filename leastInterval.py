def leastInterval(self, tasks, n):
      task_counts = Counter(tasks)
      freq = max(task_counts.values())
      task = sum(1 for count in task_counts.values() if count == freq)
      intervals = (freq - 1) * (n + 1) + task
      
      return max(intervals, len(tasks))
