# Generated by Django 5.0.6 on 2024-05-26 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_payments_pay_link_payments_session_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='sum_pay',
            new_name='amount',
        ),
    ]