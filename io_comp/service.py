from datetime import time, timedelta, datetime
from typing import List, Tuple
from .models import Event

class CalendarService:
    DAY_START = time(7, 0)
    DAY_END = time(19, 0)

    def find_available_slots(self, events: List[Event], person_list: List[str], duration_mins: int) -> List[Tuple[time, time]]:
        event_duration = timedelta(minutes=duration_mins)
        
        clipped_events = []
        for e in events:
            if e.person in person_list:
                if e.end <= self.DAY_START or e.start >= self.DAY_END:
                    continue
                actual_start = max(e.start, self.DAY_START)
                actual_end = min(e.end, self.DAY_END)
                clipped_events.append((actual_start, actual_end))

        if not clipped_events:
            return [(self.DAY_START, self.DAY_END)]

        clipped_events.sort()
        merged = []
        if clipped_events:
            curr_s, curr_e = clipped_events[0]
            for nxt_s, nxt_e in clipped_events[1:]:
                if nxt_s <= curr_e:
                    curr_e = max(curr_e, nxt_e)
                else:
                    merged.append((curr_s, curr_e))
                    curr_s, curr_e = nxt_s, nxt_e
            merged.append((curr_s, curr_e))

        slots = []
        timeline = [(self.DAY_START, self.DAY_START)] + merged + [(self.DAY_END, self.DAY_END)]
        for i in range(len(timeline) - 1):
            gap_start, gap_end = timeline[i][1], timeline[i+1][0]
            duration = datetime.combine(datetime.today(), gap_end) - datetime.combine(datetime.today(), gap_start)
            if duration >= event_duration:
                slots.append((gap_start, gap_end))
        
        return slots