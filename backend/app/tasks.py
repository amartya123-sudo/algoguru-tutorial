from app.services.project_service import ProjectService
from app.core.executor import Executor
from app.core.validator import Validator


def execute_submission(
    project: str,
    step: str,
    code: str,
):

    service = ProjectService()

    scaffold = service.scaffold(
        project,
        step,
    )

    validator_code = service.validator(
        project,
        step,
    )

    executor = Executor()

    execution = executor.run(
        scaffold,
        code,
    )

    validator = Validator()

    validation = validator.run(
        validator_code,
        execution.globals_dict,
    )

    return {
        "success": validation.success,
        "stdout": execution.stdout,
        "stderr": execution.stderr,
        "execution_time": execution.time_taken,
        "message": validation.message,
        "errors": validation.errors,
    }