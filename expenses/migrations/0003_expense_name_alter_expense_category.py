# Generated manually

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_expense_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='name',
            field=models.CharField(default='Expense', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Transport', 'Transport'), ('Utilities', 'Utilities'), ('Entertainment', 'Entertainment'), ('Other', 'Other')], max_length=100),
        ),
    ]
