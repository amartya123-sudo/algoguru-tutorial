from dataclasses import dataclass, field


@dataclass
class Progress:

    completed: set[str] = field(default_factory=set)

    def complete(self, lesson: str):

        self.completed.add(lesson)

    def is_completed(self, lesson: str) -> bool:

        return lesson in self.completed

    def completion_percentage(self, lessons: list[str]) -> int:

        if not lessons:
            return 0

        return int(
            len(self.completed)
            / len(lessons)
            * 100
        )