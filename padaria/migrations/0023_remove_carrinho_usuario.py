# Generated by Django 4.2.6 on 2023-10-11 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('padaria', '0022_alter_carrinho_usuario_delete_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='usuario',
        ),
    ]
