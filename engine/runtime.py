from engine.executor import Executor
from engine.validator import Validator


class LessonRuntime:

    def __init__(self, lesson):
        self.lesson = lesson
        self.executor = Executor()
        self.validator = Validator()

    def execute(self, user_code: str):

        result = self.executor.run(
            self.lesson.scaffold_code,
            user_code
        )

        validation = self.validator.run(
            self.lesson.validator_code,
            result.globals_dict
        )

        result.validation = validation

        return result