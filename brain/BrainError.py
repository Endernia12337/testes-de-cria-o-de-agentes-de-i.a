class BrainError(Exception):
    pass


class InvalidActionError(BrainError):
    def __init__(self, action, operation=None):

        message = f'<InvalidActionError>: invalid action "{action}"'

        if operation:
            message += f' during {operation}'

        super().__init__(message)


class MemoryError(BrainError):
    def __init__(self, operation, file, error=None):

        message = f'<MemoryError>: failed to {operation} file "{file}"'

        if error:
            message += f' -> <{error}>'

        super().__init__(message)


class ActionTrackerError(BrainError):
    def __init__(self, error, operation=None):

        message = f'<ActionTrackerError>: {error}'

        if operation:
            message += f' during {operation}'

        super().__init__(message)


class LearningError(BrainError):
    def __init__(
        self,
        action_name,
        dimension=None,
        operation=None,
        error=None
    ):

        message = f'<LearningError>: failed learning for action "{action_name}"'

        if operation:
            message += f' during {operation}'

        if dimension:
            message += f' in dimension "{dimension}"'

        if error:
            message += f' -> <{error}>'

        super().__init__(message)


class DecisionError(BrainError):
    def __init__(
        self,
        operation=None,
        action=None,
        score=None,
        error=None
    ):

        message = '<DecisionError>: failed decision process'

        if operation:
            message += f' during {operation}'

        if action:
            message += f' with action "{action}"'

        if score is not None:
            message += f' and score "{score}"'

        if error:
            message += f' -> <{error}>'

        super().__init__(message)
class ValidationError(BrainError):
    def __init__(self, field, expected=None, received=None, operation=None):

        message = f'<ValidationError>: invalid structure in "{field}"'

        if expected:
            message += f' | expected: <{expected}>'

        if received:
            message += f' | received: <{received}>'

        if operation:
            message += f' during "{operation}"'

        super().__init__(message)