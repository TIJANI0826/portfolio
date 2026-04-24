from django.shortcuts import render, get_object_or_404
from .models import Profile, SkillCategory, Experience, Project, Certification, Education, Achievement, Language


def home(request):
    profile = Profile.objects.filter(is_active=True).first()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    featured_projects = projects.filter(is_featured=True)
    certifications = Certification.objects.all()
    educations = Education.objects.all()
    achievements = Achievement.objects.all()
    languages = Language.objects.all()

    context = {
        'profile': profile,
        'skill_categories': skill_categories,
        'experiences': experiences,
        'projects': projects,
        'featured_projects': featured_projects,
        'certifications': certifications,
        'educations': educations,
        'achievements': achievements,
        'languages': languages,
        'total_skills': sum(cat.skills.count() for cat in skill_categories),
        'years_experience': 7,
    }
    return render(request, 'portfolio/home.html', context)
