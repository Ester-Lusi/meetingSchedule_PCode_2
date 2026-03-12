import csv
import os
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from .models import Event

class CalendarRepository(ABC):
    @abstractmethod
    def get_events(self) -> List[Event]: pass
    
    @abstractmethod
    def add_event(self, event: Event): pass
    
    @abstractmethod
    def remove_event(self, index: int): pass

class MemoryRepository(CalendarRepository):
    def __init__(self):
        self._events: List[Event] = []

    def add_event(self, event: Event):
        self._events.append(event)

    def remove_event(self, index: int):
        if 0 <= index < len(self._events):
            self._events.pop(index)

    def get_events(self) -> List[Event]:
        return self._events

    def load_from_csv(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"קובץ לא נמצא: {file_path}")
            
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 4: continue
                name, subject, start_str, end_str = row
                try:
                    self.add_event(Event(
                        name.strip().replace('"', ''), 
                        subject.strip().replace('"', ''),
                        datetime.strptime(start_str.strip(), "%H:%M").time(),
                        datetime.strptime(end_str.strip(), "%H:%M").time()
                    ))
                except ValueError: continue