# Generated by Django 4.2.6 on 2023-10-11 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('padaria', '0020_alter_categoria_imagem_alter_usuario_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='uploader.image'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='uploader.image'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='uploader.image'),
        ),
    ]
