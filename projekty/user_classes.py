#w tym pliku definiujemy grupy użytkowników i nadajemy im odpowiednie uprawnienia
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from .models import Project, Experiment


#trzy grupy, admin, kierownik, laborant

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    if sender.name == 'projekty':
        # admin
        admin_group, created = Group.objects.get_or_create(name='Admin')

        # kierownik
        kierownik_group, created = Group.objects.get_or_create(name='Kierownik')
        projects_ct = ContentType.objects.get_for_model(Project)
        experiments_ct = ContentType.objects.get_for_model(Experiment)
        
        add_project_perm = Permission.objects.get(codename='add_projects', content_type=projects_ct)
        change_experiment_perm = Permission.objects.get(codename='change_experiments', content_type=experiments_ct)
        
        kierownik_group.permissions.add(add_project_perm)
        kierownik_group.permissions.add(change_experiment_perm)
        
        # laborant
        laborant_group, created = Group.objects.get_or_create(name='Laborant')
        view_project_perm = Permission.objects.get(codename='view_projects', content_type=projects_ct)
        change_experiment_perm = Permission.objects.get(codename='change_experiments', content_type=experiments_ct)
        
        laborant_group.permissions.add(view_project_perm)
        laborant_group.permissions.add(change_experiment_perm)