# Generated by Django 4.2.6 on 2023-10-11 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('padaria', '0021_alter_categoria_imagem_alter_produto_imagem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]