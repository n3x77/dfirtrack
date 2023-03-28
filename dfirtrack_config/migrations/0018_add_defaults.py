# Generated by Django 3.2.3 on 2021-05-28 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dfirtrack_main', '0017_simplify_system_times'),
        ('dfirtrack_config', '0017_main_overview_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_create_time',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_id',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_md5',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_modify_time',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_note_analysisresult',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_note_external',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_note_internal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_sha1',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_sha256',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_source_path',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifact_storage_path',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifactpriority',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifactstatus',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_artifacttype',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_system_id',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_system_name',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_worksheet_artifactstatus',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='artifactexporterspreadsheetxlsconfigmodel',
            name='artifactlist_xls_worksheet_artifacttype',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='mainconfigmodel',
            name='system_name_editable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_analysisstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_case',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_company',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_dnsname',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_domain',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_ip',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_location',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_os',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_reason',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_recommendation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_serviceprovider',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_system_create_time',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_system_id',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_system_modify_time',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_systemstatus',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_systemtype',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetcsvconfigmodel',
            name='spread_csv_tag',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_analysisstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_case',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_company',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_dnsname',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_domain',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_ip',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_location',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_os',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_reason',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_recommendation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_serviceprovider',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_system_create_time',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_system_id',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_system_modify_time',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_systemstatus',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_systemtype',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_tag',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_worksheet_analysisstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_worksheet_reason',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_worksheet_recommendation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_worksheet_systemstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemexporterspreadsheetxlsconfigmodel',
            name='spread_xls_worksheet_tag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_case',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_company',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_dnsname',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_domain',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_location',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_os',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_reason',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_recommendation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_serviceprovider',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_systemtype',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_tag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_tagfree_analysisstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_choice_tagfree_systemstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_column_system',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_default_analysisstatus',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='system_importer_file_csv_config_analysisstatus',
                to='dfirtrack_main.analysisstatus',
            ),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_default_systemstatus',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='system_importer_file_csv_config_systemstatus',
                to='dfirtrack_main.systemstatus',
            ),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_default_tagfree_analysisstatus',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='system_importer_file_csv_config_tagfree_analysisstatus',
                to='dfirtrack_main.analysisstatus',
            ),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_default_tagfree_systemstatus',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='system_importer_file_csv_config_tagfree_systemstatus',
                to='dfirtrack_main.systemstatus',
            ),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_headline',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_remove_analysisstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_remove_case',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_remove_company',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_remove_dnsname',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_remove_domain',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_remove_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_remove_location',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_remove_os',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_remove_reason',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_remove_recommendation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_remove_serviceprovider',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_remove_systemstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_remove_systemtype',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='systemimporterfilecsvconfigmodel',
            name='csv_skip_existing_system',
            field=models.BooleanField(default=False),
        ),
    ]
