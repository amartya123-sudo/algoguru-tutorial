from pathlib import Path
import yaml
from engine.models import Lesson

class LessonLoader:

    def __init__(self, tutorials_dir: str = "tutorials"):
        self.tutorials_dir = Path(tutorials_dir)

    def _read_file(self, path: Path) -> str:
        return path.read_text(encoding="utf-8")

    def list_projects(self) -> list[str]:
        return sorted(
            [
                project.name
                for project in self.tutorials_dir.iterdir()
                if project.is_dir()
            ]
        )

    def list_lessons(self, project: str) -> list[str]:

        project_dir = self.tutorials_dir / project

        return sorted(
            [
                lesson.name
                for lesson in project_dir.iterdir()
                if lesson.is_dir()
            ]
        )

    def load(self, project: str, lesson: str) -> Lesson:

        lesson_dir = (
            self.tutorials_dir
            / project
            / lesson
        )

        metadata = yaml.safe_load(
            self._read_file(
                lesson_dir / "lesson.yaml"
            )
        )

        return Lesson(
            id=metadata["id"],
            title=metadata["title"],
            difficulty=metadata["difficulty"],
            estimated_time=metadata["estimated_time"],
            objective=metadata["objective"],
            concept=metadata["concept"],
            instructions=metadata["instructions"],
            hint=metadata["hint"],
            success_message=metadata["success_message"],
            next_lesson=metadata.get("next_lesson"),
            starter_code=self._read_file(
                lesson_dir / "starter.py"
            ),
            scaffold_code=self._read_file(
                lesson_dir / "scaffold.py"
            ),
            validator_code=self._read_file(
                lesson_dir / "validator.py"
            ),
            solution_code=self._read_file(
                lesson_dir / "solution.py"
            ),
        )