from dataclasses import dataclass, asdict


@dataclass
class User:
    user_id: int
    name: str
    phone: str
    street: str
    city: str
    neighborhood: str
    zip_code: str
    state: str
    email: str
    password_hash: str

    def to_dict(self):
        user_dict = asdict(self)
        user_dict.pop("password_hash", None)
        return user_dict
