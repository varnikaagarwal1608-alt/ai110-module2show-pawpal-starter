# PawPal+ Project Reflection

## 1. System Design
1. Add and manage pets
The user should be able to enter basic information about their pet (such as name, type, age, or special needs) and update it when needed.

2. Create and manage care tasks
The user should be able to add tasks like feeding, walking, or medication, including details like duration, priority, and frequency.

3. Generate and view a daily schedule
The system should create an optimized daily plan based on the user’s available time, task priorities, and constraints, and display it clearly along with an explanation.
**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

-My initial UML design included four main classes: Owner, Pet, Task, and Scheduler. The Owner class is responsible for storing user information such as name, available time, and preferences, and for managing pets. The Pet class represents individual pets and stores details like name, type, age, and any special needs, along with their associated tasks. The Task class represents different pet care activities such as feeding or walking, and includes attributes like duration, priority, and frequency. The Scheduler class is responsible for organizing tasks into a daily plan based on constraints like available time and task priority. Overall, the design focuses on separating responsibilities clearly while allowing the classes to interact through defined relationships.
---
**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

-While no changes were made to the Python skeleton itself, reviewing it with AI made me think about improvements in class relationships. For example, linking the Scheduler directly to the Owner (instead of just passing available_time) would make the system more consistent. I also reviewed how tasks should be associated with pets to ensure clear object relationships. These reflections helped refine my design thinking without altering the actual code.
---
## 2. Scheduling Logic and Tradeoffs
My scheduler uses a simple conflict detection approach that only checks for exact time matches between tasks. This improves readability and keeps the implementation lightweight, but it does not handle overlapping durations, which could lead to missed conflicts in more complex scenarios.

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

a. Constraints and priorities

My scheduler considers several constraints such as the owner’s available time, the priority of each task (HIGH, MEDIUM, LOW), and the task duration. Tasks are sorted based on time and priority to ensure that more important tasks are handled first. I decided that time and priority mattered the most because a pet owner typically has limited time and needs to focus on the most essential tasks first, such as feeding or medication, before lower priority activities like playtime.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

 One tradeoff my scheduler makes is that it only checks for conflicts based on exact time matches rather than overlapping durations. This makes the implementation simpler and easier to understand, but it means that some real-world conflicts (like a 10:00–10:30 task overlapping with a 10:15 task) may not be detected. This tradeoff is reasonable for this project because it keeps the system lightweight and readable while still demonstrating the core idea of conflict detection.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used VS Code Copilot mainly for debugging, understanding errors, and completing parts of the implementation. It helped me fix issues in my code, especially when my tests were failing or when methods like mark_complete() were not working correctly. I also used it to understand how different parts of the system should connect, such as linking tasks to pets and integrating the scheduler. 
The most helpful prompts were simple and direct, like asking why a specific error was happening, how to fix a failing test, or how to implement a method step by step. These questions helped me not just fix the code, but also understand the logic behind it.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

One moment where I didn’t accept an AI suggestion directly was when handling recurring tasks. The initial suggestion didn’t correctly handle cases where the task had no due date, which caused errors. I modified the logic to use the current date when no due date was present. I verified this by running tests using pytest and checking whether new tasks were correctly created.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
I tested core behaviors such as task creation, task completion, recurring task generation, sorting tasks by time, and conflict detection. These tests were important because they ensured that the main functionality of the scheduler worked correctly and handled both normal cases and edge cases.
**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am fairly confident that my scheduler works correctly for the main use cases, especially after running automated tests with pytest. However, if I had more time, I would test more edge cases such as overlapping task durations, invalid time formats, and scenarios with no pets or tasks.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I am fairly confident that my scheduler works correctly for the main use cases, especially after running automated tests with pytest. However, if I had more time, I would test more edge cases such as overlapping task durations, invalid time formats, and scenarios with no pets or tasks.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would improve the scheduling logic to handle overlapping task durations more accurately and make the schedule generation more dynamic so that tasks always appear for the current day. I would also improve the UI to allow managing multiple pets more easily.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One important thing I learned is that designing a system is not just about writing code, but about structuring logic clearly and making good decisions about tradeoffs. Working with AI showed me that while AI can generate code quickly, I still need to act as the “lead architect” to guide, verify, and refine the final solution.