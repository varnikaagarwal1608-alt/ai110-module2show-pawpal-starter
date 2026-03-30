from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date, timedelta
from itertools import combinations


# -------------------- Task --------------------
@dataclass
class Task:
    def __init__(self, name, duration, priority, frequency, pet=None, completed=False, time=None, due_date=None):
        self.name = name
        self.duration = duration
        self.priority = priority
        self.frequency = frequency
        self.pet = pet
        self.completed = completed
        self.time = time
        # if no due_date is provided, default to today
        self.due_date = due_date or date.today()

    def mark_complete(self):
        self.completed = True
        if self.frequency.lower() in ["daily", "weekly"]:
            next_date = self.due_date + timedelta(days=1 if self.frequency.lower() == "daily" else 7)
            new_task = Task(
                name=self.name,
                duration=self.duration,
                priority=self.priority,
                frequency=self.frequency,
                pet=self.pet,
                completed=False,
                time=self.time,
                due_date=next_date
            )
            if self.pet:
                self.pet.add_task(new_task)
    def update_task(self, name=None, duration=None, priority=None, frequency=None):
        """Update task details."""
        if name:
            self.name = name
        if duration:
            self.duration = duration
        if priority:
            self.priority = priority
        if frequency:
            self.frequency = frequency

  
    def get_details(self):
        """Return a summary of the task details."""
        return f"{self.name} ({self.priority}) - {self.duration} mins, Completed: {self.completed}"
    
    def is_recurring(self):
        """Check if task is recurring."""
        return self.frequency.lower() in ["daily", "weekly"]

# -------------------- Pet --------------------
@dataclass
class Pet:
    name: str
    type: str
    age: int
    special_needs: Optional[str] = None
    owner: Optional["Owner"] = None
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet and link the task back to the pet."""
        task.pet = self
        self.tasks.append(task)

    def get_tasks(self):
        """Return the list of tasks for this pet."""
        return self.tasks

    def update_info(self, name=None, type=None, age=None, special_needs=None):
        """Update pet information."""
        if name:
            self.name = name
        if type:
            self.type = type
        if age:
            self.age = age
        if special_needs:
            self.special_needs = special_needs
# -------------------- Owner --------------------
class Owner:
    def __init__(self, name: str, available_time: int, preferences: dict):
        self.name = name
        self.available_time = available_time
        self.preferences = preferences
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's list of pets."""
        pet.owner = self
        self.pets.append(pet)

    def update_preferences(self, preferences: dict):
        """Update the owner's preferences."""
        self.preferences = preferences

    def get_available_time(self):
        """Return the owner's available time for pet care."""
        return self.available_time

    def get_all_tasks(self):
        """Return all tasks from all pets."""
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks
# -------------------- Scheduler --------------------
class Scheduler:
    def __init__(self, owner: Owner):
        """Initialize the scheduler with an optional owner."""
        self.owner = owner
        self.daily_plan: List[Task] = []

    def sort_tasks_by_priority(self, tasks: List[Task]):
        """Sort tasks in descending order of priority: HIGH > MEDIUM > LOW."""
        priority_map = {"HIGH": 1, "MEDIUM": 2, "LOW": 3}
        return sorted(tasks, key=lambda t: (priority_map.get(t.priority.upper(), 4), t.time))

    def generate_schedule(self):
        """Generate the daily schedule based on owner's available time and task priority."""
        tasks = self.sort_tasks_by_priority(self.owner.get_all_tasks())
        remaining_time = self.owner.get_available_time()
        self.daily_plan = []

        for task in tasks:
            if task.duration <= remaining_time:
                self.daily_plan.append(task)
                remaining_time -= task.duration

    def check_constraints(self):
        """Add tasks to the daily plan respecting available time."""
        # Example: ensure total duration <= available time
        total_duration = sum(task.duration for task in self.daily_plan)
        return total_duration <= self.owner.get_available_time()

    def explain_plan(self):
        """Return a readable summary of today's schedule."""
        explanation = "Today's schedule:\n"
        for task in self.daily_plan:
            explanation += f"- {task.get_details()} for pet {task.pet.name}\n"
        return explanation

    def sort_by_time(self):
        """Sort tasks by time in HH:MM format."""
        self.tasks_list.sort(key=lambda t: t.time)

    def filter_by_pet(self, pet_name):
        """Return tasks for a specific pet."""
        return [t for t in self.tasks_list if t.pet and t.pet.name == pet_name]

    def filter_completed(self, completed=True):
        """Return tasks based on completion status."""
        return [t for t in self.tasks_list if t.completed == completed]

    def detect_conflicts(self):
        """Detect scheduling conflicts based on overlapping times and return list of conflicting task pairs."""
        def time_to_minutes(t: str) -> int:
            h, m = map(int, t.split(':'))
            return h * 60 + m
        
        tasks = self.daily_plan  # Check conflicts in the daily plan
        conflicts = []
        for t1, t2 in combinations(tasks, 2):
            start1 = time_to_minutes(t1.time)
            end1 = start1 + t1.duration
            start2 = time_to_minutes(t2.time)
            end2 = start2 + t2.duration
            if start1 < end2 and start2 < end1:
                conflicts.append((t1, t2))
        
        return conflicts