import contextlib
import io
import time
import traceback


class ExecutionResult:

    def __init__(
        self,
        stdout="",
        stderr="",
        globals_dict=None,
        success=False,
        time_taken=0.0,
    ):
        self.stdout = stdout
        self.stderr = stderr
        self.globals_dict = globals_dict or {}
        self.success = success
        self.time_taken = time_taken


class Executor:

    def run(self, scaffold: str, user_code: str):

        # Handle case where user_code is None
        if user_code is None:
            user_code = ""

        start = time.time()

        # Inject the Monaco editor code into the scaffold
        final_code = scaffold.replace(
            "{{USER_CODE}}",
            user_code
        )

        namespace = {}

        stdout_buffer = io.StringIO()

        stderr = ""
        success = False

        try:

            with contextlib.redirect_stdout(stdout_buffer):
                exec(final_code, namespace)

            success = True

        except Exception:
            stderr = traceback.format_exc()

        return ExecutionResult(
            stdout=stdout_buffer.getvalue(),
            stderr=stderr,
            globals_dict=namespace,
            success=success,
            time_taken=time.time() - start,
        )