from domain.entities.session import UserSession


class SessionUseCase:
    def __init__(self):
        self.session = None

    def create_session(self, user_id: str) -> UserSession:
        self.session = UserSession(user_id=user_id)
        return self.session

    def set_file(self, file_name: str):
        if self.session:
            self.session.uploaded_file_name = file_name

    def get_session(self):
        return self.session
