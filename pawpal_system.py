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

    def update_task(self):
        pass

    def mark_complete(self):
        pass

    def get_details(self):
        pass


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
        pass

    def get_tasks(self):
        pass

    def update_info(self):
        pass


# -------------------- Owner --------------------
class Owner:
    def __init__(self, name: str, available_time: int, preferences: dict):
        self.name = name
        self.available_time = available_time
        self.preferences = preferences
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        pass

    def update_preferences(self):
        pass

    def get_available_time(self):
        pass


# -------------------- Scheduler --------------------
class Scheduler:
    def __init__(self, tasks_list: List[Task], available_time: int):
        self.tasks_list = tasks_list
        self.available_time = available_time
        self.daily_plan: List[Task] = []

    def generate_schedule(self):
        pass

    def sort_tasks_by_priority(self):
        pass

    def check_constraints(self):
        pass

    def explain_plan(self):
        pass