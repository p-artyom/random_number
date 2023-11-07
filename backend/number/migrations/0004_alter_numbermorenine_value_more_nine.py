import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("number", "0003_numbermorenine_value_more_nine"),
    ]

    operations = [
        migrations.AlterField(
            model_name="numbermorenine",
            name="value_more_nine",
            field=models.FloatField(
                validators=[
                    django.core.validators.MaxValueValidator(10),
                    django.core.validators.MinValueValidator(9),
                ],
                verbose_name="число больше 9",
            ),
        ),
    ]
