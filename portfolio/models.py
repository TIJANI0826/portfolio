from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=200, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)
    credly_url = models.URLField(blank=True)
    avatar = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, help_text="CSS class or emoji for icon")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    LEVEL_CHOICES = [
        (1, 'Beginner'),
        (2, 'Elementary'),
        (3, 'Intermediate'),
        (4, 'Advanced'),
        (5, 'Expert'),
    ]
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=3)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    @property
    def level_percent(self):
        return self.level * 20


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    company_url = models.URLField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(help_text="Use new lines for bullet points")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_date', 'order']

    def __str__(self):
        return f"{self.title} at {self.company}"

    @property
    def duration_str(self):
        end = "Present" if self.is_current else self.end_date.strftime("%b %Y")
        return f"{self.start_date.strftime('%b %Y')} – {end}"

    @property
    def bullet_points(self):
        return [line.strip() for line in self.description.split('\n') if line.strip()]


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=500, help_text="Comma-separated technologies")
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class Certification(models.Model):
    name = models.CharField(max_length=300)
    issuer = models.CharField(max_length=200)
    date_issued = models.DateField()
    credential_url = models.URLField(blank=True)
    credential_id = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-date_issued', 'order']

    def __str__(self):
        return f"{self.name} — {self.issuer}"


class Education(models.Model):
    institution = models.CharField(max_length=300)
    degree = models.CharField(max_length=300)
    field = models.CharField(max_length=200, blank=True)
    grade = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} — {self.institution}"

    @property
    def duration_str(self):
        end = "Present" if self.is_current else (self.end_date.strftime("%b %Y") if self.end_date else "")
        return f"{self.start_date.strftime('%b %Y')} – {end}"


class Achievement(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    metric = models.CharField(max_length=100, blank=True, help_text="e.g. '60% reduction', '5000+ users'")
    icon = models.CharField(max_length=50, blank=True, help_text="Emoji or icon class")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Language(models.Model):
    LEVEL_CHOICES = [
        ('native', 'Native'),
        ('advanced', 'Advanced'),
        ('intermediate', 'Intermediate'),
        ('basic', 'Basic'),
    ]
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='intermediate')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.level})"
