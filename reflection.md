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

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
