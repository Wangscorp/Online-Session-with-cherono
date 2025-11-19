import csv
from datetime import datetime, timedelta

# ============== 9-DAY EXAM CRUSH PLAN (20–28 Nov 2025) ==============
start_date = datetime(2025, 11, 20)
end_date   = datetime(2025, 11, 28)
# ====================================================================

units = {
    "INTE 421": "Data Mining and Warehousing",
    "INTE 422": "IT Security, Audit and Ethics",
    "INTE 423": "Business Process Re-engineering",
    "INTE 424": "Research Project",
    "INTE 462": "Web Based Information System",
    "INTE 472": "Scripting Languages"
}

# Embedded resources for normal sessions
resources = {
    "INTE 421": "Data Mining Notes → https://www.vssut.ac.in/lecture_notes/lecture1428550844.pdf\nGuru99 → https://www.guru99.com/data-warehousing-tutorial.html",
    "INTE 422": "Kabarak Security Notes → https://www.studocu.com/row/document/kabarak-university/information-technology/inte-422-bbit-422-it-security-audit-and-ethics-kabarak-university/88509397",
    "INTE 423": "BPR Notes → https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate",
    "INTE 424": "Research Project Guide → https://phdservices.org/information-technology-research-topics-for-undergraduates/",
    "INTE 462": "Web Tech Notes → https://mrcet.com/downloads/digital_notes/IT/%28R18A0517%29%20Web%20Technologies.pdf\nW3Schools → https://www.w3schools.com",
    "INTE 472": "Flask → https://flask.palletsprojects.com\nPyMongo → https://www.mongodb.com/developer/languages/python/python-quickstart-flask"
}

# YOUR DAILY 4:00–6:00 AM CODING TASKS (specific & progressive)
daily_coding_plan = {
    "2025-11-20": "DAY 1: Flask Basics\n→ Build Hello World + 5 routes + templates\nhttps://flask.palletsprojects.com/en/stable/quickstart/",
    "2025-11-21": "DAY 2: HTML/CSS Forms\n→ Login + Register pages with Bootstrap\nhttps://getbootstrap.com/docs/5.3/forms/overview/",
    "2025-11-22": "DAY 3: Flask + MongoDB Connection\n→ Connect & do Insert/Read\nhttps://www.mongodb.com/developer/languages/python/python-quickstart-flask",
    "2025-11-23": "DAY 4: Full Login System\n→ Registration + Login + Sessions (bcrypt)\nhttps://www.youtube.com/watch?v=dam0GPOAvVI",
    "2025-11-24": "DAY 5: PHP Full CRUD App\n→ Build complete PHP project\nhttps://www.kashipara.com/project/php-projects",
    "2025-11-25": "DAY 6: JSON APIs\n→ Build REST API in Flask & PHP that returns JSON\nhttps://www.w3schools.com/js/js_json_intro.asp",
    "2025-11-26": "DAY 7: Student Management System (Flask + MongoDB)\n→ Full exam-style project (Add/View/Edit/Delete + Login)",
    "2025-11-27": "DAY 8: Library Management System (PHP)\n→ Common university exam project",
    "2025-11-28": "DAY 9: MOCK PRACTICAL EXAM\n→ 2-hour timed test: Build full app from scratch!"
}

# Daily revision schedule (Mon–Sat)
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
    day_str = current.strftime("%Y%m%d")
    date_key = current.strftime("%Y-%m-%d")
    day_num = current.day - 19  # 20→1, 21→2, etc.

    # === 4:00 – 6:00 AM DAILY CODING (with exact task) ===
    events.append({
        "Subject": f"DAY {day_num} CODING – INTE 472/462 PRACTICAL",
        "Start Date": day_str,
        "Start Time": "04:00 AM",
        "End Date": day_str,
        "End Time": "06:00 AM",
        "Description": daily_coding_plan.get(date_key, "Revise all previous projects + fix bugs"),
        "All Day Event": "False",
        "Location": ""
    })

    # Sunday (23 Nov) → only coding, then rest
    if weekday == 6:
        current += timedelta(days=1)
        continue

    # Lunch every day Mon–Sat
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

    # Normal revision sessions
    for start, end, code in schedule[weekday]:
        if code == "CLEANING":
            subject = "House Cleaning (3 hours)"
            desc = "Deep cleaning day"
        else:
            subject = f"{code} - {units[code]}"
            desc = resources.get(code, "")

        # Format time
        sh = int(start[:2])
        eh = int(end[:2])
        start_fmt = f"{sh}:{start[3:]} AM" if sh < 12 else f"{sh-12}:{start[3:]} PM"
        end_fmt   = f"{eh}:{end[3:]} AM" if eh < 12 else f"{eh-12}:{end[3:]} PM"

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

# Write CSV (fixed header order & no wrong keys)
header = ["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day Event", "Description", "Location"]
with open("9_DAY_EXAM_CRUSH_PLAN.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(events)

print("9_DAY_EXAM_CRUSH_PLAN.csv created successfully! (20–28 Nov 2025)")
print("→ Daily 4–6 AM coding tasks assigned")
print("→ All resources embedded")
print("→ Ready to import into Google Calendar")