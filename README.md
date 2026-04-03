# EECE430 – Assignment 4: Volleyball Player List Manager

A simple **Python-Django** web application that manages a volleyball player list with full **CRUD** (Create, Read, Update, Delete) functionality, implementing both frontend and backend.

---

## Project Structure

```
volleyballproject/
├── manage.py                  # Django management script
├── db.sqlite3                 # SQLite database (auto-created)
├── venv/                      # Python virtual environment
├── volleysite/                # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── players/                   # Main app
│   ├── models.py              # VolleyPlayer model
│   ├── views.py               # CRUD views
│   ├── forms.py               # ModelForm for player
│   ├── urls.py                # URL routes
│   ├── admin.py               # Admin site registration
│   └── tests.py               # Unit tests (7 tests)
└── templates/players/         # HTML templates
    ├── base.html              # Base layout with navbar
    ├── player_list.html       # List all players (READ)
    ├── player_form.html       # Add / Edit player form
    ├── player_detail.html     # View single player details
    └── player_confirm_delete.html  # Delete confirmation
```

## Player Model Fields

| Field           | Type          | Description                      |
|-----------------|---------------|----------------------------------|
| `player_id`     | AutoField (PK)| Auto-generated unique ID         |
| `name`          | CharField     | Player's full name               |
| `date_joined`   | DateField     | Date the player joined the team  |
| `position`      | CharField     | Player position (dropdown list)  |
| `salary`        | DecimalField  | Salary / payment amount          |
| `contact_person` | CharField    | Name of the contact person       |

**Available positions:** Setter, Outside Hitter, Middle Blocker, Opposite Hitter, Libero, Defensive Specialist.

## CRUD Operations

| Operation | URL                     | Description                |
|-----------|-------------------------|----------------------------|
| **C**reate | `/add/`                | Add a new player           |
| **R**ead   | `/` (list all)         | View all players in a table|
| **R**ead   | `/player/<id>/`        | View a single player       |
| **U**pdate | `/player/<id>/edit/`   | Edit an existing player    |
| **D**elete | `/player/<id>/delete/` | Delete a player (with confirmation) |

## How to Run

1. **Open a terminal** and navigate to the project folder:
   ```
   cd volleyballproject
   ```

2. **Activate the virtual environment:**
   ```
   .\venv\Scripts\Activate.ps1       # Windows PowerShell
   # or
   venv\Scripts\activate.bat         # Windows CMD
   ```

3. **Run migrations** (only needed the first time):
   ```
   python manage.py migrate
   ```

4. **Start the development server:**
   ```
   python manage.py runserver
   ```

5. **Open your browser** and go to: [http://127.0. 0.1:8000/](http://127.0.0.1:8000/)

## Manual Testing Steps

1. Go to `http://127.0.0.1:8000/` → You should see an empty player list.
2. Click **"+ Add New Player"** → Fill in the form and submit → Player appears in the list.
3. Click **"View"** on any player → See full details.
4. Click **"Edit"** → Modify fields and save → Changes are reflected.
5. Click **"Delete"** → Confirm → Player is removed from the list.

## Technologies Used

- **Python 3.x**
- **Django 6.0.3**
- **SQLite** (default database)
- **HTML/CSS** (frontend, no external libraries needed)
