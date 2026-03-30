import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import date

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

# ---------------------
# Initialize Owner
# ---------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner(
        name="Jordan",
        available_time=240,
        preferences={}  # Required argument added
    )
owner = st.session_state.owner

# ---------------------
# Welcome & Scenario
# ---------------------
st.markdown(
    """
Welcome to the PawPal+ app! This assistant helps you plan pet care tasks,
track recurring tasks, and avoid scheduling conflicts.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant.
It helps a pet owner plan tasks for their pet(s) based on time, priority, and preferences.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
Your system should:
- Represent pet care tasks (name, duration, priority, frequency)
- Represent pets and owner preferences
- Generate a daily schedule
- Explain the plan and flag conflicts
"""
    )

st.divider()

# ---------------------
# Add Pet & Tasks
# ---------------------
st.subheader("Add a Pet & Tasks")
owner_name = st.text_input("Owner name", value=owner.name)
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a task. This feeds directly into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3, col4 = st.columns(4)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
with col4:
    frequency = st.selectbox("Frequency", ["once", "daily", "weekly"], index=0)

if st.button("Add task"):
    # Create default pet if none
    if not owner.pets:
        new_pet = Pet(name=pet_name, type=species, age=1)
        owner.add_pet(new_pet)
    else:
        new_pet = owner.pets[0]

    # Create Task
    new_task = Task(
        name=task_title,
        duration=int(duration),
        priority=priority.upper(),
        frequency=frequency,
        pet=new_pet
    )
    new_pet.add_task(new_task)
    st.success(f"Added task '{new_task.name}' to pet '{new_pet.name}' ({frequency})")

# ---------------------
# Display current pets & tasks
# ---------------------
st.subheader("Current Pets & Tasks")
for pet in owner.pets:
    st.write(f"**{pet.name} ({pet.type})**")
    for t in pet.get_tasks():
        st.write(
            f"- {t.name} ({t.priority}) - {t.duration} mins | "
            f"Completed: {t.completed} | "
            f"Frequency: {t.frequency} | "
            f"Next Due: {t.due_date if t.due_date else 'N/A'}"
        )

st.divider()

# ---------------------
# Generate Schedule
# ---------------------
st.subheader("Build Schedule")
st.caption("Generate your daily schedule and check for conflicts.")

if st.button("Generate schedule"):
    if not owner.pets:
        st.warning("Add a pet first!")
    else:
        scheduler = Scheduler(owner=owner)
        schedule = scheduler.generate_schedule()
        st.markdown("### 🗓️ Today's Schedule")
        if schedule:
            # Display as table
            st.table([
                {
                    "Pet": t.pet.name if t.pet else "Unknown",
                    "Task": t.name,
                    "Duration": t.duration,
                    "Priority": t.priority,
                    "Completed": t.completed,
                    "Due": t.due_date
                }
                for t in schedule
            ])
            # Show conflicts
            conflicts = scheduler.detect_conflicts()
            if conflicts:
                st.warning("⚠️ Conflicts detected!")
                for t1, t2 in conflicts:
                    st.warning(f"{t1.name} overlaps with {t2.name} for {t1.pet.name}")
            else:
                st.success("No conflicts detected! ✅")
        else:
            st.info("No tasks scheduled for today.")

# ---------------------
# Real-time Conflict Checker
# ---------------------
with st.expander("Check for conflicts"):
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        for t1, t2 in conflicts:
            st.warning(f"Conflict: {t1.name} ({t1.pet.name}) overlaps with {t2.name} ({t2.pet.name})")
    else:
        st.success("No conflicts detected!")