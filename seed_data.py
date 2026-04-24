import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from portfolio.models import Profile, SkillCategory, Skill, Experience, Project, Certification, Education, Achievement, Language
from datetime import date

print("Seeding portfolio data...")

# Profile
profile, _ = Profile.objects.get_or_create(
    email='ibrahimtijani08@gmail.com',
    defaults={
        'name': 'Ibrahim Adewale Tijani',
        'title': 'Senior Data Analyst & Full-Stack Developer',
        'summary': (
            'Results-driven Senior Data Analyst & IT professional with 7+ years of experience translating complex business '
            'and product questions into actionable insights. Proven expertise in SQL, Python (Pandas, NumPy, SciPy, Matplotlib, Seaborn), '
            'BigQuery, Django, and cloud-based data pipelines. Hands-on experience engineering data for predictive modelling, '
            'building self-service dashboards, and delivering end-to-end analytics across product development lifecycles. '
            'Adept at designing and analysing experiments (A/B and multivariate tests), applying statistical modelling techniques, '
            'and partnering cross-functionally with product, engineering, marketing, and growth teams to drive measurable business impact — '
            'including user acquisition, retention, and product engagement at scale.'
        ),
        'phone': '08141994147',
        'location': 'Abuja, Nigeria',
        'linkedin': 'https://www.linkedin.com/in/ibrahim-tijani-adewale',
        'github': 'https://github.com/TIJANI0826',
        'portfolio_url': 'https://tijani.pythonanywhere.com/',
        'credly_url': 'https://www.credly.com/users/ibrahim-tijani.87cecd14',
        'is_active': True,
    }
)
print(f"  ✓ Profile: {profile.name}")

# Skill Categories
skills_data = [
    ('Analytics & SQL', '📊', [
        ('Advanced SQL (BigQuery, CloudSQL)', 5),
        ('A/B Testing & Multivariate Testing', 5),
        ('Statistical Modelling', 4),
        ('Regression Analysis', 4),
        ('Clustering & Supervised Learning', 4),
        ('ETL/ELT Pipelines', 4),
        ('Data Wrangling', 5),
        ('Funnel & Cohort Analysis', 5),
    ]),
    ('Python & Libraries', '🐍', [
        ('Python', 5),
        ('Pandas', 5),
        ('NumPy', 5),
        ('SciPy', 4),
        ('Matplotlib / Seaborn', 5),
        ('Jupyter Notebooks', 5),
        ('Bash / Scripting', 4),
    ]),
    ('Cloud & Data Infrastructure', '☁️', [
        ('Google BigQuery', 5),
        ('BigQuery ML', 4),
        ('DataFlow & DataProc', 4),
        ('Vertex AI & TensorFlow', 3),
        ('Google Cloud Storage', 4),
        ('AWS EC2', 4),
        ('Docker & DockerHub', 4),
        ('GitHub Actions / CI/CD', 4),
    ]),
    ('Web Development', '🌐', [
        ('Django', 5),
        ('JavaScript', 4),
        ('HTML / CSS / Bootstrap', 5),
        ('MySQL / MariaDB', 4),
        ('REST API Integration', 5),
        ('ERPNext / Frappe', 4),
    ]),
    ('Visualisation & BI', '📈', [
        ('Looker / Data Studio', 4),
        ('Tableau', 3),
        ('Advanced Excel', 5),
        ('AppSheet', 4),
        ('Power BI (Conceptual)', 3),
    ]),
    ('Systems & Platforms', '🛠️', [
        ('Splynx', 4),
        ('Proxmox', 3),
        ('Mailcow / Nextcloud', 3),
        ('Chatwoot', 4),
        ('SmartOLT', 3),
        ('Linux Server Admin', 4),
    ]),
]

for order, (cat_name, icon, skills) in enumerate(skills_data):
    cat, _ = SkillCategory.objects.get_or_create(name=cat_name, defaults={'icon': icon, 'order': order})
    for s_order, (skill_name, level) in enumerate(skills):
        Skill.objects.get_or_create(category=cat, name=skill_name, defaults={'level': level, 'order': s_order})
print(f"  ✓ Skills seeded")

