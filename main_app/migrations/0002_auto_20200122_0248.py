# Generated by Django 2.2.9 on 2020-01-22 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skincare',
            name='cons',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='skincare',
            name='pros',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='skincare',
            name='star_ingredients',
            field=models.TextField(max_length=255),
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('0', 'No change'), ('10', 'Great!'), ('STR', 'Start product'), ('FIN', 'Finish product'), ('OIL', 'Oily'), ('DRY', 'Dry'), ('NOR', 'Normal'), ('HY', 'Hydrated'), ('DHY', 'Dehydrated'), ('ACB', 'Breakout'), ('ACR', 'Acne reduced'), ('PC', 'Clogged pores'), ('PR', 'Reduced pores'), ('B', 'Bright'), ('D', 'Dull'), ('RD', 'Redness'), ('WR', 'Wrinkles reduced')], default='0', max_length=4)),
                ('skincare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Skincare')),
            ],
        ),
    ]
