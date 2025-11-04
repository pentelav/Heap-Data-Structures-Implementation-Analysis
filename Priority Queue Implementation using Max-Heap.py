# Defines Priority Queue based on a Max-Heap data structure based on Python list.
# It is also used to schedule tasks by inserting, extracting and updating the priorities of tasks effectively.
# The operations in the heap such as the push and pop operations make sure that the task with the highest priority is always executed first.

class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        # Initializing a task with ID, priority, arrival time, and deadline
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        # Comparing tasks based on priority for heap ordering
        return self.priority < other.priority


class PriorityQueue:
    def __init__(self):
        # Initializing an empty list to represent the binary heap
        self.heap = []

    def insert(self, task):
        """
        Inserting a new task into the priority queue and restoring heap order
        """
        self.heap.append(task)  # Adding the new task at the end
        self._heapify_up(len(self.heap) - 1)  # Performing upward heapify

    def _heapify_up(self, index):
        """
        Restoring the heap property by moving the element upward
        """
        parent = (index - 1) // 2
        # Swapping until the heap property is satisfied
        while index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]  # Exchanging with parent
            index = parent  # Updating current index
            parent = (index - 1) // 2  # Moving to next parent

    def extract_max(self):
        """
        Removing and returning the task with the highest priority
        """
        if not self.heap:
            return None
        root = self.heap[0]  # Storing the highest-priority task
        self.heap[0] = self.heap[-1]  # Moving the last element to the root
        self.heap.pop()  # Removing the last element
        if self.heap:
            self._heapify_down(0)  # Performing downward heapify
        return root  # Returning the removed highest-priority task

    def _heapify_down(self, index):
        """
        Restoring the heap property by moving the element downward
        """
        size = len(self.heap)
        largest = index

        # Iteratively checking and swapping with larger child
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < size and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]  # Swapping nodes
            index = largest  # Updating index to continue checking below

    def increase_key(self, task_id, new_priority):
        """
        Increasing the priority of a given task and restoring heap order
        """
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority > task.priority:
                    task.priority = new_priority  # Updating task priority
                    self._heapify_up(i)  # Reordering the heap
                break

    def is_empty(self):
        """
        Checking if the priority queue is empty
        """
        return len(self.heap) == 0  # Returning True if heap has no elements

    def display(self):
        """
        Displaying all tasks currently in the priority queue
        """
        print("\nCurrent Priority Queue:")
        for task in self.heap:
            print(f"Task ID: {task.task_id}, Priority: {task.priority}, Arrival: {task.arrival_time}, Deadline: {task.deadline}")


# Example Usage
if __name__ == "__main__":
    pq = PriorityQueue()  # Creating a priority queue instance

    # Inserting tasks into the queue
    pq.insert(Task("T1", 3, "10:00", "12:00"))
    pq.insert(Task("T2", 5, "10:10", "11:30"))
    pq.insert(Task("T3", 1, "10:20", "13:00"))

    pq.display()  # Displaying all tasks

    # Extracting the task with the highest priority
    print("\nExtracted Task:")
    extracted = pq.extract_max()
    print(f"Task ID: {extracted.task_id}, Priority: {extracted.priority}")

    pq.display()  # Displaying remaining tasks

    # Increasing the priority of a task
    pq.increase_key("T3", 6)
    print("\nAfter Increasing Priority:")
    pq.display()

    # Checking if the priority queue is empty
    print("\nIs Priority Queue Empty?", pq.is_empty())
