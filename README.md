# Resource Allocator

A Python-based resource allocator system that generates and manages activity plans based on facilitator availability and activity frequencies.

## Features

- Activity generation with various types, frequencies, and facilitators
- Availability tracking for different facilitators
- Smart scheduling considering:
  - Maximum daily activities
  - Weekly frequency limits
  - Facilitator availability
  - Backup activities

## Usage

1. Generate sample data:
```python
python generate_activity.py    # Creates activities_dataset.json
python generate_availability.py # Creates availability_dataset.json
```

2. Run the scheduler:
```python
python scheduler.py           # Creates schedule.json
```

