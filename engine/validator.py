class ValidationResult:

    def __init__(self, success, message="", errors=None):
        self.success = success
        self.message = message
        self.errors = errors or []


class Validator:

    def run(self, validator_code: str, user_globals: dict):

        namespace = {}

        exec(validator_code, namespace)

        validate = namespace["validate"]

        result = validate(user_globals)

        return ValidationResult(
            success=result["success"],
            message=result["message"],
            errors=result["errors"],
        )