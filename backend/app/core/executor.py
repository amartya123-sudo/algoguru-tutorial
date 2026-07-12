import contextlib
import io
import time
import traceback


class ExecutionResult:

    def __init__(self, stdout="", stderr="", globals_dict=None, success=False, time_taken=0.0):
        self.stdout = stdout
        self.stderr = stderr
        self.globals_dict = globals_dict or {}
        self.success = success
        self.time_taken = time_taken


class Executor:
    def run(self, scaffold: str, user_code: str):
        start = time.time()
        final_code = scaffold.replace(
            "{{USER_CODE}}",
            user_code,
        )
        namespace = {}
        stdout = io.StringIO()
        stderr = ""
        success = False
        try:
            with contextlib.redirect_stdout(stdout):
                exec(final_code, namespace)
            success = True

        except Exception:
            stderr = traceback.format_exc()

        return ExecutionResult(
            stdout=stdout.getvalue(),
            stderr=stderr,
            globals_dict=namespace,
            success=success,
            time_taken=time.time() - start,
        )