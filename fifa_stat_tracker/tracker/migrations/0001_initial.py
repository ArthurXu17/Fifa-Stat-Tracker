# Generated by Django 4.2.3 on 2023-08-06 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minute', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opponent', models.CharField(max_length=20)),
                ('round', models.CharField(choices=[('GR', 'Group Stage'), ('R16', 'Round of 16'), ('QF', 'Quarter Finals'), ('SF', 'Semi Finals'), ('F', 'Finals')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Shot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_target', models.BooleanField()),
                ('blocked_by_player', models.BooleanField()),
                ('body_part', models.CharField(choices=[('Foot', 'Foot'), ('Head', 'Head')], max_length=10)),
                ('minute', models.IntegerField()),
                ('corner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.corner')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.player')),
            ],
            options={
                'default_related_name': 'shots',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='tracker.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.team'),
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_part', models.CharField(choices=[('Foot', 'Foot'), ('Head', 'Head')], max_length=10)),
                ('minute', models.IntegerField()),
                ('is_impressive_assist', models.BooleanField(blank=True, null=True)),
                ('is_impressive_goal', models.BooleanField()),
                ('assist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goals_assisted_on', to='tracker.player')),
                ('corner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.corner')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.player')),
            ],
            options={
                'default_related_name': 'goals',
            },
        ),
        migrations.AddField(
            model_name='corner',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corners', to='tracker.match'),
        ),
    ]
