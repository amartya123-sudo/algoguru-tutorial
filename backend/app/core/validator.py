class ValidationResult:

    def __init__(self, success, message="", errors=None):
        self.success = success
        self.message = message
        self.errors = errors or []


class Validator:
    def run(self, validator_code: str, namespace: dict):
        scope = {}
        exec(validator_code, scope)
        validate = scope["validate"]

        try:
            result = validate(namespace)
            if isinstance(result, str):
                return ValidationResult(
                    success=True,
                    message=result,
                    errors=[],
                )

            return ValidationResult(
                success=result["success"],
                message=result["message"],
                errors=result["errors"],
            )

        except AssertionError as e:

            return ValidationResult(
                success=False,
                message="Validation failed.",
                errors=[str(e)],
            )