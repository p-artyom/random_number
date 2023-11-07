import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("number", "0002_numbermorenine"),
    ]

    operations = [
        migrations.AddField(
            model_name="numbermorenine",
            name="value_more_nine",
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(10),
                    django.core.validators.MinValueValidator(9),
                ],
                verbose_name="число больше 9",
            ),
        ),
    ]
