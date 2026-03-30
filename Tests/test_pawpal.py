import pytest
from datetime import date, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler

# ---------- Fixtures ----------
@pytest.fixture
def sample_owner():
    owner = Owner("Alice", available_time=120, preferences={})
    dog = Pet("Buddy", "Dog", 5)
    cat = Pet("Mittens", "Cat", 3)
    owner.add_pet(dog)
    owner.add_pet(cat)
    dog.add_task(Task("Walk", 30, "HIGH", "daily", time="10:00"))
    dog.add_task(Task("Feed", 15, "MEDIUM", "daily", time="08:00"))
    cat.add_task(Task("Play", 45, "LOW", "daily", time="09:00"))
    return owner

@pytest.fixture
def scheduler(sample_owner):
    return Scheduler(sample_owner)

# ---------- Task Tests ----------
def test_task_completion():
    task = Task("Feed", 15, "HIGH", "daily")
    assert not task.completed
    task.mark_complete()
    assert task.completed

def test_task_addition():
    pet = Pet("Buddy", "Dog", 5)
    initial_count = len(pet.tasks)
    task = Task("Walk", 30, "HIGH", "daily")
    pet.add_task(task)
    assert len(pet.tasks) == initial_count + 1
    assert pet.tasks[0] == task
    assert task.pet == pet

# ---------- Sorting Tests ----------
def test_sort_by_time(scheduler):
    scheduler.tasks_list = scheduler.owner.get_all_tasks()
    scheduler.sort_by_time()
    times = [t.time for t in scheduler.tasks_list]
    assert times == sorted(times)

# ---------- Recurrence Tests ----------
def test_daily_recurrence():
    buddy = Pet("Buddy", "Dog", 5)
    task = Task("Feed", 15, "HIGH", "daily", pet=buddy, time="08:00")
    buddy.add_task(task)

    task.mark_complete()
    new_tasks = buddy.tasks

    print(f"Number of tasks: {len(new_tasks)}")
    for t in new_tasks:
        print(f"Task: {t.name}, freq: {t.frequency}, completed: {t.completed}, is same: {t is task}")

    # Ensure a new task was created for the next day
    assert any(t for t in new_tasks if t is not task and t.frequency == "daily")
# ---------- Conflict Detection ----------
def test_conflicts_detection(scheduler):
    # Add two tasks at same time for same pet
    dog = scheduler.owner.pets[0]
    dog.add_task(Task("Checkup", 20, "HIGH", "once", time="10:00"))
    scheduler.generate_schedule()
    conflicts = scheduler.detect_conflicts()
    # Should detect at least one conflict
    assert any(c[0].time == c[1].time for c in conflicts)

# ---------- Edge Cases ----------
def test_empty_task_list():
    empty_pet = Pet("Ghost", "Dog", 2)
    assert empty_pet.get_tasks() == []

def test_pet_with_no_tasks(sample_owner):
    pet = Pet("NoTasks", "Cat", 1)
    sample_owner.add_pet(pet)
    tasks = pet.get_tasks()
    assert tasks == []

def test_invalid_time_format():
    task = Task("Nap", 30, "LOW", "once", time="25:00")
    # Sorting should handle or ignore invalid times without crashing
    pet = Pet("Buddy", "Dog", 5)
    pet.add_task(task)
    owner = Owner("Tester", 60, {})
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    scheduler.tasks_list = owner.get_all_tasks()
    try:
        scheduler.sort_by_time()
        success = True
    except:
        success = False
    assert success