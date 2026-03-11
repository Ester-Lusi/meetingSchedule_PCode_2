import pytest
from datetime import time, timedelta
from io_comp.app import CalendarService, CalendarRepository, Event

# מימוש MockRepo לצורכי בדיקה
class MockRepo(CalendarRepository):
    def __init__(self, events): self.events = events
    def get_all_events(self): return self.events

def test_everyone_free_all_day():
    """בדיקה שביום ריק מקבלים את כל טווח השעות 07:00-19:00"""
    service = CalendarService()
    slots = service.find_available_slots([], ["Alice"], timedelta(hours=1))
    assert slots == [(time(7, 0), time(19, 0))]

def test_working_hours_limits():
    """וידוא שהמערכת לא מציעה שעות לפני 07:00 או אחרי 19:00"""
    service = CalendarService()
    slots = service.find_available_slots([], ["Alice"], timedelta(hours=1))
    start, end = slots[0]
    assert start >= time(7, 0)
    assert end <= time(19, 0)

def test_clip_early_meeting():
    """פגישה שמתחילה ב-06:00 צריכה להיחתך ל-07:00 ולחסום את תחילת היום"""
    early_event = Event("Alice", time(6, 0), time(8, 0))
    service = CalendarService()
    slots = service.find_available_slots([early_event], ["Alice"], timedelta(hours=1))
    # החלון הראשון הפנוי חייב להתחיל ב-08:00
    assert slots[0][0] == time(8, 0)

def test_ignore_night_meetings():
    """פגישות בלילה (למשל 22:00) לא אמורות להשפיע על הזמן הפנוי ביום"""
    night_event = Event("Alice", time(22, 0), time(23, 0))
    service = CalendarService()
    slots = service.find_available_slots([night_event], ["Alice"], timedelta(hours=1))
    assert slots == [(time(7, 0), time(19, 0))]