from datetime import datetime, timedelta
import json
import os

def load_events():
    with open("events.json", "r", encoding="utf-8") as f:
        return json.load(f)

def generate_ics(event):
    title = event["title"]
    start_date = datetime.strptime(event["start_date"], "%Y-%m-%d").date()
    interval = event["interval"]

    today = datetime.utcnow().date()
    end_date = today.replace(year=today.year + 5)

    d = start_date
    lines = []
    lines.append("BEGIN:VCALENDAR")
    lines.append("VERSION:2.0")
    lines.append("PRODID:-//GAMEUPDATECALENDAR//EN")

    while d <= end_date:
        dt = d.strftime("%Y%m%d")
        lines.append("BEGIN:VEVENT")
        lines.append(f"UID:{dt}-{title}")
        lines.append(f"DTSTAMP:{dt}T000000Z")
        lines.append(f"DTSTART;VALUE=DATE:{dt}")
        lines.append(f"SUMMARY:{title}")
        lines.append(f"END:VEVENT")
        d = d + timedelta(days=interval)
    
    lines.append("END:VCALENDAR")
    return "\n".join(lines)


def generate_all():
    os.makedirs("ics", exist_ok=True)

    events = load_events()

    for key, cfg in events.items():
        ics = generate_ics(cfg)
        with open(f"ics/{key}.ics", "w", encoding="utf-8") as f:
            f.write(ics)


if __name__ == "__main__":
    generate_all()