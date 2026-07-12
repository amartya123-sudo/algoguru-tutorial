from fastapi import APIRouter, HTTPException
from app.core.executor import Executor
from app.core.validator import Validator
from app.models.request import ExecuteRequest
from app.models.response import ExecuteResponse
from app.services.project_service import ProjectService

router = APIRouter()
executor = Executor()
validator = Validator()
service = ProjectService()


@router.post("", response_model=ExecuteResponse)
def execute(request: ExecuteRequest):

    if not service.exists(request.project, request.step):
        raise HTTPException(status_code=404, detail="Step not found.")

    scaffold = service.scaffold(request.project, request.step)
    validator_code = service.validator(request.project, request.step)
    execution = executor.run(scaffold, request.code)
    validation = validator.run(validator_code, execution.globals_dict)

    return ExecuteResponse(
        success=validation.success,
        stdout=execution.stdout,
        stderr=execution.stderr,
        execution_time=execution.time_taken,
        message=validation.message,
        errors=validation.errors,
    )