from dataclasses import dataclass, field
from typing import List, Optional


# -------------------- Task --------------------
@dataclass
class Task:
    name: str
    duration: int
    priority: str
    frequency: str
    pet: Optional["Pet"] = None
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

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
        return sorted(tasks, key=lambda t: priority_map.get(t.priority.upper(), 4))

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