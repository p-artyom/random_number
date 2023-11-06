from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("number", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NumberMoreNine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
            ],
            options={
                "verbose_name": "число больше 9",
                "verbose_name_plural": "числа больше 9",
            },
        ),
    ]
