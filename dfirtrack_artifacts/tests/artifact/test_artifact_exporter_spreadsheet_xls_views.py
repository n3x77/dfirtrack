import urllib.parse
from datetime import datetime
from unittest.mock import patch

import xlrd
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.utils import timezone

from dfirtrack_artifacts.exporter.spreadsheet.xls import artifact_cron
from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype
from dfirtrack_artifacts.tests.artifact.artifact_exporter_spreadsheet_xls_shared_checks import (
    artifact_exporter_spreadsheet_xls_complete_spreadsheet_check,
)
from dfirtrack_config.models import (
    ArtifactExporterSpreadsheetXlsConfigModel,
    MainConfigModel,
)
from dfirtrack_main.models import (
    Case,
    Casepriority,
    Casestatus,
    System,
    Systemstatus,
    Tag,
    Tagcolor,
)


class ArtifactExporterSpreadsheetXlsViewTestCase(TestCase):
    """artifact exporter spreadsheet XLS view tests"""

    @classmethod
    def setUpTestData(cls):
        # create user
        test_user = User.objects.create_user(
            username='testuser_artifact_exporter_spreadsheet_xls',
            is_staff=True,
            is_superuser=True,
            password='LTzoNHIdxiJydsaJKf1G',
        )
        User.objects.create_user(
            username='message_user', password='gwvXRsMEfYVNIJXK8NZq'
        )

        # create object
        artifactstatus_3 = Artifactstatus.objects.create(
            artifactstatus_name='artifactstatus_3'
        )

        # create object
        artifactstatus_1 = Artifactstatus.objects.create(
            artifactstatus_name='artifactstatus_1',
            artifactstatus_note='lorem ipsum',
        )

        # create objects
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_1')
        artifacttype_2 = Artifacttype.objects.create(
            artifacttype_name='artifacttype_2',
            artifacttype_note='lorem ipsum',
        )

        # create objects
        casepriority_1 = Casepriority.objects.create(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.create(casestatus_name='casestatus_1')

        # create object
        case_1 = Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
            casepriority=casepriority_1,
            casestatus=casestatus_1,
        )

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name='artifact_exporter_spreadsheet_xls_system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        # create object
        tag_1 = Tag.objects.create(tag_name='tag_1', tagcolor=tagcolor_1)
        tag_2 = Tag.objects.create(tag_name='tag_2', tagcolor=tagcolor_1)

        """ create artifacts """

        # mock timezone.now()
        t_1 = datetime(2012, 11, 10, 12, 34, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_1):
            # create object with maximum attributes
            artifact_1 = Artifact.objects.create(
                artifact_name='artifact_exporter_spreadsheet_xls_artifact_1_all_attributes',
                artifactstatus=artifactstatus_3,
                artifacttype=artifacttype_1,
                case=case_1,
                system=system_1,
                artifact_source_path=r'C:\Temp\malicious.exe',
                artifact_note_internal='artifact note for internal usage',
                artifact_note_external='artifact note for external usage',
                artifact_note_analysisresult='artifact note for analysis result',
                artifact_md5='d41d8cd98f00b204e9800998ecf8427e',
                artifact_sha1='da39a3ee5e6b4b0d3255bfef95601890afd80709',
                artifact_sha256='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
                artifact_assigned_to_user_id=test_user,
                artifact_created_by_user_id=test_user,
                artifact_modified_by_user_id=test_user,
            )

        artifact_1.tag.add(tag_1)
        artifact_1.tag.add(tag_2)

        # mock timezone.now()
        t_2 = datetime(2009, 8, 7, 23, 45, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=t_2):
            # create object with minimum attributes
            Artifact.objects.create(
                artifact_name='artifact_exporter_spreadsheet_xls_artifact_2_no_attributes',
                artifactstatus=artifactstatus_3,
                artifacttype=artifacttype_1,
                system=system_1,
                artifact_created_by_user_id=test_user,
                artifact_modified_by_user_id=test_user,
            )

        # create object that will not be exported
        Artifact.objects.create(
            artifact_name='artifact_exporter_spreadsheet_xls_artifact_3_not_exported',
            artifactstatus=artifactstatus_1,
            artifacttype=artifacttype_2,
            system=system_1,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
        )

    def test_artifact_exporter_spreadsheet_xls_not_logged_in(self):
        """test instant spreadsheet export via button for direct download via browser"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/artifacts/artifact/exporter/spreadsheet/xls/artifact/', safe=''
        )
        # get response
        response = self.client.get(
            '/artifacts/artifact/exporter/spreadsheet/xls/artifact/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_artifact_exporter_spreadsheet_xls_logged_in(self):
        """test instant spreadsheet export via button for direct download via browser"""

        # login testuser
        self.client.login(
            username='testuser_artifact_exporter_spreadsheet_xls',
            password='LTzoNHIdxiJydsaJKf1G',
        )
        # get response
        response = self.client.get(
            '/artifacts/artifact/exporter/spreadsheet/xls/artifact/'
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_exporter_spreadsheet_xls_redirect(self):
        """test instant spreadsheet export via button for direct download via browser"""

        # login testuser
        self.client.login(
            username='testuser_artifact_exporter_spreadsheet_xls',
            password='LTzoNHIdxiJydsaJKf1G',
        )
        # create url
        destination = urllib.parse.quote(
            '/artifacts/artifact/exporter/spreadsheet/xls/artifact/', safe='/'
        )
        # get response
        response = self.client.get(
            '/artifacts/artifact/exporter/spreadsheet/xls/artifact', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_artifact_exporter_spreadsheet_xls_minimal_spreadsheet(self):
        """test instant spreadsheet export via button for direct download via browser"""

        """ modify config section """

        # get and modify config to show only mandatory columns
        artifact_exporter_spreadsheet_xls_config_model = ArtifactExporterSpreadsheetXlsConfigModel.objects.get(
            artifact_exporter_spreadsheet_xls_config_name='ArtifactExporterSpreadsheetXlsConfig'
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_id = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_system_id = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_system_name = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifactstatus = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifactpriority = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifacttype = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_source_path = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_storage_path = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_note_internal = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_note_external = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_note_analysisresult = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_md5 = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_sha1 = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_sha256 = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_create_time = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_modify_time = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_worksheet_artifactstatus = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_worksheet_artifacttype = (
            False
        )
        artifact_exporter_spreadsheet_xls_config_model.save()
        # get object
        artifactstatus_3 = Artifactstatus.objects.get(
            artifactstatus_name='artifactstatus_3'
        )
        # add artifactstatus to choice for export
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_choice_artifactstatus.add(
            artifactstatus_3
        )

        """ call view section """

        # login testuser
        self.client.login(
            username='testuser_artifact_exporter_spreadsheet_xls',
            password='LTzoNHIdxiJydsaJKf1G',
        )

        # mock timezone.now()
        t1_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t1_now):
            # get response
            response = self.client.get(
                '/artifacts/artifact/exporter/spreadsheet/xls/artifact/'
            )

        """ get file section """

        # get artifactlist from response content
        workbook = response.content
        # open artifactlist directly from byte stream
        artifactlist = xlrd.open_workbook(file_contents=workbook)

        """ prepare objects section """

        # get objects
        artifact_1 = Artifact.objects.get(
            artifact_name='artifact_exporter_spreadsheet_xls_artifact_1_all_attributes'
        )
        artifact_2 = Artifact.objects.get(
            artifact_name='artifact_exporter_spreadsheet_xls_artifact_2_no_attributes'
        )

        # get sheets
        sheet_artifacts = artifactlist.sheet_by_name('artifacts')

        """ compare values section """

        # compare non-available sheets
        self.assertRaises(
            xlrd.biffh.XLRDError,
            artifactlist.sheet_by_name,
            sheet_name='artifactstatus',
        )
        self.assertRaises(
            xlrd.biffh.XLRDError, artifactlist.sheet_by_name, sheet_name='artifacttype'
        )
        # compare number of rows and columns
        self.assertEqual(sheet_artifacts.nrows, 6)
        self.assertEqual(sheet_artifacts.ncols, 2)
        # compare headlines
        self.assertEqual(sheet_artifacts.row_values(0), ['Artifact', ''])
        # compare content - artifact 1
        self.assertEqual(sheet_artifacts.cell(1, 0).value, artifact_1.artifact_name)
        # compare content - artifact 2
        self.assertEqual(sheet_artifacts.cell(2, 0).value, artifact_2.artifact_name)
        # compare content - metadata
        self.assertEqual(sheet_artifacts.cell(4, 0).value, 'Created:')
        self.assertEqual(
            sheet_artifacts.cell(4, 1).value, t1_now.strftime('%Y-%m-%d %H:%M')
        )
        self.assertEqual(sheet_artifacts.cell(5, 0).value, 'Created by:')
        self.assertEqual(
            sheet_artifacts.cell(5, 1).value,
            'testuser_artifact_exporter_spreadsheet_xls',
        )

    def test_artifact_exporter_spreadsheet_xls_complete_spreadsheet(self):
        """test instant spreadsheet export via button for direct download via browser"""

        """ modify config section """

        # get and modify config to show all columns and sheets
        artifact_exporter_spreadsheet_xls_config_model = ArtifactExporterSpreadsheetXlsConfigModel.objects.get(
            artifact_exporter_spreadsheet_xls_config_name='ArtifactExporterSpreadsheetXlsConfig'
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_id = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_system_id = True
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_system_name = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifactstatus = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifactpriority = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifacttype = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_source_path = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_storage_path = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_note_internal = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_note_external = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_note_analysisresult = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_md5 = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_sha1 = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_sha256 = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_case_id = True
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_case_name = True
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_tag_all = True
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_assigned_to_user_id = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_create_time = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_created_by_user_id = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_modify_time = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_modified_by_user_id = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_worksheet_artifactstatus = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_worksheet_artifacttype = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.save()
        # get object
        artifactstatus_3 = Artifactstatus.objects.get(
            artifactstatus_name='artifactstatus_3'
        )
        # add artifactstatus to choice for export
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_choice_artifactstatus.add(
            artifactstatus_3
        )

        """ call view section """

        # login testuser
        self.client.login(
            username='testuser_artifact_exporter_spreadsheet_xls',
            password='LTzoNHIdxiJydsaJKf1G',
        )

        # mock timezone.now()
        t2_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t2_now):
            # get response
            response = self.client.get(
                '/artifacts/artifact/exporter/spreadsheet/xls/artifact/'
            )

        """ get file section """

        # get artifactlist from response content
        workbook = response.content
        # open artifactlist directly from byte stream
        artifactlist = xlrd.open_workbook(file_contents=workbook)

        """ test section """

        # test for complete spreadsheet content
        artifact_exporter_spreadsheet_xls_complete_spreadsheet_check(
            self, artifactlist, t2_now, 'testuser_artifact_exporter_spreadsheet_xls'
        )

    def test_artifact_exporter_spreadsheet_xls_cron_path_not_existent(self):
        """test spreadsheet export via scheduled task to server file system"""

        # get and modify main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.cron_export_path = '/this_path_does_not_exist'
        main_config_model.cron_username = 'cron'
        main_config_model.save()

        # create spreadsheet without GET by directly calling the function
        artifact_cron()

        # login testuser
        self.client.login(
            username='testuser_artifact_exporter_spreadsheet_xls',
            password='LTzoNHIdxiJydsaJKf1G',
        )
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(
            str(response.context['user']), 'testuser_artifact_exporter_spreadsheet_xls'
        )
        self.assertEqual(
            messages[0].message,
            '[Scheduled task spreadsheet exporter] ARTIFACT_XLS: Export path does not exist. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='gwvXRsMEfYVNIJXK8NZq')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(
            messages[0].message,
            '[Scheduled task spreadsheet exporter] ARTIFACT_XLS: Export path does not exist. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')

    def test_artifact_exporter_spreadsheet_xls_cron_path_no_write_permission(self):
        """test spreadsheet export via scheduled task to server file system"""

        # get and modify main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.cron_export_path = '/root'
        main_config_model.cron_username = 'cron'
        main_config_model.save()

        # create spreadsheet without GET by directly calling the function
        artifact_cron()

        # login testuser
        self.client.login(
            username='testuser_artifact_exporter_spreadsheet_xls',
            password='LTzoNHIdxiJydsaJKf1G',
        )
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(
            str(response.context['user']), 'testuser_artifact_exporter_spreadsheet_xls'
        )
        self.assertEqual(
            messages[0].message,
            '[Scheduled task spreadsheet exporter] ARTIFACT_XLS: No write permission for export path. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='gwvXRsMEfYVNIJXK8NZq')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(
            messages[0].message,
            '[Scheduled task spreadsheet exporter] ARTIFACT_XLS: No write permission for export path. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')

    def test_artifact_exporter_spreadsheet_xls_cron_complete_spreadsheet(self):
        """test spreadsheet export via scheduled task to server file system"""

        """ modify config section """

        # get and modify main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.cron_export_path = '/tmp'
        main_config_model.cron_username = 'cron'
        main_config_model.save()

        # get and modify config to show all columns and sheets
        artifact_exporter_spreadsheet_xls_config_model = ArtifactExporterSpreadsheetXlsConfigModel.objects.get(
            artifact_exporter_spreadsheet_xls_config_name='ArtifactExporterSpreadsheetXlsConfig'
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_id = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_system_id = True
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_system_name = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifactstatus = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifactpriority = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifacttype = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_source_path = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_storage_path = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_note_internal = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_note_external = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_note_analysisresult = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_md5 = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_sha1 = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_sha256 = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_case_id = True
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_case_name = True
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_tag_all = True
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_assigned_to_user_id = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_create_time = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_created_by_user_id = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_modify_time = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_artifact_modified_by_user_id = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_worksheet_artifactstatus = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_worksheet_artifacttype = (
            True
        )
        artifact_exporter_spreadsheet_xls_config_model.save()
        # get object
        artifactstatus_3 = Artifactstatus.objects.get(
            artifactstatus_name='artifactstatus_3'
        )
        # add artifactstatus to choice for export
        artifact_exporter_spreadsheet_xls_config_model.artifactlist_xls_choice_artifactstatus.add(
            artifactstatus_3
        )

        """ call view section """

        # login testuser
        self.client.login(
            username='testuser_artifact_exporter_spreadsheet_xls',
            password='LTzoNHIdxiJydsaJKf1G',
        )

        # mock timezone.now()
        t3_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t3_now):
            # create spreadsheet without GET by directly calling the function
            artifact_cron()

        """ get file section """

        # refresh config
        main_config_model.refresh_from_db()
        # get time for output file
        filetime = t3_now.strftime('%Y%m%d_%H%M')
        # prepare output file path
        output_file_path = (
            main_config_model.cron_export_path + '/' + filetime + '_artifacts.xls'
        )
        # open file from temp folder
        xls_disk = xlrd.open_workbook(output_file_path)

        """ test section """

        # test for complete spreadsheet content
        artifact_exporter_spreadsheet_xls_complete_spreadsheet_check(
            self, xls_disk, t3_now, 'cron'
        )

    def test_artifact_exporter_spreadsheet_xls_create_cron_not_logged_in(self):
        """test helper function to check config before creating scheduled task"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/artifacts/artifact/exporter/spreadsheet/xls/artifact/cron/', safe=''
        )
        # get response
        response = self.client.get(
            '/artifacts/artifact/exporter/spreadsheet/xls/artifact/cron/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_artifact_exporter_spreadsheet_xls_create_cron_logged_in(self):
        """test helper function to check config before creating scheduled task"""

        # login testuser
        self.client.login(
            username='testuser_artifact_exporter_spreadsheet_xls',
            password='LTzoNHIdxiJydsaJKf1G',
        )
        # create url
        destination = urllib.parse.quote(
            '/admin/django_q/schedule/add/?name=artifact_spreadsheet_exporter_xls&func=dfirtrack_artifacts.exporter.spreadsheet.xls.artifact_cron',
            safe='/?=&',
        )
        # get response
        response = self.client.get(
            '/artifacts/artifact/exporter/spreadsheet/xls/artifact/cron/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_artifact_exporter_spreadsheet_xls_create_cron_redirect(self):
        """test helper function to check config before creating scheduled task"""

        # login testuser
        self.client.login(
            username='testuser_artifact_exporter_spreadsheet_xls',
            password='LTzoNHIdxiJydsaJKf1G',
        )
        # create url
        destination = urllib.parse.quote(
            '/admin/django_q/schedule/add/?name=artifact_spreadsheet_exporter_xls&func=dfirtrack_artifacts.exporter.spreadsheet.xls.artifact_cron',
            safe='/?=&',
        )
        # get response
        response = self.client.get(
            '/artifacts/artifact/exporter/spreadsheet/xls/artifact/cron', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_artifact_exporter_spreadsheet_xls_create_cron_path_not_existent(self):
        """test helper function to check config before creating scheduled task"""

        # get and modify main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.cron_export_path = '/this_path_does_not_exist'
        main_config_model.cron_username = 'cron'
        main_config_model.save()

        # login testuser
        self.client.login(
            username='testuser_artifact_exporter_spreadsheet_xls',
            password='LTzoNHIdxiJydsaJKf1G',
        )

        # create url
        destination = urllib.parse.quote('/artifacts/artifact/', safe='/')
        # get response
        response = self.client.get(
            '/artifacts/artifact/exporter/spreadsheet/xls/artifact/cron/'
        )
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )
        self.assertEqual(
            messages[0].message,
            'Export path does not exist. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')

    def test_artifact_exporter_spreadsheet_xls_create_cron_path_no_write_permission(
        self,
    ):
        """test helper function to check config before creating scheduled task"""

        # get and modify main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        main_config_model.cron_export_path = '/root'
        main_config_model.cron_username = 'cron'
        main_config_model.save()

        # login testuser
        self.client.login(
            username='testuser_artifact_exporter_spreadsheet_xls',
            password='LTzoNHIdxiJydsaJKf1G',
        )

        # create url
        destination = urllib.parse.quote('/artifacts/artifact/', safe='/')
        # get response
        response = self.client.get(
            '/artifacts/artifact/exporter/spreadsheet/xls/artifact/cron/'
        )
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )
        self.assertEqual(
            messages[0].message,
            'No write permission for export path. Check config or file system!',
        )
        self.assertEqual(messages[0].level_tag, 'error')
