# Generated by Django 3.2.14 on 2022-07-15 19:46

from django.db import migrations, models
import django.db.models.deletion


def populate_synclist_distros(apps, schema_editor):
    """
    Populate the foreign key to AnsibleDistribution based on SyncList name
    """
    AnsibleDistribution = apps.get_model('ansible', 'AnsibleDistribution')
    SyncList = apps.get_model('galaxy', 'SyncList')
    db_alias = schema_editor.connection.alias

    for synclist in SyncList.objects.using(db_alias).all():
        distro_qs = AnsibleDistribution.objects.using(db_alias).filter(name=synclist.name)
        if len(distro_qs) == 0:
            print(f"Found SyncList with no matching AnsibleDistribution: {synclist.name}")
            continue
        if len(distro_qs) > 1:
            print(f"Found SyncList with multilpe matching AnsibleDistribution: {synclist.name}")
            continue
        synclist.distribution = distro_qs[0]
        synclist.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ansible', '0041_alter_collectionversion_collection'),
        ('galaxy', '0028_move_perms_to_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='synclist',
            name='distribution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='distributions', to='ansible.ansibledistribution'),
        ),
        migrations.AlterField(
            model_name='synclist',
            name='repository',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='repositories', to='ansible.ansiblerepository'),
        ),
        migrations.AlterField(
            model_name='synclist',
            name='upstream_repository',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='upstream_repositories', to='ansible.ansiblerepository'),
        ),
        migrations.RunPython(
            code=populate_synclist_distros,
            reverse_code=migrations.RunPython.noop
        ),
    ]