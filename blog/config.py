from dataclasses import dataclass


@dataclass
class BlogConfig:
    DEBUG: bool = True
    SECRET_KEY: str = 'you secret key'
