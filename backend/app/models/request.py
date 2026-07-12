from pydantic import BaseModel


class ExecuteRequest(BaseModel):

    project: str
    step: str
    code: str