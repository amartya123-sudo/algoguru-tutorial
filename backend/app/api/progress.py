from fastapi import APIRouter

router = APIRouter()


@router.get("/{project}")
def progress(project: str):

    return {
        "project": project,
        "completed_steps": [],
    }