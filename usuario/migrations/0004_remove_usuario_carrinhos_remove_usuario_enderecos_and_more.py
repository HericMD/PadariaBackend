# Generated by Django 4.2.6 on 2023-10-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padaria', '0025_remove_carrinho_produto_carrinho_produto'),
        ('usuario', '0003_usuario_carrinhos_usuario_enderecos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='carrinhos',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='enderecos',
        ),
        migrations.AddField(
            model_name='usuario',
            name='carrinhos',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='padaria.carrinho'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='enderecos',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='padaria.endereco'),
        ),
    ]
