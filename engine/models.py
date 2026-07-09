from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


@dataclass
class Lesson:
    id: str
    title: str
    difficulty: str
    estimated_time: int
    objective: str
    concept: str
    instructions: list
    hint: str
    success_message: str
    next_lesson: str | None
    starter_code: str
    scaffold_code: str
    validator_code: str
    solution_code: str

@dataclass
class ExecutionResult:
    success: bool
    stdout: str
    stderr: str
    validation: str
    execution_time: float

@dataclass
class ValidationResult:
    success: bool
    errors: List[str]
    hints: List[str]