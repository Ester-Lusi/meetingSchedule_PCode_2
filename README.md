# Comp Take-Home Exercise - Calendar Scheduler

A modular Python application for managing calendars and finding available meeting slots among participants. The codebase is organized following a simple clean architecture with distinct layers for models, persistence, business logic, and the user interface.

## Architecture 📐

The repository is structured to make each responsibility explicit:

- **`io_comp/`** – main package
  - `models.py` – domain objects (`Event`).
  - `repository.py` – abstract repository interface and an in‑memory implementation that also supports loading events from a CSV file.
  - `service.py` – business logic, including working‑hour enforcement and slot calculation.
  - `gui.py` – Tkinter GUI that interacts with the repository and service layers.
  - `app.py` – entry point that wires the components together and launches the application.

- **`resources/`** – supporting data files such as `calendar.csv` with example events.
- **`tests/`** – unit tests exercising the service logic and application behavior.
- `setup.py` and `requirements.txt` – packaging and dependencies.

This layout makes it easy to test and extend each part independently.

## Features ✅

- **Event Management** – add, remove, and load calendar events.
- **Availability Calculation** – compute common free slots within standard working hours (07:00–19:00).
- **GUI Interface** – intuitive Tkinter front end for managing events and searching for meeting times.
- **Data Persistence** – simple in‑memory store with CSV loading for sample data.

## Installation 💻

1. Ensure Python 3.8 or newer is installed.
2. Clone or download the project:
   ```sh
   git clone <repo-url>
   cd meetingSchedule_PCode_2
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   or, for editable/development installs:
   ```sh
   pip install -e .[dev]
   ```

## Usage 🚀

### GUI Application

Run the main application:
```sh
python -m io_comp.app
```
or, if installed as a package, via the console script:
```sh
comp-calendar
```

#### GUI Capabilities

- **Add Event**: enter a person name and time span.
- **Load CSV**: import events from `resources/calendar.csv`.
- **Delete Event**: select and remove an event.
- **Find Free Slots**: enter meeting duration and compute available times for all participants.

### Command‑Line

The app is designed for interactive use; there is no separate CLI beyond running the module.

## Testing 🧪

Execute the test suite with:
```sh
pytest
```

Tests focus on availability calculations, boundary conditions, and repository operations.

## Dependencies 📦

- Python 3.8+
- Tkinter (bundled with most Python installations)
- `pytest` (development/testing)

## License 📝

This repository is provided as a take‑home exercise for Comp.io. See internal licensing documentation for details.

