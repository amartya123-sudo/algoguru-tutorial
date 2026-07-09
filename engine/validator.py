class ValidationResult:

    def __init__(self, success, message="", errors=None):
        self.success = success
        self.message = message
        self.errors = errors or []


class Validator:

    def run(self, validator_code: str, user_globals: dict):

        namespace = {}

        try:
            exec(validator_code, namespace)

            validate = namespace["validate"]

            message = validate(user_globals)

            return ValidationResult(
                success=True,
                message=message,
                errors=[],
            )

        except AssertionError as e:

            return ValidationResult(
                success=False,
                message="Validation failed.",
                errors=[str(e)],
            )

        except Exception as e:

            return ValidationResult(
                success=False,
                message="Validator error.",
                errors=[str(e)],
            )