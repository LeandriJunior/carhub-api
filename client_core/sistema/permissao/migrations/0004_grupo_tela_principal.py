# Generated by Django 4.2.7 on 2023-11-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissao', '0003_pontofuncaouser_grupouser'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='tela_principal',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
