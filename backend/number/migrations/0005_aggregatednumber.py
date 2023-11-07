import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("number", "0004_alter_numbermorenine_value_more_nine"),
    ]

    operations = [
        migrations.CreateModel(
            name="AggregatedNumber",
            fields=[
                (
                    "time_minute",
                    models.DateTimeField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="дата создания",
                    ),
                ),
                (
                    "avg_value",
                    models.FloatField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(0),
                        ],
                        verbose_name="агрегированное число",
                    ),
                ),
            ],
            options={
                "verbose_name": "агрегированное число",
                "verbose_name_plural": "агрегированные числа",
                "db_table": "minute_by_minute_aggregated_data",
                "managed": False,
            },
        ),
    ]
