# PawPal+ Project Reflection

## 1. System Design

Brainstorm:

The user should be able to add a pet and information about the pet. Then the user should be able to add tasks for the pet to be completed. Then the program should be able to display the information of the pet along with the tasks set to be completed.

Pet object. Contains The type of animal, the name of the pet, the age, and the name of the owner of the pet.

Task object. Contains the name of the task, the duration of the task, the importance of the task, and the status of the task (completed/incomplete).
- function for marking the status of the task as complete.

Each object should be able to return a organized view of all the information, via a toString function. Each object should have getter and setter functions.

There can be another class for the schedule that contains a list of tasks.


**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial design just included classes for the pet, the task, and the schedule to be created. The pet would've contained info like name, age, species, owner. The task class would've contained info like the name of the task, description, priority, and duration of the task. Lastly the class for the schedule wasn't well designed, I thought it would contain the list of tasks for a pet.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, with the help of the AI assistant I was able to better define each class and their relationships as well as other classes that would make the code cleaner and the relationships easier to work with. The overall class would be a scheduler that creates a schedule from already existing classes and information, then there would be an owner who has a pet who has a task, and each task uses enumeration to define the priority of the task. The overall scheduler class creates a daily plan class which looks at the task class and each tasks priority and duration.

This version of the UML came after the initial creation of the UML with some unecessary information trimmed out of some of the classes. This is to make the code less cluttered and make everything have a purpose for existing.

---

## 2. Scheduling Logic and Tradeoffs

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