# Experiences
experiences = [
    {
        'title': 'System Administrator / Web Developer',
        'company': 'Dotmac Fiber',
        'start_date': date(2025, 2, 1),
        'is_current': True,
        'description': (
            'Developed and customized internal and customer-facing web applications using Python, Django, JavaScript, and modern UI frameworks.\n'
            'Designed, maintained, and optimized MySQL/MariaDB databases; improved query performance and ensured data integrity.\n'
            'Integrated APIs and third-party systems including ERPNext, Splynx, GIS platforms, and payment gateways.\n'
            'Built backend workflows for customer management, billing automation, IP allocation, and service provisioning.\n'
            'Provided technical support, documentation, and user guidance for internal teams to enhance application usage.'
        ),
        'order': 0,
    },
    {
        'title': 'Python Instructor',
        'company': 'TIIDELAB',
        'start_date': date(2024, 6, 1),
        'end_date': date(2024, 7, 31),
        'is_current': False,
        'description': (
            'Designed data-driven Python curriculum covering statistical computing, data analysis, and machine learning, adapting content to diverse learning styles.\n'
            'Mentored 20+ students on hands-on data projects using Pandas, NumPy, and Matplotlib, building analytical problem-solving skills.\n'
            'Assessed learner performance with structured feedback loops, tracking individual progress metrics and improving cohort pass rates.'
        ),
        'order': 1,
    },
    {
        'title': 'Web Developer',
        'company': 'Delainah Optimah',
        'company_url': '',
        'start_date': date(2024, 2, 1),
        'is_current': True,
        'description': (
            'Built and maintained an e-commerce platform serving 5,000+ monthly users, integrating Payment System APIs processing 1,000+ monthly transactions at a 99% success rate.\n'
            'Instrumented key product metrics and monitored KPIs including transaction volume, success rates, and user retention, ensuring 100% database availability.\n'
            'Implemented data-backed security optimisations (SSL, routing), reducing security incidents by 50%.'
        ),
        'order': 2,
    },
    {
        'title': 'Web Developer',
        'company': 'FastsubData',
        'start_date': date(2023, 2, 1),
        'end_date': date(2024, 2, 28),
        'is_current': False,
        'description': (
            'Integrated and monitored multiple payment and messaging APIs (Monnify, Paystack, Husmodataapi, BulkSMS), handling 500+ daily API calls.\n'
            'Analysed API usage patterns and transaction data to identify bottlenecks, improving system throughput and development speed by 30%.'
        ),
        'order': 3,
    },
    {
        'title': 'ICT Instructor',
        'company': 'I-Scholars International Academy',
        'start_date': date(2019, 9, 1),
        'end_date': date(2025, 2, 28),
        'is_current': False,
        'description': (
            'Taught information communication technology, data processing and web authoring to secondary school students.\n'
            'Prepared learners for examinations including WAEC and IGCSE with 100% effective modern teaching methods.\n'
            'Designed evaluation tools to build students critical-thinking skills.\n'
            'Taught Scratch programming to Grade 1–5 pupils during the COVID lockdown in 2020.'
        ),
        'order': 4,
    },
    {
        'title': 'Web Developer',
        'company': 'Amshatib Projects Limited',
        'start_date': date(2022, 2, 1),
        'end_date': date(2023, 2, 28),
        'is_current': False,
        'description': (
            'Developed and deployed a data-driven web platform that increased site traffic by 40%, leveraging analytics to identify high-performing content.\n'
            'Directed CI/CD pipelines via GitHub Actions, reducing deployment time by 20% and improving data pipeline reliability.'
        ),
        'order': 5,
    },
    {
        'title': 'Cloud & Data Engineering Participant',
        'company': 'SUSE Scholarship — Udacity',
        'start_date': date(2021, 6, 1),
        'end_date': date(2022, 2, 28),
        'is_current': False,
        'description': (
            'Containerised and deployed Python data applications to DockerHub using Git Actions, reducing deployment errors by 25%.\n'
            'Gained hands-on experience with cloud infrastructure monitoring and automated scaling for high-availability data pipelines.'
        ),
        'order': 6,
    },
    {
        'title': 'Python Developer',
        'company': 'Workie',
        'start_date': date(2017, 12, 1),
        'end_date': date(2021, 6, 7),
        'is_current': False,
        'description': (
            'Deployed and monitored AWS EC2 instances with automated alerting systems, maintaining 99.9% uptime and reducing downtime costs by 20%.\n'
            'Monitored application scaling and performance metrics, optimising resource allocation and reducing operational costs by 15%.\n'
            'Deployed ERPNext application to DockerHub, enabling seamless data management and reporting for 100+ users.'
        ),
        'order': 7,
    },
    {
        'title': 'IT & Data Intern',
        'company': 'Intelligent Mechatronics Plus Limited',
        'location': 'Minna',
        'start_date': date(2016, 2, 1),
        'end_date': date(2017, 12, 31),
        'is_current': False,
        'description': (
            'Conducted in-depth research on the NCC-sponsored Multiple Operator Enable SIM Card (MOES) project, analysing data for 10,000+ users.\n'
            'Created a SIM Toolkit application in Python, streamlining user operations and improving efficiency by 20%.\n'
            'Delivered data-backed web solutions that increased user engagement by 50% and average session duration by 20%.'
        ),
        'order': 8,
    },
]

