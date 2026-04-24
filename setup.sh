#!/bin/bash
# ================================================
# Ibrahim Tijani Portfolio — Setup Script
# ================================================
# Run this once to set up the project:
#   chmod +x setup.sh && ./setup.sh
# ================================================

echo ""
echo "🚀 Setting up Ibrahim Tijani Portfolio..."
echo "========================================="

# 1. Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# 3. Run migrations
echo ""
echo "🗄️  Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# 4. Seed data
echo ""
echo "🌱 Seeding portfolio data..."
python seed_data.py

# 5. Create superuser prompt
echo ""
echo "👤 Creating admin superuser..."
echo "   (You'll use these credentials to log into /admin/)"
python manage.py createsuperuser

# 6. Collect static files
echo ""
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "✅ Setup complete!"
echo ""
echo "▶️  To start the server:"
echo "   source venv/bin/activate"
echo "   python manage.py runserver"
echo ""
echo "🌐 Then open: http://127.0.0.1:8000"
echo "🔧 Admin panel: http://127.0.0.1:8000/admin"
echo ""
