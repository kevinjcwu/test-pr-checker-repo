import datetime

global_event_counter = 0

def log_event(timestamp: datetime.datetime, message: str, event_list: list):
    global global_event_counter

    formatted_event = f"{timestamp.isoformat()}: {message}"
    event_list.append(formatted_event)
    global_event_counter += 1
    print(f"Event logged. Global counter is now: {global_event_counter}")

if __name__ == "__main__":
    events = []
    print(f"Initial global counter: {global_event_counter}")
    log_event(datetime.datetime.now(), "User logged in", events)
    log_event(datetime.datetime.now(), "Data processed", events)
    print("\nLogged Events:")
    for event in events:
        print(event)
    print(f"\nFinal global counter: {global_event_counter}")
