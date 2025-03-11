import json
import random

def generate_activity_data(num_activities=100):
    activity_types = [
    "Running", "Strength Training", "Eye Exercises", "Meal Consumption - Protein Rich", "Hydration",
    "Sauna Therapy", "Cold Therapy", "Consultation - Physiotherapy", "Vitamin D Supplementation", "Yoga",
    "Cycling", "Rowing", "Stretching", "Foam Rolling", "Deep Tissue Massage", "Swimming", "Tai Chi",
    "Weightlifting", "Jump Rope", "Shadow Boxing", "Pilates", "Meditation", "Keto Meal Consumption",
    "Intermittent Fasting", "Protein Shake", "Mental Health Counseling", "Blood Sugar Test", "Blood Pressure Check",
    "Vitamin B12 Injection", "Acupuncture", "Cardio Dance", "TRX Training", "Boxing Training", "Rock Climbing",
    "Hiking", "Trail Running", "CrossFit", "Calisthenics", "Aqua Aerobics", "Parkour", "Judo", "Karate", "Ballet",
    "Posture Training", "Sound Therapy", "Breathing Exercises", "Reflexology", "Tai Massage", "Juicing",
    "Herbal Supplementation", "Tea Therapy", "Ayurvedic Diet", "Vegan Diet Plan", "Gluten-Free Diet",
    "Ketone Monitoring", "Cholesterol Check", "Insulin Sensitivity Test", "Sleep Study", "Brainwave Monitoring",
    "EMG Analysis", "HRV Monitoring", "Mobility Training", "Balance Training", "Grip Strength Training",
    "Obstacle Course Training", "Pole Fitness", "Park Workout", "Skateboarding", "Surfing", "Stand-Up Paddleboarding",
    "Ice Skating", "Skiing", "Snowboarding", "Archery", "Fencing", "Ultimate Frisbee", "Disc Golf", "E-Sports Training",
    "VR Workout", "Mindfulness Journaling", "Art Therapy", "Music Therapy", "Dance Therapy", "Writing Therapy",
    "Acting Therapy", "Cooking Therapy", "Gardening Therapy", "Animal Therapy", "Aromatherapy", "Sauna Detox",
    "Infrared Therapy", "Hydrotherapy", "Sensory Deprivation", "Sound Bath", "Float Therapy", "Light Therapy",
    "Chiropractic Adjustment", "Postural Correction", "Neuromuscular Therapy", "Myofascial Release"
]
    frequency = ["Daily", "Twice a week", "3 times a week", "4 times a week", "Once a week", "Every other day"]
    locations = ["Gym", "Home", "Clinic", "Park", "Wellness Center", "Anywhere"]
    preparations = [
        "Wear appropriate clothing", "Hydrate well before session", "Ensure proper equipment", 
        "Log previous records", "Prepare necessary food", "Take pre-session supplements"
    ]
    metrics = [
        ["Heart Rate", "Calories Burned", "Workout Duration"], 
        ["Nutritional Intake", "Hydration Level", "Meal Timing"], 
        ["Recovery Score", "Pain Level", "Flexibility"], 
        ["Blood Pressure", "Glucose Levels", "Cholesterol"]
    ]
    facilitators = ["Trainer", "Dietitian", "Doctor", "Physiotherapist"]

    activities = []
    for i in range(num_activities):
        activity = {
            "id": i,
            "activity": random.choice(activity_types),
            "frequency": random.choice(frequency),
            "details": "Maintain HR 120-140",
            "facilitator": random.choice(facilitators),
            "location": random.choice(locations),
            "remote_possible": random.choice([True, False]),
            "prep_requirements": random.sample(preparations, random.randint(1, 3)),
            "backup_activities": random.sample(activity_types, random.randint(1, 3)),
            "metrics": random.choice(metrics)
        }
        activities.append(activity)
    
    with open("activities_dataset.json", "w") as f:
        json.dump(activities, f, indent=4)
    return activities