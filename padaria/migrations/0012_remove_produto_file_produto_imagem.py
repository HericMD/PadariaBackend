# Generated by Django 4.2.2 on 2023-08-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("padaria", "0011_remove_produto_uploaded_on_alter_produto_file"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="produto",
            name="file",
        ),
        migrations.AddField(
            model_name="produto",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
