# Generated by Django 4.2.10 on 2024-02-15 17:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galaxy", "0048_update_collection_remote_rhcertified_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        default=None,
                        editable=False,
                        help_text="The date/time this resource was created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        default=None,
                        editable=False,
                        help_text="The date/time this resource was created",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The name of this resource", max_length=512, unique=True
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default="", help_text="The organization description."
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=None,
                        editable=False,
                        help_text="The user who created this resource",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="%(app_label)s_%(class)s_created+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        default=None,
                        editable=False,
                        help_text="The user who last modified this resource",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="%(app_label)s_%(class)s_modified+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        help_text="The list of users in this organization.",
                        related_name="organizations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        default=None,
                        editable=False,
                        help_text="The date/time this resource was created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        default=None,
                        editable=False,
                        help_text="The date/time this resource was created",
                    ),
                ),
                ("name", models.CharField(help_text="The name of this resource", max_length=512)),
                (
                    "description",
                    models.TextField(blank=True, default="", help_text="The team description."),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=None,
                        editable=False,
                        help_text="The user who created this resource",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="%(app_label)s_%(class)s_created+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        default=None,
                        editable=False,
                        help_text="The user who last modified this resource",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="%(app_label)s_%(class)s_modified+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        help_text="The organization of this team.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teams",
                        to="galaxy.organization",
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        help_text="The list of users in this team.",
                        related_name="teams",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "group",
                    models.OneToOneField(
                        help_text="Related group record.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="galaxy.group",
                    ),

                )
            ],
            options={
                "ordering": ("organization__name", "name"),
                "abstract": False,
                "unique_together": {("organization", "name")},
            },
        ),
    ]