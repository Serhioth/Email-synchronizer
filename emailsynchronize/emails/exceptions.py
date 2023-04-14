class BaseException(Exception):
    """Basic initialization exception class."""

    def __init__(self, message, description) -> None:
        """Initializing custom exception class."""
        self.description = description
        if message:
            self.message = message
        else:
            self.message = None

    def __str__(self):
        """Basic exceprion error message."""
        if self.message:
            return f'''
        {self.__class__.__name__}
        {self.description}
        {self.message}
        '''
        else:
            return 'Неизвестная ошибка!'


class ParseEmailError(BaseException):
    """Raises if can't parse data from email."""

    def __init__(self, message) -> None:
        """Initializing custom email-parsing error class."""
        self.message = message
        self.description = 'Ошибка при получении данных из e-mail:'
        super().__init__(message=self.message, description=self.description)


class DomainError(BaseException):
    """Raises if can't parse data from email."""

    def __init__(self, message) -> None:
        """Initializing custom email-parsing error class."""
        self.message = message
        self.description = 'Неверный домен:'
        super().__init__(message=self.message, description=self.description)


class IMAPError(BaseException):
    """Raises if an error occurs when connecting to IMAP-server."""

    def __init__(self, message) -> None:
        """Initializing custom IMAP error class."""
        self.message = message
        self.description = 'Ошибка при соединении с IMAP:'
        super().__init__(message=self.message, description=self.description)


class RequestsError(BaseException):
    """Raises if an error occurs when requesting to server."""

    def __init__(self, message) -> None:
        """Initializing custom request error class."""
        self.message = message
        self.description = 'Ошибка при обращении к серверу:'
        super().__init__(message=self.message, description=self.description)


class FIOError(BaseException):
    """Raises if can't find FIO in excel files."""

    def __init__(self, message) -> None:
        """Initializing custom FIO error class."""
        self.message = message
        self.description = 'Нет ФИО связанных с логином:'
        super().__init__(message=self.message, description=self.description)


class UserCreateError(BaseException):
    """Raises if an error occurs when creating a user."""

    def __init__(self, message) -> None:
        """Initializing custom user-creation error class."""
        self.message = message
        self.description = 'Ошибка при создании пользователя:'
        super().__init__(message=self.message, description=self.description)
