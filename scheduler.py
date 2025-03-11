import json
from collections import defaultdict
from datetime import datetime

from generate_activity import generate_activity_data
from generate_availability import generate_availability_data


def parse_frequency(freq):
    if freq == "Daily":
        return 7
    elif freq == "Every other day":
        return 3
    elif "times a week" in freq:
        return int(freq[0])
    elif freq == "Twice a week":  
        return 2
    elif freq == "Once a week":
        return 1
    return 7


def get_week_number(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return date.isocalendar()[1]


def schedule_activities():
    with open("activities_dataset.json", "r") as f:
        activities = json.load(f)
    with open("availability_dataset.json", "r") as f:
        availability = json.load(f)

    schedule = {}
    weekly_activity_count = defaultdict(lambda: defaultdict(int))

    for date, resources in availability.items():
        daily_plan = []
        resources = {k.lower(): v for k, v in resources.items()}
        week_num = get_week_number(date)

        for activity in activities:
            if len(daily_plan) >= 3:
                break

            facilitator = activity["facilitator"].lower()
            max_weekly_freq = parse_frequency(activity["frequency"])
            current_freq = weekly_activity_count[week_num][activity["id"]]

            if resources.get(facilitator, False) and current_freq < max_weekly_freq:
                daily_plan.append(
                    {
                        "activity": activity["activity"],
                        "facilitator": activity["facilitator"],
                        "frequency": activity["frequency"],
                    }
                )
                weekly_activity_count[week_num][activity["id"]] += 1
                continue

            for backup in activity["backup_activities"]:
                if len(daily_plan) >= 3:
                    break

                backup_activity = next(
                    (a for a in activities if a["activity"] == backup), None
                )
                if not backup_activity:
                    continue

                backup_facilitator = backup_activity["facilitator"].lower()
                if not resources.get(backup_facilitator, False):
                    continue

                backup_freq = parse_frequency(backup_activity["frequency"])
                backup_current_freq = weekly_activity_count[week_num][
                    backup_activity["id"]
                ]

                if backup_current_freq < backup_freq:
                    daily_plan.append(
                        {
                            "activity": backup,
                            "facilitator": backup_activity["facilitator"],
                            "frequency": backup_activity["frequency"],
                        }
                    )
                    weekly_activity_count[week_num][backup_activity["id"]] += 1
                    break

        if daily_plan:
            schedule[date] = daily_plan

    with open("schedule.json", "w") as f:
        json.dump(schedule, f, indent=4)

    return schedule


if __name__ == "__main__":
    # generate_activity_data()
    # generate_availability_data()
    final_schedule = schedule_activities()
    print("Schedule created successfully! Check schedule.json for output.")
