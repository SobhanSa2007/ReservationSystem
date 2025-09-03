Reservation System 🗓️ (Django FrameWork)

A simple reservation system built for fun and learning new things.

Features:
- 🚫 No Authentication → uses sessions instead of user accounts
- 📅 Calendar view → shows the current month with available days
- ⏰ Limited capacity by time slots
- 👀 View your own reservations
- ❌ Fully booked days are disabled
- ⏳ Past days are disabled

---------------------------------------

Installation/How to run:

Clone the repository:
```bash
git clone https://github.com/your-username/reservation-system.git
cd reservation-system
```
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run migrations:
```bash
python manage.py migrate
```
Start the development server/Run project:
```bash
python manage.py runserver
```

Now open your browser and go to: http://127.0.0.1:8000
