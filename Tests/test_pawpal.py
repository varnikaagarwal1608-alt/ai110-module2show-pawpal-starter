import pytest
from pawpal_system import Task, Pet

def test_task_completion():
    task = Task("Feed", 15, "HIGH", "daily")
    assert not task.completed  # initially False
    task.mark_complete()
    assert task.completed      # should now be True

def test_task_addition():
    pet = Pet("Buddy", "Dog", 5)
    initial_count = len(pet.tasks)
    task = Task("Walk", 30, "HIGH", "daily")
    pet.add_task(task)
    assert len(pet.tasks) == initial_count + 1
    assert pet.tasks[0] == task
    assert task.pet == pet