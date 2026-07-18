from fastapi import APIRouter, HTTPException

from redis import Redis
from rq.job import Job

router = APIRouter()

redis = Redis(
    host="redis",
    port=6379,
)


@router.get("/{job_id}")
def get_job(job_id: str):
    try:
        job = Job.fetch(
            job_id,
            connection=redis,
        )
    except Exception:
        raise HTTPException(
            status_code=404,
            detail="Job not found.",
        )

    if job.is_finished:

        return {
            "status": "finished",
            "result": job.result,
        }

    if job.is_failed:

        return {
            "status": "failed",
        }

    if job.is_started:

        return {
            "status": "running",
        }

    return {
        "status": "queued",
    }