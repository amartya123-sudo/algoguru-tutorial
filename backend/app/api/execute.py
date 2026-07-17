from fastapi import APIRouter, HTTPException

from app.core.queue import execution_queue
from app.models.request import ExecuteRequest
from app.services.project_service import ProjectService
from app.tasks import execute_submission

router = APIRouter()

service = ProjectService()


@router.post("")
def execute(request: ExecuteRequest):

    if not service.exists(
        request.project,
        request.step,
    ):
        raise HTTPException(
            status_code=404,
            detail="Step not found.",
        )

    job = execution_queue.enqueue(
        execute_submission,
        request.project,
        request.step,
        request.code,
    )

    return {
        "job_id": job.id,
        "status": "queued",
    }