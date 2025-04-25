# OneMaster
One Master is a Client Relationship Management (CRM) system designed for personal fitness trainers working in gyms. This platform helps trainers manage their clients, track attendance, monitor payments, schedule workout plans, and analyze performance — all in one place.

It's ideal for trainers who want to move from paper notebooks and messy spreadsheets to a smart digital solution.

## 🚀 Key Features
 - 👥 Client Management: Add, edit, and organize client profiles with detailed health and training info.

 - 📆 Attendance Tracking: Log when clients attend sessions and identify inactive members.

 - 💳 Payment Tracking: Manage payment history, debts, and income reports.

 - 🏋️ Workout Planning: Create, update, and assign training schedules to clients.

 - 📊 Analytics Dashboard: Get insights on income, client activity, and performance.

 - 🏢 Multi-Gym Support: Trainers can work with one or more fitness clubs.

 - 🔐 User Roles & Authentication: Trainers, admins, and future client logins.

 - 🧩 Project Structure (Django Apps)

App Name | Description
fitness_clubs | Manage gyms and fitness club details
trainers | Trainer profiles linked to Django users
clients | Manage clients, health data, and workout notes
visits | Track when clients attend sessions
payments | Record client payments and financial summaries
dashboard | Data analytics and performance charts
accounts | User authentication and role management

## 🛠️ Technologies

  - Python 3.11+

  - Django 5.2

  - PostgreSQL

  - Django Rest Framework (planned)

  - Bootstrap or Tailwind CSS (for frontend)

  - Docker (deployment, coming soon)

## 🔮 Roadmap
 
 - Mobile app (React Native or Flutter)

 - Telegram/SMS notifications

 - Automated reminders for sessions and payments

 - Subscription support (monthly memberships)

 - Client progress visualization (charts, graphs)

 - Admin panel for gym managers

⚙️ Installation (Work in Progress)
bash

```bash
git clone https://github.com/yourusername/FitnessTrainerCRM.git
cd OneMaster
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
🤝 Author
Shavkat
Student @ PDP University, Tashkent
Passionate about Python, backend systems, and building real-world projects

📌 Project Status
🚧 Actively under development.
Feedback, ideas, and contributions are always welcome!

