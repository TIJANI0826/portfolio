from django.contrib import admin
from .models import Profile, SkillCategory, Skill, Experience, Project, Certification, Education, Achievement, Language

admin.site.site_header = "Ibrahim Tijani — Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Manage Your Portfolio"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'is_active']
    fieldsets = (
        ('Personal Info', {'fields': ('name', 'title', 'email', 'phone', 'location', 'avatar', 'resume_file', 'is_active')}),
        ('Summary', {'fields': ('summary',)}),
        ('Social Links', {'fields': ('linkedin', 'github', 'portfolio_url', 'credly_url')}),
    )


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 3
    fields = ['name', 'level', 'order']


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order']
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'level', 'order']
    list_filter = ['category', 'level']
    list_editable = ['level', 'order']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['is_current']
    list_editable = ['order']
    ordering = ['-start_date']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'order']
    list_editable = ['is_featured', 'order']
    list_filter = ['is_featured']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuer', 'date_issued', 'order']
    list_editable = ['order']
    ordering = ['-date_issued']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current']
    ordering = ['-start_date']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'metric', 'date', 'order']
    list_editable = ['order']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'order']
    list_editable = ['level', 'order']
