from engine.loader import LessonLoader


class LessonNavigator:

    def __init__(self, loader: LessonLoader):
        self.loader = loader

    def first_lesson(self, project: str) -> str:
        lessons = self.loader.list_lessons(project)
        return lessons[0]

    def previous_lesson(
        self,
        project: str,
        current: str,
    ) -> str | None:

        lessons = self.loader.list_lessons(project)

        index = lessons.index(current)

        if index == 0:
            return None

        return lessons[index - 1]

    def next_lesson(
        self,
        project: str,
        current: str,
    ) -> str | None:

        lessons = self.loader.list_lessons(project)

        index = lessons.index(current)

        if index == len(lessons) - 1:
            return None

        return lessons[index + 1]

    def lesson_number(
        self,
        project: str,
        current: str,
    ) -> tuple[int, int]:

        lessons = self.loader.list_lessons(project)

        return (
            lessons.index(current) + 1,
            len(lessons),
        )