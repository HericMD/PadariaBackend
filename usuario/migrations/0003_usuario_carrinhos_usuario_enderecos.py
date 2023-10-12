# Generated by Django 4.2.6 on 2023-10-11 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('padaria', '0023_remove_carrinho_usuario'),
        ('usuario', '0002_usuario_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='carrinhos',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='padaria.carrinho'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='enderecos',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='padaria.endereco'),
        ),
    ]