for exp_data in experiences:
    Experience.objects.get_or_create(
        title=exp_data['title'],
        company=exp_data['company'],
        start_date=exp_data['start_date'],
        defaults=exp_data,
    )
print(f"  ✓ Experiences seeded")

# Projects
projects = [
    {
        'title': 'OLT Management Application',
        'description': 'Designed and developed a full web-based OLT Management System enabling automated OLT configuration, service-port creation, VLAN mapping, ONT onboarding, and GPON monitoring — reducing manual configuration time by 60%.',
        'tech_stack': 'Python, Django, JavaScript, MySQL, GPON/OLT APIs',
        'is_featured': True,
        'order': 0,
    },
    {
        'title': 'Business Intelligence AI Query Engine',
        'description': 'Developed an AI-powered BI application using the Frappe Framework that allows staff to query ERP data via natural language. Implemented SQL auto-generation, dashboards, and unified ERPNext/Splynx metadata — reducing report generation time to under 10 minutes.',
        'tech_stack': 'Python, Frappe, ERPNext, Splynx, AI/NLP, SQL',
        'is_featured': True,
        'order': 1,
    },
    {
        'title': 'Custom Chatwoot Reporting System',
        'description': 'Built a custom reporting and analytics platform by integrating Chatwoot Webhooks and API endpoints to track conversations, agent performance, response times, and customer interactions — improving support reporting accuracy by 70%.',
        'tech_stack': 'Python, Chatwoot API, Webhooks, Django, Analytics',
        'is_featured': True,
        'order': 2,
    },
    {
        'title': 'ERPNext Deployment for SON',
        'description': 'Led the deployment, configuration, and customization of ERPNext for the Standards Organisation of Nigeria (SON). Set up modules, optimized permissions, performed server deployment, and trained staff — resulting in smooth system adoption.',
        'tech_stack': 'ERPNext, Frappe, Docker, Linux, MySQL',
        'is_featured': True,
        'order': 3,
    },
    {
        'title': 'Build a Data Warehouse with BigQuery',
        'description': 'Designed and implemented a scalable data warehouse on Google BigQuery, integrating multiple data sources via ETL pipelines and optimising query performance for large-scale analytics.',
        'tech_stack': 'BigQuery, SQL, ETL, Google Cloud',
        'is_featured': False,
        'order': 4,
    },
    {
        'title': 'Engineer Data for Predictive Modelling with BigQuery ML',
        'description': 'Prepared and engineered feature-rich datasets for predictive modelling; built, trained, and evaluated ML models directly in BigQuery, iterating on model accuracy.',
        'tech_stack': 'BigQuery ML, DataFlow, Data Pipelines, Google Cloud',
        'is_featured': False,
        'order': 5,
    },
    {
        'title': 'Sea Level Predictor',
        'description': 'Developed a linear regression model to forecast future sea level changes from historical data, visualising predictions with Matplotlib for clear stakeholder communication.',
        'tech_stack': 'Python, NumPy, Pandas, Matplotlib, Linear Regression',
        'is_featured': False,
        'order': 6,
    },
    {
        'title': 'Medical Data Visualiser',
        'description': 'Designed visualisation dashboards to surface trends and anomalies in patient medical records, supporting data-driven healthcare decision-making.',
        'tech_stack': 'Pandas, Matplotlib, Seaborn',
        'is_featured': False,
        'order': 7,
    },
    {
        'title': 'Page View Time Series Visualiser',
        'description': 'Built a time series analysis tool applying data wrangling and statistical visualisation (line, bar, box plots) to identify trends and distributions in web traffic data.',
        'tech_stack': 'Pandas, NumPy, Matplotlib',
        'is_featured': False,
        'order': 8,
    },
]

for proj_data in projects:
    Project.objects.get_or_create(title=proj_data['title'], defaults=proj_data)
print(f"  ✓ Projects seeded")

