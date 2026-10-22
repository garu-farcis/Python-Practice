"""Write a function flatten_events(events: list[dict]) -> list[dict] that
flattens nested dictionaries (one level of nesting is enough for intermediate).
Preserve top-level keys and prefix nested keys with the parent key + _."""


def flatten_events(events: list[dict]) -> list[dict]:
    my_event=[]
    for each in events:
        if isinstance(each,dict):
            my_event.extend(list(flatten_events(each)))
        else:
            my_event.append(list(each))

events = [
        {"id": 1, "user": {"name": "Alice", "age": 30}, "ts": 1690000000},
        {"id": 2, "user": {"name": "Bob", "age": 25}, "ts": 1690000100}
    ]