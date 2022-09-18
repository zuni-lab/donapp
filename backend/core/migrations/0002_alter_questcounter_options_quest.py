# Generated by Django 4.1.1 on 2022-09-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questcounter',
            options={'ordering': ['quest_id', 'user_id'], 'verbose_name': 'QuestCounter', 'verbose_name_plural': 'QuestCounters'},
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streamer_id', models.CharField(max_length=50, verbose_name='Streamer ID')),
                ('quest_id', models.CharField(max_length=100, verbose_name='Quest ID')),
            ],
            options={
                'verbose_name': 'Quest',
                'verbose_name_plural': 'Quests',
                'ordering': ['streamer_id', 'quest_id'],
                'unique_together': {('streamer_id', 'quest_id')},
            },
        ),
    ]
