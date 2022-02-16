# Generated by Django 2.1.5 on 2019-07-21 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FitnessStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FitnessStore.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FitnessStore.custinfo')),
            ],
        ),
    ]
