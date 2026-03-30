# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Smarter Scheduling

The PawPal+ system now includes:
- Task sorting by time
- Filtering by pet and completion status
- Basic conflict detection for overlapping tasks
- Support for recurring tasks (daily/weekly)

## Testing PawPal+

To ensure PawPal+ works correctly, we created an automated test suite using `pytest`.

**Run the tests:**  
```bash
python -m pytest
What the tests cover:
-Task completion and addition
-Recurring task creation (daily and weekly)
-Sorting tasks by priority and time
-Conflict detection between overlapping tasks
-Edge cases like empty lists, invalid times, and task updates
Confidence Level: ⭐⭐⭐⭐⭐


## Features

PawPal+ includes several smart features:

- **Task Management** – Add tasks with duration, priority, and frequency.
- **Recurring Tasks** – Automatically repeat daily or weekly tasks.
- **Task Completion Tracking** – Mark tasks as done; recurring tasks auto-generate for the next date.
- **Conflict Detection** – Scheduler warns if tasks overlap for the same pet.
- **Priority-Based Scheduling** – Scheduler sorts tasks based on priority and time availability.
- **Filtering & Sorting** – View tasks by pet, completion status, or scheduled time.
- **Interactive Streamlit UI** – Easily add pets, tasks, and generate schedules.


## 📸 Demo

Here’s a screenshot of the PawPal+ app running in Streamlit:

<a href="/course_images/ai110/pawpal_demo.png
" target="_blank"><img src='/course_images/ai110/your_screenshot_name.png' title='PawPal App' width='' alt='PawPal App' class='center-block' /></a>.
!