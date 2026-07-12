from pydantic import BaseModel


class ExecuteResponse(BaseModel):

    success: bool
    stdout: str
    stderr: str
    execution_time: float
    message: str
    errors: list[str]