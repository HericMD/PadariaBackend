# Generated by Django 4.2.2 on 2023-08-14 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('padaria', '0004_alter_carrinho_bairro_alter_carrinho_cep_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
    ]
