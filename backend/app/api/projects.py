from fastapi import APIRouter

from app.services.project_service import ProjectService

router = APIRouter()
service = ProjectService()

@router.get("")
def list_projects():
    return service.list_projects()

@router.get("/{project}/steps")
def list_steps(project: str):
    return service.list_steps(project)

@router.get("/{project}/steps/{step}/starter")
def starter(project: str, step: str):
    return {"code": service.starter(project, step)}

@router.get("/{project}/steps/{step}/solution")
def solution(project: str, step: str):
    return {"code": service.solution(project, step)}