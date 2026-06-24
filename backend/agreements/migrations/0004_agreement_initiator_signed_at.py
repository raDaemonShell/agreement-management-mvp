from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreements', '0003_agreement_section_1_agreement_section_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='initiator_signed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
