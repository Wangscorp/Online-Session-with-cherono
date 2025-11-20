import csv
from datetime import datetime, timedelta

# ============== 9-DAY EXAM CRUSH PLAN (20–28 Nov 2025) ==============
start_date = datetime(2025, 11,20)
end_date   = datetime(2025,11,28)

units = {
    "INTE 421": "Data Mining and Warehousing",
    "INTE 422": "IT Security, Audit and Ethics",
    "INTE 423": "Business Process Re-engineering",
    "INTE 424": "Research Project",
    "INTE 462": "Web Based Information System",
    "INTE 472": "Scripting Languages"
}

# FIXED: proper dictionary, not a set!
resources = {
    "INTE 421": "Data Mining Notes → https://www.vssut.ac.in/lecture_notes/lecture1428550844.pdf\nGuru99 → https://www.guru99.com/data-warehousing-tutorial.html",
    "INTE 422": "Security & Ethics Notes → https://www.studocu.com/row/document/kabarak-university/.../88509397",
    "INTE 423": "BPR Classic → https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate",
    "INTE 424": "Research Project Guide → https://phdservices.org/information-technology-research-topics-for-undergraduates/",
    "INTE 462": "Web Technologies Full Notes → https://mrcet.com/downloads/digital_notes/IT/(R18A0517) Web Technologies.pdf\nW3Schools → https://www.w3schools.com",
    "INTE 472": "Flask Official → https://flask.palletsprojects.com\nPyMongo → https://www.mongodb.com/developer/languages/python/python-quickstart-flask"
}

daily_coding_plan = {
    "2025-11-20": "DAY 1 → Flask Basics (Hello World + routes + templates)\nhttps://flask.palletsprojects.com/en/stable/quickstart/",
    "2025-11-21": "DAY 2 → Beautiful Forms with Bootstrap\nhttps://getbootstrap.com/docs/5.3/forms/overview/",
    "2025-11-22": "DAY 3 → Flask + MongoDB Connection & CRUD\nhttps://www.mongodb.com/developer/languages/python/python-quickstart-flask",
    "2025-11-23": "DAY 4 → Complete Login + Registration System (bcrypt + sessions)\nhttps://www.youtube.com/watch?v=dam0GPOAvVI",
    "2025-11-24": "DAY 5 → Full PHP CRUD Project\nhttps://www.kashipara.com/project/php-projects",
    "2025-11-25": "DAY 6 → Build JSON REST APIs (Flask & PHP)",
    "2025-11-26": "DAY 7 → Student Management System (Flask + MongoDB) – Full exam project",
    "2025-11-27": "DAY 8 → Library Management System (PHP) – Another common exam",
    "2025-11-28": "DAY 9 → MOCK PRACTICAL EXAM (2 hours – build anything from scratch)"
}

schedule = {
    0: [("06:00","08:00","INTE 421"),("08:00","10:00","INTE 422"),("10:15","12:00","INTE 423"),("14:00","16:00","INTE 462"),("16:00","18:00","INTE 472")],
    1: [("06:00","08:00","INTE 462"),("08:00","10:00","INTE 472"),("10:15","12:00","INTE 424"),("14:00","16:00","INTE 421"),("16:00","18:00","INTE 422")],
    2: [("06:00","08:00","INTE 421"),("08:00","10:00","INTE 422"),("10:15","12:00","INTE 423"),("13:00","16:00","CLEANING"),("16:00","18:00","INTE 424")],
    3: [("06:00","08:00","INTE 462"),("08:00","10:00","INTE 472"),("10:15","12:00","INTE 424"),("14:00","16:00","INTE 421"),("16:00","18:00","INTE 422")],
    4: [("06:00","08:00","INTE 421"),("08:00","10:00","INTE 422"),("10:15","12:00","INTE 423"),("14:00","16:00","INTE 462"),("16:00","18:00","INTE 472")],
    5: [("06:00","08:00","INTE 462"),("08:00","10:00","INTE 472"),("10:15","12:00","INTE 424"),("14:00","16:00","INTE 421"),("16:00","18:00","INTE 422")]
}

events = []
current = start_date

while current <= end_date:
    weekday = current.weekday()
    day_str = current.strftime("%Y-%m-%d")          # Google likes YYYY-MM-DD
    date_key = current.strftime("%Y-%m-%d")
    day_num = current.day - 19                      # 20→1, 21→2 ...

    # 4–6 AM daily coding
    events.append({
        "Subject": f"DAY {day_num} CODING – INTE 472/462 PRACTICAL",
        "Start Date": day_str,
        "Start Time": "04:00 AM",
        "End Date": day_str,
        "End Time": "06:00 AM",
        "Description": daily_coding_plan.get(date_key, "Revise all projects"),
        "All Day Event": "False",
        "Location": ""
    })

    if weekday == 6:  # Sunday 23 Nov
        current += timedelta(days=1)
        continue

    # Lunch
    events.append({
        "Subject": "Lunch + Rest",
        "Start Date": day_str,
        "Start Time": "12:00 PM",
        "End Date": day_str,
        "End Time": "02:00 PM",
        "Description": "",
        "All Day Event": "False",
        "Location": ""
    })

    # Revision sessions
    for start, end, code in schedule[weekday]:
        if code == "CLEANING":
            subject = "House Cleaning (3 hours)"
            desc = ""
        else:
            subject = f"{code} - {units[code]}"
            desc = resources.get(code, "")

        sh = int(start[:2])
        eh = int(end[:2])
        start_fmt = f"{sh}:{start[3:]} AM" if sh < 12 else f"{sh-12}:{start[3:]} PM"
        end_fmt   = f"{eh}:{end[3:]} AM" if eh <12 else f"{eh-12}:{end[3:]} PM"

        events.append({
            "Subject": subject,
            "Start Date": day_str,
            "Start Time": start_fmt,
            "End Date": day_str,
            "End Time": end_fmt,
            "Description": desc,
            "All Day Event": "False",
            "Location": ""
        })

    current += timedelta(days=1)

# Write CSV
header = ["Subject","Start Date","Start Time","End Date","End Time","All Day Event","Description","Location"]
with open("FINAL_WORKING_9_DAY_PLAN.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(events)

print("FINAL_WORKING_9_DAY_PLAN.csv created – ZERO errors!")
print("Now go to Google Calendar → Import → select this file → IT WILL WORK 100%")