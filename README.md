# Comp Take-Home Exercise - Calendar Scheduler

A Python application for managing calendars and finding available meeting slots among multiple participants. This project implements a simple calendar service with a GUI for adding, loading, and deleting events, and calculating free time slots.

## Features

- **Event Management**: Add, load from CSV, and delete calendar events.
- **Availability Calculation**: Find common free slots for a group of people within working hours (07:00 - 19:00).
- **GUI Interface**: Built with Tkinter for easy interaction.
- **Data Persistence**: In-memory repository with CSV loading support.

## Installation

1. Ensure you have Python 3.8 or higher installed.
2. Clone or download the project.
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   Or for development:
   ```sh
   pip install -e .[dev]
   ```

## Usage

### Running the GUI Application

Execute the application:
```sh
python -m io_comp.app
```
Or use the console script:
```sh
comp-calendar
```

### GUI Features

- **Add Event**: Enter person name, start time, and end time to add a manual event.
- **Load CSV**: Load events from [`resources/calendar.csv`](resources/calendar.csv ).
- **Delete Event**: Select an event from the table and delete it.
- **Find Free Slots**: Specify meeting duration and calculate available slots for all participants.

### Command-Line Usage

The application can be run as a script, but primarily uses the GUI.

## Testing

Run tests with pytest:
```sh
pytest
```

Tests cover availability calculations, working hour limits, and event clipping.

## Project Structure

- [`io_comp`](io_comp ): Main package containing the application logic.
  - [`io_comp/app.py`](io_comp/app.py ): Core classes and GUI implementation.
- [`tests`](tests ): Unit tests.
- [`resources`](resources ): Sample CSV data.
- [`setup.py`](setup.py ): Package configuration.

## Dependencies

- Python 3.8+
- Tkinter (usually included with Python)
- pytest (for testing)

## License

This is a take-home exercise project. Refer to Comp.io for licensing details.
