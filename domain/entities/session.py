from dataclasses import dataclass


@dataclass
class UserSession:
    user_id: str
    uploaded_file_name: str = ""
