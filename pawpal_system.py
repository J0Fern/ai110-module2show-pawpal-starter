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
        """Add a care task to this pet."""
        pass

    def edit_task(self, task: Task, **changes) -> None:
        """Update fields (title, duration, priority, ...) on one of this pet's tasks."""
        pass

    def get_pending_tasks(self) -> list[Task]:
        """Return tasks that are not yet completed."""
        pass


@dataclass
class Owner:
    name: str
    available_minutes_per_day: int
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Register a pet under this owner."""
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
        """Return a readable summary of what was scheduled, what was skipped, and why."""
        pass


class Scheduler:
    def __init__(self, owner: Owner) -> None:
        self.owner = owner

    def generate_plan(self) -> DailyPlan:
        """Build a DailyPlan from the owner's pending tasks, ordered by priority
        and limited by the owner's available minutes per day."""
        pass
