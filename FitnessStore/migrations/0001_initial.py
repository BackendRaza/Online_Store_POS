# Generated by Django 2.1.5 on 2019-07-18 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Catagory',
            },
        ),
        migrations.CreateModel(
            name='custinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cfname', models.CharField(max_length=50)),
                ('cmail', models.CharField(max_length=50)),
                ('cpass', models.CharField(max_length=50)),
                ('ccontact', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'custinfo',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('plocation', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('pdesc', models.CharField(max_length=50)),
                ('prate', models.FloatField(default=0)),
                ('pimage', models.ImageField(default='Select Pic', upload_to='Images')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='subCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcatname', models.CharField(max_length=50)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FitnessStore.Catagory')),
            ],
            options={
                'db_table': 'subCatagory',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='subcat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FitnessStore.subCatagory'),
        ),
    ]
