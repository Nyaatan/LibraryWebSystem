from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=32, null=True)),
                ('last_name', models.CharField(blank=True, max_length=32, null=True)),
                ('nickname', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'Author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'Book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bookauthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'BookAuthor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('borrowing_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'Borrowing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('card_id', models.IntegerField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=16)),
                ('token', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'Card',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'Category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('isbn', models.BigIntegerField(primary_key=True, serialize=False)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('page_count', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'Edition',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('payments_id', models.IntegerField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'Payments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('publisher_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'Publisher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('subscription_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, unique=True)),
                ('price', models.IntegerField()),
                ('borrowing_count', models.IntegerField()),
            ],
            options={
                'db_table': 'Subscription',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, unique=True)),
                ('email', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(db_column='hash', max_length=64)),
                ('borrowings_remaining', models.IntegerField()),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
    ]
