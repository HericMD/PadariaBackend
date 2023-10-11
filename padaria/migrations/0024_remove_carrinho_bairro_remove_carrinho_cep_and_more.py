# Generated by Django 4.2.6 on 2023-10-11 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('padaria', '0023_remove_carrinho_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='carrinho',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='carrinho',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='carrinho',
            name='complemento',
        ),
        migrations.RemoveField(
            model_name='carrinho',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='carrinho',
            name='rua',
        ),
        migrations.AddField(
            model_name='carrinho',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='produto', to='padaria.endereco'),
            preserve_default=False,
        ),
    ]
