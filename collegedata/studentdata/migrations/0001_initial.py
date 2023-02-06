# Generated by Django 4.1.5 on 2023-02-01 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('RollNo', models.AutoField(primary_key=True, serialize=False)),
                ('StudentName', models.CharField(max_length=500)),
                ('Year', models.IntegerField(null=True)),
                ('Batch', models.IntegerField(null=True)),
                ('DOB', models.DateTimeField(null=True)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentdata.departments')),
            ],
        ),
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('FacultieId', models.AutoField(primary_key=True, serialize=False)),
                ('FacultieName', models.CharField(max_length=500)),
                ('Salary', models.IntegerField(null=True)),
                ('DateOfJoining', models.DateField(null=True)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentdata.departments')),
            ],
        ),
    ]
