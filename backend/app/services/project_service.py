from pathlib import Path


class ProjectService:

    def __init__(self):
        self.projects_dir = Path("app/projects")

    def project_path(self, project: str) -> Path:
        return (self.projects_dir / project)

    def step_path(self, project: str, step: str) -> Path:
        return (self.project_path(project) / step)

    def exists(self, project: str, step: str) -> bool:
        return self.step_path(project, step).exists()

    def read(self, project: str, step: str, filename: str) -> str:
        path = (self.step_path(project, step) / filename)
        return path.read_text(encoding="utf-8")

    def starter(self, project: str, step: str) -> str:
        return self.read(project, step, "starter.py")

    def solution(self, project: str, step: str) -> str:
        return self.read(project, step, "solution.py")

    def scaffold(self, project: str, step: str) -> str:
        return self.read(project, step, "scaffold.py")

    def validator(self, project: str, step: str) -> str:
        return self.read(project, step, "validator.py")

    def list_projects(self):
        return sorted([p.name for p in self.projects_dir.iterdir() if p.is_dir()])

    def list_steps(self, project: str):
        return sorted([p.name for p in self.project_path(project).iterdir() if p.is_dir()])