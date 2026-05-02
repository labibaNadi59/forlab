from django.db import migrations

def add_vaccines(apps, schema_editor):
    Vaccine = apps.get_model('vaccination', 'Vaccine')
    vaccines = [
        ('BCG', 'Protects against Tuberculosis'),
        ('Hepatitis B', 'Protects against Hepatitis B virus'),
        ('DPT', 'Protects against Diphtheria, Pertussis, Tetanus'),
        ('Polio (OPV)', 'Oral Polio Vaccine'),
        ('Influenza', 'Protects against seasonal flu'),
        ('MMR', 'Protects against Measles, Mumps, Rubella'),
        ('Varicella', 'Protects against Chickenpox'),
        ('Hepatitis A', 'Protects against Hepatitis A virus'),
        ('Tdap', 'Tetanus, Diphtheria booster'),
        ('HPV', 'Protects against Human Papillomavirus'),
    ]
    for name, description in vaccines:
        Vaccine.objects.get_or_create(name=name, defaults={'description': description})


def remove_vaccines(apps, schema_editor):
    Vaccine = apps.get_model('vaccination', 'Vaccine')
    names = ['BCG', 'Hepatitis B', 'DPT', 'Polio (OPV)', 'Influenza',
             'MMR', 'Varicella', 'Hepatitis A', 'Tdap', 'HPV']
    Vaccine.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0001_initial'),  # ← fixed
    ]

    operations = [
        migrations.RunPython(add_vaccines, remove_vaccines),
    ]