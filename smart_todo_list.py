import datetime
import re

def parse_task(input_text):
    date_match = re.search(r"tomorrow|today|(\d{4}-\d{2}-\d{2})", input_text)
    task = input_text
    due = "unspecified"

    if date_match:
        if date_match.group() == "tomorrow":
            due = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
        elif date_match.group() == "today":
            due = datetime.date.today().isoformat()
        else:
            due = date_match.group()
        task = input_text.replace(date_match.group(), "").strip()

    return {"task": task, "due": due}

while True:
    user_input = input("Add a task (or type 'exit'): ")
    if user_input.lower() == 'exit':
        break
    parsed = parse_task(user_input)
    print(f"✔ Task: {parsed['task']} | Due: {parsed['due']}")
