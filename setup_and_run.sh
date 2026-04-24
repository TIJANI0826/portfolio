#!/bin/bash
# ================================================
# Ibrahim Tijani Portfolio — Quick Setup Script
# ================================================
set -e

echo ""
echo "╔══════════════════════════════════════════╗"
echo "║   Ibrahim Tijani Portfolio — Setup       ║"
echo "╚══════════════════════════════════════════╝"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install django pillow --break-system-packages --quiet

# Run migrations
echo "🗄️  Running database migrations..."
python manage.py makemigrations portfolio
python manage.py migrate

# Seed data
echo "🌱 Seeding portfolio data..."
python seed_data.py

# Create superuser (non-interactive)
echo ""
echo "👤 Creating admin user..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'ibrahimtijani08@gmail.com', 'admin1234')
    print('   Admin created: username=admin, password=admin1234')
else:
    print('   Admin user already exists')
"

echo ""
echo "✅ Setup complete!"
echo ""
echo "   🌐 Portfolio:  http://127.0.0.1:8000/"
echo "   🔧 Admin:      http://127.0.0.1:8000/admin/"
echo "   👤 Username:   admin"
echo "   🔑 Password:   admin1234"
echo ""
echo "▶  Starting server..."
echo ""
python manage.py runserver
