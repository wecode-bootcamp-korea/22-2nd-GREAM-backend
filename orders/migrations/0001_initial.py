# Generated by Django 3.2.5 on 2021-07-25 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_seller', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=18)),
            ],
            options={
                'db_table': 'biddings',
            },
        ),
        migrations.CreateModel(
            name='ExpiredWithin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.IntegerField()),
            ],
            options={
                'db_table': 'expired_within',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'statuses',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('buying_bid', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buying_bid', to='orders.bidding')),
                ('selling_bid', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='selling_bid', to='orders.bidding')),
            ],
            options={
                'db_table': 'contracts',
            },
        ),
        migrations.AddField(
            model_name='bidding',
            name='expired_within',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.expiredwithin'),
        ),
        migrations.AddField(
            model_name='bidding',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
        migrations.AddField(
            model_name='bidding',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.status'),
        ),
        migrations.AddField(
            model_name='bidding',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user'),
        ),
    ]
