# Ibrahim Adewale Tijani — Portfolio Website

A modern, fully dynamic Django portfolio application pre-loaded with Ibrahim Tijani's CV data. Every section is manageable through the Django admin panel.

---

## 🚀 Quick Start

### 1. Clone / Extract the project

Place the project folder somewhere on your machine.

### 2. Create and activate a virtual environment

```bash
cd portfolio
python3 -m venv venv
source venv/bin/activate       # Linux / macOS
# OR
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Seed your portfolio data (Ibrahim's CV data pre-loaded)

```bash
python seed_data.py
```

### 6. Create an admin superuser

```bash
python manage.py createsuperuser
```
Enter a username, email, and password when prompted.

### 7. Start the development server

```bash
python manage.py runserver
```

Open your browser at **http://127.0.0.1:8000**

---

## 🔧 Managing Your Portfolio

Visit **http://127.0.0.1:8000/admin** and log in with the superuser credentials you created.

### What you can manage:

| Section | Model | What you can do |
|---|---|---|
| **Profile** | Profile | Name, title, summary, contact info, social links, photo, resume |
| **Skills** | SkillCategory + Skill | Add/edit/reorder skill categories and individual skills with proficiency levels |
| **Experience** | Experience | Add jobs, edit bullet points, mark current roles |
| **Projects** | Project | Add projects, mark featured, add tech stack tags and links |
| **Certifications** | Certification | Add/remove certifications with dates and verification links |
| **Education** | Education | Degrees, institutions, grades |
| **Achievements** | Achievement | Quantified achievements with metrics and icons |
| **Languages** | Language | Language proficiency levels |

---

## 📁 Project Structure

```
portfolio/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── seed_data.py                 # Pre-loads Ibrahim's CV data
├── setup.sh                     # One-command setup script
├── db.sqlite3                   # Database (created after migrate)
│
├── portfolio/                   # Django app
│   ├── models.py                # All data models
│   ├── views.py                 # Page views
│   ├── admin.py                 # Admin panel configuration
│   ├── settings.py              # Django settings
│   └── urls.py                  # URL routing
│
├── templates/
│   └── portfolio/
│       └── home.html            # Main portfolio page template
│
└── static/
    ├── css/
    │   └── portfolio.css        # All styles
    └── js/
        └── portfolio.js         # Animations & interactions
```

---

## 🎨 Design

- **Font**: Syne (display/headings) + DM Sans (body)
- **Theme**: Dark editorial with amber/orange gradient accents
- **Sections**: Hero → About → Experience → Skills → Projects → Certifications → Contact
- **Features**: Animated skill bars, counter animations, typing effect, parallax orbs, smooth scroll, mobile-responsive

---

## 🌐 Deployment (PythonAnywhere)

Since Ibrahim is already on PythonAnywhere:

1. Upload project files
2. Create a virtual environment and install `requirements.txt`
3. Set `DEBUG = False` and update `ALLOWED_HOSTS` in `settings.py`
4. Run `python manage.py collectstatic`
5. Configure the WSGI file in PythonAnywhere dashboard
6. Set `STATIC_ROOT` static files mapping in the web app settings

---

## 🔒 Production Checklist

Before going live:
- [ ] Change `SECRET_KEY` to a random secret (use `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- [ ] Set `DEBUG = False`
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Set up proper email backend if needed
- [ ] Enable HTTPS

---

## ✉️ Contact

Ibrahim Adewale Tijani · ibrahimtijani08@gmail.com · Abuja, Nigeria
