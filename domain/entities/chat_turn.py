from dataclasses import dataclass


@dataclass
class ChatTurn:
    user_message: str
    assistant_response: str
