from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum
from typing import Optional


class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: Priority = Priority.MEDIUM
    is_completed: bool = False
    pet_name: str = ""  # set by Pet.add_task so a plan can say which pet a task is for

    def __post_init__(self) -> None:
        """Validate that duration_minutes is a positive number."""
        pass

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: Optional[int] = None
    notes: Optional[str] = None
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a care task to this pet and set task.pet_name to this pet's name."""
        pass

    def edit_task(self, task: Task, **changes) -> None:
        """Update fields (title, duration, priority, ...) on one of this pet's tasks.

        Raises ValueError if the task is not in self.tasks or a key in `changes`
        is not a Task field.
        """
        pass

    def get_pending_tasks(self) -> list[Task]:
        """Return tasks that are not yet completed."""
        pass


@dataclass
class Owner:
    name: str
    available_minutes_per_day: int
    pets: list[Pet] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate that available_minutes_per_day is a positive number."""
        pass

    def add_pet(self, pet: Pet) -> None:
        """Register a pet under this owner."""
        pass

    def get_all_tasks(self) -> list[Task]:
        """Return every task across all of this owner's pets."""
        pass


@dataclass
class DailyPlan:
    scheduled_tasks: list[Task] = field(default_factory=list)
    skipped_tasks: list[Task] = field(default_factory=list)

    @property
    def total_minutes(self) -> int:
        """Total duration of all scheduled tasks."""
        pass

    def explain(self) -> str:
        """Return a readable summary of what was scheduled (with pet names),
        what was skipped, and why."""
        pass


class Scheduler:
    def __init__(self, owner: Owner) -> None:
        self.owner = owner

    def generate_plan(self) -> DailyPlan:
        """Build a DailyPlan from the owner's pending tasks.

        Rules:
        - Sort by priority (HIGH first); ties broken by shorter duration, then
          by original order, so results are deterministic.
        - Greedy fill: if a task doesn't fit in the remaining minutes, put it in
          skipped_tasks and keep trying the remaining (smaller) tasks.
        - Total scheduled time never exceeds owner.available_minutes_per_day.
        """
        pass
