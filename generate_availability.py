import json
import random
from datetime import datetime, timedelta

def generate_availability_data(months=3):

    activities = json.load(open("activities_dataset.json", "r"))
    facilitators = set()
    for activity in activities:
        facilitators.add(activity["facilitator"])

    start_date = datetime.today()
    end_date = start_date + timedelta(days=30 * months)
    
    availability = {}
    for day in range((end_date - start_date).days):
        date = (start_date + timedelta(days=day)).strftime('%Y-%m-%d')
        availability[date] = {
            facilitator: random.choice([True, False]) for facilitator in facilitators
        }
    
    with open("availability_dataset.json", "w") as f:
        json.dump(availability, f, indent=4)
    return availability