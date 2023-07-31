# Generated by Django 4.2.2 on 2023-07-31 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.FloatField(max_length=6)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('rua', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.FloatField(max_length=8)),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.FloatField(blank=True, max_length=11, null=True)),
                ('senha', models.CharField(max_length=50)),
                ('endereco_padrao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuarios', to='padaria.endereco')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
    ]