# Certifications
certs = [
    ('Applied Data Science I: Scientific Computing & Python (With Honours)', 'WorldQuant University', date(2020, 6, 1), ''),
    ('Data Fundamentals', 'IBM SkillsBuild', date(2024, 10, 1), ''),
    ('Build a Data Warehouse with BigQuery', 'Google Cloud', date(2024, 5, 1), ''),
    ('Prepare Data for ML APIs on Google Cloud', 'Google Cloud', date(2024, 5, 1), ''),
    ('Derive Insights from BigQuery Data', 'Google Cloud', date(2024, 4, 1), ''),
    ('Engineer Data for Predictive Modelling with BigQuery ML', 'Google Cloud', date(2024, 4, 1), ''),
    ('App Building with AppSheet', 'Google Cloud', date(2025, 3, 1), ''),
    ('Data Analysis with Python', 'FreeCodeCamp', date(2023, 11, 1), ''),
    ('MS Excel: Analyzing and Visualizing Data', 'Udemy', date(2023, 6, 1), ''),
    ('Scientific Computing with Python', 'FreeCodeCamp', date(2021, 6, 1), ''),
    ('Project Management Professional (PMP)', 'PMI', date(2019, 6, 1), ''),
    ('Web Development Fundamentals', 'IBM SkillsBuild', date(2024, 8, 1), ''),
    ('JavaScript Algorithm and Data Structure', 'FreeCodeCamp', date(2021, 8, 1), ''),
    ('Responsive Web Design', 'FreeCodeCamp', date(2020, 7, 1), ''),
]

for i, (name, issuer, date_issued, url) in enumerate(certs):
    Certification.objects.get_or_create(name=name, issuer=issuer, defaults={'date_issued': date_issued, 'credential_url': url, 'order': i})
print(f"  ✓ Certifications seeded")

# Education
educations = [
    {
        'institution': 'Federal University of Technology, Minna',
        'degree': 'B.Tech in Computer Science',
        'field': 'Computer Science',
        'grade': 'Second Class Upper (Hons)',
        'start_date': date(2013, 10, 1),
        'end_date': date(2017, 11, 30),
        'is_current': False,
        'order': 0,
    },
    {
        'institution': 'Oyun Baptist High School, Ijagbo',
        'degree': 'Senior Secondary Education',
        'field': 'WAEC & NECO',
        'grade': '',
        'start_date': date(2007, 1, 1),
        'end_date': date(2010, 12, 31),
        'is_current': False,
        'order': 1,
    },
]

for edu in educations:
    Education.objects.get_or_create(institution=edu['institution'], degree=edu['degree'], defaults=edu)
print(f"  ✓ Education seeded")

# Achievements
achievements_data = [
    ('60% Reduction in OLT Configuration Time', 'Automated OLT configuration, service-port creation, VLAN mapping, and ONT onboarding through the OLT Management Application.', '60% faster', '⚡', 0),
    ('70% Improvement in Support Reporting Accuracy', 'Custom Chatwoot Reporting System integrated webhooks and API endpoints to track conversations and agent performance.', '70% accuracy gain', '📊', 1),
    ('5,000+ Monthly Users Served', 'E-commerce platform at Delainah Optimah serving over 5,000 monthly users with 99% payment transaction success rate.', '5,000+ users', '🛒', 2),
    ('99.9% System Uptime at Workie', 'Directed AWS EC2 instance deployment with automated monitoring and alert systems, significantly reducing downtime costs by 20%.', '99.9% uptime', '🟢', 3),
    ('50% Security Incident Reduction', 'Implemented SSL and proper routing for e-commerce platform, protecting user data and reducing security incidents by half.', '50% fewer incidents', '🔐', 4),
    ('10,000+ SIM Users Analysed', 'Conducted in-depth research on the NCC-sponsored Multiple Operator Enable SIM Card (MOES) project with data for over 10,000 users.', '10,000+ users', '📱', 5),
    ('Report Generation Under 10 Minutes', 'AI-powered BI application reduced report generation time from hours to under 10 minutes using natural language SQL auto-generation.', '<10 min reports', '🤖', 6),
    ('40% Traffic Increase at Amshatib', 'Developed and deployed a data-driven web platform that increased site traffic by 40% through analytics-guided content strategy.', '40% more traffic', '📈', 7),
]

for title, desc, metric, icon, order in achievements_data:
    Achievement.objects.get_or_create(title=title, defaults={'description': desc, 'metric': metric, 'icon': icon, 'order': order})
print(f"  ✓ Achievements seeded")

# Languages
languages_data = [
    ('English', 'advanced', 0),
    ('Arabic', 'advanced', 1),
    ('Yoruba', 'native', 2),
    ('Hausa', 'advanced', 3),
]
for name, level, order in languages_data:
    Language.objects.get_or_create(name=name, defaults={'level': level, 'order': order})
print(f"  ✓ Languages seeded")

print("\n✅ All data seeded successfully!")
