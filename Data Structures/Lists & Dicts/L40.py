"""Given a list of events sorted by timestamp,
remove duplicates where the same user_id + event_type appears within window_seconds. Keep the earliest event."""

from collections import defaultdict

events = [
    {"user_id": "u1", "event_type": "click", "ts": 100},
    {"user_id": "u1", "event_type": "click", "ts": 105},
    {"user_id": "u1", "event_type": "view", "ts": 110},
    {"user_id": "u2", "event_type": "click", "ts": 120},
]
window_seconds = 10
my_events=[]
print(events)
dup=defaultdict(list)
uni=defaultdict(list)
for each in range(len(events)):
    if (events[each]['user_id']==events[(each+1)]['user_id']) and (events[each]['ts']-events[(each+1)]['ts'])==window_seconds:


my_events.append(dup)
print(uni)