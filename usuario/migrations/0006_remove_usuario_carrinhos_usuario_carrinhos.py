# Generated by Django 4.2.6 on 2023-11-06 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('padaria', '0034_alter_carrinho_endereco'),
        ('usuario', '0005_alter_usuario_carrinhos_alter_usuario_enderecos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='carrinhos',
        ),
        migrations.AddField(
            model_name='usuario',
            name='carrinhos',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='padaria.carrinho'),
        ),
    ]
