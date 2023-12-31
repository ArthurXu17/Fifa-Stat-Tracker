# Generated by Django 4.2.3 on 2023-08-20 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_alter_goal_body_part_alter_shot_body_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('LF', 'Left Forward'), ('CF', 'Centre Forward'), ('RF', 'Right Forward'), ('LM', 'Left Midfield'), ('CM', 'Centre Midfield'), ('RM', 'Right Midfield'), ('LB', 'Left Back'), ('CB', 'Centre Back'), ('RB', 'Right Back'), ('GK', 'Goalkeeper')], max_length=20, null=True),
        ),
    ]
