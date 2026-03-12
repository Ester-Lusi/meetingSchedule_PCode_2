from typing import NamedTuple
from datetime import time

class Event(NamedTuple):
    person: str
    subject: str
    start: time
    end: time