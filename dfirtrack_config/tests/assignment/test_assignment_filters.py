from django.test import TestCase
from django.contrib.auth.models import User

from dfirtrack_artifacts.models import (
    Artifact,
    Artifactstatus,
    Artifacttype,
)
from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.models import (
    Case,
    Casepriority,
    Casestatus,
    Headline,
    Note,
    Notestatus,
    Reportitem,
    System,
    Systemstatus,
    Tag,
    Tagcolor,
    Task,
    Taskname,
    Taskpriority,
    Taskstatus,
)


def set_user_config(
    test_user,
    filter_assignment_view_case,
    filter_assignment_view_tag,
    filter_assignment_view_user,
    filter_assignment_view_keep=True,
):
    """set user config"""

    # get config
    user_config = UserConfigModel.objects.get(user_config_username=test_user)
    # set values
    user_config.filter_assignment_view_case = filter_assignment_view_case
    user_config.filter_assignment_view_tag = filter_assignment_view_tag
    user_config.filter_assignment_view_user = filter_assignment_view_user
    user_config.filter_assignment_view_keep = filter_assignment_view_keep
    # save config
    user_config.save()

    # return to test
    return


class AssignmentViewTestCase(TestCase):
    """assignment view tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username='testuser_assignment_filter', password='B1z2nn60R4XUMmRoqcA7'
        )

        # create config
        UserConfigModel.objects.create(user_config_username=test_user)

        # create objects
        artifactstatus_1 = Artifactstatus.objects.create(
            artifactstatus_name='artifactstatus_1'
        )
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_1')
        casepriority_1 = Casepriority.objects.create(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.create(casestatus_name='casestatus_1')
        headline_1 = Headline.objects.create(headline_name='headline_1')
        notestatus_1 = Notestatus.objects.create(notestatus_name='notestatus_1')
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        taskname_1 = Taskname.objects.create(taskname_name='taskname_1')
        taskpriority_1 = Taskpriority.objects.create(taskpriority_name='prio_1')
        taskstatus_1 = Taskstatus.objects.create(taskstatus_name='taskstatus_1')

        # create objects
        tag_1 = Tag.objects.create(
            tag_name='tag_1',
            tagcolor=tagcolor_1,
        )
        Tag.objects.create(
            tag_name='tag_2',
            tagcolor=tagcolor_1,
        )
        Tag.objects.create(
            tag_name='tag_3',
            tagcolor=tagcolor_1,
        )
        Tag.objects.create(
            tag_name='tag_4',
            tagcolor=tagcolor_1,
            tag_assigned_to_user_id=test_user,
        )

        # create objects
        case_1 = Case.objects.create(
            case_name='case_1',
            casepriority=casepriority_1,
            casestatus=casestatus_1,
            case_is_incident=True,
            case_created_by_user_id=test_user,
            case_modified_by_user_id=test_user,
        )
        Case.objects.create(
            case_name='case_2',
            casepriority=casepriority_1,
            casestatus=casestatus_1,
            case_is_incident=True,
            case_created_by_user_id=test_user,
            case_modified_by_user_id=test_user,
        )
        case_3 = Case.objects.create(
            case_name='case_3',
            casepriority=casepriority_1,
            casestatus=casestatus_1,
            case_is_incident=True,
            case_created_by_user_id=test_user,
            case_modified_by_user_id=test_user,
        )
        case_3.tag.add(tag_1)
        Case.objects.create(
            case_name='case_4',
            casepriority=casepriority_1,
            casestatus=casestatus_1,
            case_is_incident=True,
            case_created_by_user_id=test_user,
            case_modified_by_user_id=test_user,
            case_assigned_to_user_id=test_user,
        )

        # create objects
        Note.objects.create(
            note_title='note_1',
            note_content='note_1',
            notestatus=notestatus_1,
            note_created_by_user_id=test_user,
            note_modified_by_user_id=test_user,
        )
        Note.objects.create(
            note_title='note_2',
            note_content='note_2',
            notestatus=notestatus_1,
            note_created_by_user_id=test_user,
            note_modified_by_user_id=test_user,
            case=case_1,
        )
        note_3 = Note.objects.create(
            note_title='note_3',
            note_content='note_3',
            notestatus=notestatus_1,
            note_created_by_user_id=test_user,
            note_modified_by_user_id=test_user,
        )
        note_3.tag.add(tag_1)
        Note.objects.create(
            note_title='note_4',
            note_content='note_4',
            notestatus=notestatus_1,
            note_created_by_user_id=test_user,
            note_modified_by_user_id=test_user,
            note_assigned_to_user_id=test_user,
        )

        # create objects
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        system_2 = System.objects.create(
            system_name='system_2',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        system_2.case.add(case_1)
        system_3 = System.objects.create(
            system_name='system_3',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        system_3.tag.add(tag_1)
        System.objects.create(
            system_name='system_4',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
            system_assigned_to_user_id=test_user,
        )

        # create objects
        Task.objects.create(
            taskname=taskname_1,
            task_note='task_1',
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )
        Task.objects.create(
            taskname=taskname_1,
            task_note='task_2',
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
            case=case_1,
        )
        task_3 = Task.objects.create(
            taskname=taskname_1,
            task_note='task_3',
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )
        task_3.tag.add(tag_1)
        Task.objects.create(
            taskname=taskname_1,
            task_note='task_4',
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
            task_assigned_to_user_id=test_user,
        )

        # create objects
        Artifact.objects.create(
            artifact_name='artifact_1',
            artifactstatus=artifactstatus_1,
            artifacttype=artifacttype_1,
            system=system_1,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
        )
        Artifact.objects.create(
            artifact_name='artifact_2',
            artifactstatus=artifactstatus_1,
            artifacttype=artifacttype_1,
            system=system_1,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
            case=case_1,
        )
        artifact_3 = Artifact.objects.create(
            artifact_name='artifact_3',
            artifactstatus=artifactstatus_1,
            artifacttype=artifacttype_1,
            system=system_1,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
        )
        artifact_3.tag.add(tag_1)
        Artifact.objects.create(
            artifact_name='artifact_4',
            artifactstatus=artifactstatus_1,
            artifacttype=artifacttype_1,
            system=system_1,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
            artifact_assigned_to_user_id=test_user,
        )

        # create objects
        Reportitem.objects.create(
            reportitem_note='reportitem_1',
            headline=headline_1,
            notestatus=notestatus_1,
            system=system_1,
            reportitem_created_by_user_id=test_user,
            reportitem_modified_by_user_id=test_user,
        )
        Reportitem.objects.create(
            reportitem_note='reportitem_2',
            headline=headline_1,
            notestatus=notestatus_1,
            system=system_1,
            reportitem_created_by_user_id=test_user,
            reportitem_modified_by_user_id=test_user,
            case=case_1,
        )
        reportitem_3 = Reportitem.objects.create(
            reportitem_note='reportitem_3',
            headline=headline_1,
            notestatus=notestatus_1,
            system=system_1,
            reportitem_created_by_user_id=test_user,
            reportitem_modified_by_user_id=test_user,
        )
        reportitem_3.tag.add(tag_1)
        Reportitem.objects.create(
            reportitem_note='reportitem_4',
            headline=headline_1,
            notestatus=notestatus_1,
            system=system_1,
            reportitem_created_by_user_id=test_user,
            reportitem_modified_by_user_id=test_user,
            reportitem_assigned_to_user_id=test_user,
        )

    def test_assignment_view_no_filter_context(self):
        """no filter applied"""

        # login testuser
        self.client.login(
            username='testuser_assignment_filter', password='B1z2nn60R4XUMmRoqcA7'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_filter')
        # get objects
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        artifact_2 = Artifact.objects.get(artifact_name='artifact_2')
        artifact_3 = Artifact.objects.get(artifact_name='artifact_3')
        artifact_4 = Artifact.objects.get(artifact_name='artifact_4')
        case_1 = Case.objects.get(case_name='case_1')
        case_2 = Case.objects.get(case_name='case_2')
        case_3 = Case.objects.get(case_name='case_3')
        case_4 = Case.objects.get(case_name='case_4')
        note_1 = Note.objects.get(note_title='note_1')
        note_2 = Note.objects.get(note_title='note_2')
        note_3 = Note.objects.get(note_title='note_3')
        note_4 = Note.objects.get(note_title='note_4')
        reportitem_1 = Reportitem.objects.get(reportitem_note='reportitem_1')
        reportitem_2 = Reportitem.objects.get(reportitem_note='reportitem_2')
        reportitem_3 = Reportitem.objects.get(reportitem_note='reportitem_3')
        reportitem_4 = Reportitem.objects.get(reportitem_note='reportitem_4')
        system_1 = System.objects.get(system_name='system_1')
        system_2 = System.objects.get(system_name='system_2')
        system_3 = System.objects.get(system_name='system_3')
        system_4 = System.objects.get(system_name='system_4')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        tag_2 = Tag.objects.get(tag_name='tag_2')
        tag_3 = Tag.objects.get(tag_name='tag_3')
        tag_4 = Tag.objects.get(tag_name='tag_4')
        task_1 = Task.objects.get(task_note='task_1')
        task_2 = Task.objects.get(task_note='task_2')
        task_3 = Task.objects.get(task_note='task_3')
        task_4 = Task.objects.get(task_note='task_4')

        # change config
        set_user_config(test_user, None, None, None)

        # get response
        response = self.client.get('/config/assignment/')
        # compare
        self.assertTrue(
            response.context['artifact']
            .filter(artifact_name=artifact_1.artifact_name)
            .exists()
        )
        self.assertTrue(
            response.context['artifact']
            .filter(artifact_name=artifact_2.artifact_name)
            .exists()
        )
        self.assertTrue(
            response.context['artifact']
            .filter(artifact_name=artifact_3.artifact_name)
            .exists()
        )
        self.assertTrue(
            response.context['case'].filter(case_name=case_1.case_name).exists()
        )
        self.assertTrue(
            response.context['case'].filter(case_name=case_2.case_name).exists()
        )
        self.assertTrue(
            response.context['case'].filter(case_name=case_3.case_name).exists()
        )
        self.assertTrue(
            response.context['note'].filter(note_title=note_1.note_title).exists()
        )
        self.assertTrue(
            response.context['note'].filter(note_title=note_2.note_title).exists()
        )
        self.assertTrue(
            response.context['note'].filter(note_title=note_3.note_title).exists()
        )
        self.assertTrue(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_1.reportitem_note)
            .exists()
        )
        self.assertTrue(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_2.reportitem_note)
            .exists()
        )
        self.assertTrue(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_3.reportitem_note)
            .exists()
        )
        self.assertTrue(
            response.context['system'].filter(system_name=system_1.system_name).exists()
        )
        self.assertTrue(
            response.context['system'].filter(system_name=system_2.system_name).exists()
        )
        self.assertTrue(
            response.context['system'].filter(system_name=system_3.system_name).exists()
        )
        self.assertTrue(
            response.context['tag'].filter(tag_name=tag_1.tag_name).exists()
        )
        self.assertTrue(
            response.context['tag'].filter(tag_name=tag_2.tag_name).exists()
        )
        self.assertTrue(
            response.context['tag'].filter(tag_name=tag_3.tag_name).exists()
        )
        self.assertTrue(
            response.context['task'].filter(task_note=task_1.task_note).exists()
        )
        self.assertTrue(
            response.context['task'].filter(task_note=task_2.task_note).exists()
        )
        self.assertTrue(
            response.context['task'].filter(task_note=task_3.task_note).exists()
        )
        self.assertFalse(
            response.context['artifact']
            .filter(artifact_name=artifact_4.artifact_name)
            .exists()
        )
        self.assertFalse(
            response.context['case'].filter(case_name=case_4.case_name).exists()
        )
        self.assertFalse(
            response.context['note'].filter(note_title=note_4.note_title).exists()
        )
        self.assertFalse(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_4.reportitem_note)
            .exists()
        )
        self.assertFalse(
            response.context['system'].filter(system_name=system_4.system_name).exists()
        )
        self.assertFalse(
            response.context['tag'].filter(tag_name=tag_4.tag_name).exists()
        )
        self.assertFalse(
            response.context['task'].filter(task_note=task_4.task_note).exists()
        )

    def test_assignment_view_case_filter_context(self):
        """case filter applied"""

        # login testuser
        self.client.login(
            username='testuser_assignment_filter', password='B1z2nn60R4XUMmRoqcA7'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_filter')
        # get objects
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        artifact_2 = Artifact.objects.get(artifact_name='artifact_2')
        artifact_3 = Artifact.objects.get(artifact_name='artifact_3')
        artifact_4 = Artifact.objects.get(artifact_name='artifact_4')
        case_1 = Case.objects.get(case_name='case_1')
        case_2 = Case.objects.get(case_name='case_2')
        case_3 = Case.objects.get(case_name='case_3')
        case_4 = Case.objects.get(case_name='case_4')
        note_1 = Note.objects.get(note_title='note_1')
        note_2 = Note.objects.get(note_title='note_2')
        note_3 = Note.objects.get(note_title='note_3')
        note_4 = Note.objects.get(note_title='note_4')
        reportitem_1 = Reportitem.objects.get(reportitem_note='reportitem_1')
        reportitem_2 = Reportitem.objects.get(reportitem_note='reportitem_2')
        reportitem_3 = Reportitem.objects.get(reportitem_note='reportitem_3')
        reportitem_4 = Reportitem.objects.get(reportitem_note='reportitem_4')
        system_1 = System.objects.get(system_name='system_1')
        system_2 = System.objects.get(system_name='system_2')
        system_3 = System.objects.get(system_name='system_3')
        system_4 = System.objects.get(system_name='system_4')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        tag_2 = Tag.objects.get(tag_name='tag_2')
        tag_3 = Tag.objects.get(tag_name='tag_3')
        tag_4 = Tag.objects.get(tag_name='tag_4')
        task_1 = Task.objects.get(task_note='task_1')
        task_2 = Task.objects.get(task_note='task_2')
        task_3 = Task.objects.get(task_note='task_3')
        task_4 = Task.objects.get(task_note='task_4')

        # change config
        set_user_config(test_user, case_1, None, None)

        # get response
        response = self.client.get('/config/assignment/')
        # compare
        self.assertTrue(
            response.context['artifact']
            .filter(artifact_name=artifact_2.artifact_name)
            .exists()
        )
        self.assertTrue(
            response.context['note'].filter(note_title=note_2.note_title).exists()
        )
        self.assertTrue(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_2.reportitem_note)
            .exists()
        )
        self.assertTrue(
            response.context['system'].filter(system_name=system_2.system_name).exists()
        )
        self.assertTrue(
            response.context['task'].filter(task_note=task_2.task_note).exists()
        )
        self.assertFalse(
            response.context['artifact']
            .filter(artifact_name=artifact_1.artifact_name)
            .exists()
        )
        self.assertFalse(
            response.context['artifact']
            .filter(artifact_name=artifact_3.artifact_name)
            .exists()
        )
        self.assertFalse(
            response.context['artifact']
            .filter(artifact_name=artifact_4.artifact_name)
            .exists()
        )
        self.assertFalse(
            response.context['case'].filter(case_name=case_3.case_name).exists()
        )
        self.assertFalse(
            response.context['case'].filter(case_name=case_4.case_name).exists()
        )
        self.assertFalse(
            response.context['note'].filter(note_title=note_1.note_title).exists()
        )
        self.assertFalse(
            response.context['note'].filter(note_title=note_3.note_title).exists()
        )
        self.assertFalse(
            response.context['note'].filter(note_title=note_4.note_title).exists()
        )
        self.assertFalse(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_1.reportitem_note)
            .exists()
        )
        self.assertFalse(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_3.reportitem_note)
            .exists()
        )
        self.assertFalse(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_4.reportitem_note)
            .exists()
        )
        self.assertFalse(
            response.context['system'].filter(system_name=system_3.system_name).exists()
        )
        self.assertFalse(
            response.context['system'].filter(system_name=system_4.system_name).exists()
        )
        self.assertFalse(
            response.context['tag'].filter(tag_name=tag_1.tag_name).exists()
        )
        self.assertFalse(
            response.context['tag'].filter(tag_name=tag_3.tag_name).exists()
        )
        self.assertFalse(
            response.context['tag'].filter(tag_name=tag_4.tag_name).exists()
        )
        self.assertFalse(
            response.context['task'].filter(task_note=task_1.task_note).exists()
        )
        self.assertFalse(
            response.context['task'].filter(task_note=task_3.task_note).exists()
        )
        self.assertFalse(
            response.context['task'].filter(task_note=task_4.task_note).exists()
        )
        # special case 'case' - filtering for case 1 returns only case 1 itself
        self.assertTrue(
            response.context['case'].filter(case_name=case_1.case_name).exists()
        )
        self.assertFalse(
            response.context['case'].filter(case_name=case_2.case_name).exists()
        )
        # special case 'system' - system is added to case 1 because of signal for artifact 2 and reportitem 2
        self.assertTrue(
            response.context['system'].filter(system_name=system_1.system_name).exists()
        )
        # special case 'tag' - tag has no case relation so no cases are returned
        self.assertFalse(
            response.context['tag'].filter(tag_name=tag_2.tag_name).exists()
        )

    def test_assignment_view_tag_filter_context(self):
        """tag filter applied"""

        # login testuser
        self.client.login(
            username='testuser_assignment_filter', password='B1z2nn60R4XUMmRoqcA7'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_filter')
        # get objects
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        artifact_2 = Artifact.objects.get(artifact_name='artifact_2')
        artifact_3 = Artifact.objects.get(artifact_name='artifact_3')
        artifact_4 = Artifact.objects.get(artifact_name='artifact_4')
        case_1 = Case.objects.get(case_name='case_1')
        case_2 = Case.objects.get(case_name='case_2')
        case_3 = Case.objects.get(case_name='case_3')
        case_4 = Case.objects.get(case_name='case_4')
        note_1 = Note.objects.get(note_title='note_1')
        note_2 = Note.objects.get(note_title='note_2')
        note_3 = Note.objects.get(note_title='note_3')
        note_4 = Note.objects.get(note_title='note_4')
        reportitem_1 = Reportitem.objects.get(reportitem_note='reportitem_1')
        reportitem_2 = Reportitem.objects.get(reportitem_note='reportitem_2')
        reportitem_3 = Reportitem.objects.get(reportitem_note='reportitem_3')
        reportitem_4 = Reportitem.objects.get(reportitem_note='reportitem_4')
        system_1 = System.objects.get(system_name='system_1')
        system_2 = System.objects.get(system_name='system_2')
        system_3 = System.objects.get(system_name='system_3')
        system_4 = System.objects.get(system_name='system_4')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        tag_2 = Tag.objects.get(tag_name='tag_2')
        tag_3 = Tag.objects.get(tag_name='tag_3')
        tag_4 = Tag.objects.get(tag_name='tag_4')
        task_1 = Task.objects.get(task_note='task_1')
        task_2 = Task.objects.get(task_note='task_2')
        task_3 = Task.objects.get(task_note='task_3')
        task_4 = Task.objects.get(task_note='task_4')

        # change config
        set_user_config(test_user, None, tag_1, None)

        # get response
        response = self.client.get('/config/assignment/')
        # compare
        self.assertTrue(
            response.context['artifact']
            .filter(artifact_name=artifact_3.artifact_name)
            .exists()
        )
        self.assertTrue(
            response.context['case'].filter(case_name=case_3.case_name).exists()
        )
        self.assertTrue(
            response.context['note'].filter(note_title=note_3.note_title).exists()
        )
        self.assertTrue(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_3.reportitem_note)
            .exists()
        )
        self.assertTrue(
            response.context['system'].filter(system_name=system_3.system_name).exists()
        )
        self.assertTrue(
            response.context['task'].filter(task_note=task_3.task_note).exists()
        )
        self.assertFalse(
            response.context['artifact']
            .filter(artifact_name=artifact_1.artifact_name)
            .exists()
        )
        self.assertFalse(
            response.context['artifact']
            .filter(artifact_name=artifact_2.artifact_name)
            .exists()
        )
        self.assertFalse(
            response.context['artifact']
            .filter(artifact_name=artifact_4.artifact_name)
            .exists()
        )
        self.assertFalse(
            response.context['case'].filter(case_name=case_1.case_name).exists()
        )
        self.assertFalse(
            response.context['case'].filter(case_name=case_2.case_name).exists()
        )
        self.assertFalse(
            response.context['case'].filter(case_name=case_4.case_name).exists()
        )
        self.assertFalse(
            response.context['note'].filter(note_title=note_1.note_title).exists()
        )
        self.assertFalse(
            response.context['note'].filter(note_title=note_2.note_title).exists()
        )
        self.assertFalse(
            response.context['note'].filter(note_title=note_4.note_title).exists()
        )
        self.assertFalse(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_1.reportitem_note)
            .exists()
        )
        self.assertFalse(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_2.reportitem_note)
            .exists()
        )
        self.assertFalse(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_4.reportitem_note)
            .exists()
        )
        self.assertFalse(
            response.context['system'].filter(system_name=system_1.system_name).exists()
        )
        self.assertFalse(
            response.context['system'].filter(system_name=system_2.system_name).exists()
        )
        self.assertFalse(
            response.context['system'].filter(system_name=system_4.system_name).exists()
        )
        self.assertFalse(
            response.context['tag'].filter(tag_name=tag_2.tag_name).exists()
        )
        self.assertFalse(
            response.context['tag'].filter(tag_name=tag_4.tag_name).exists()
        )
        self.assertFalse(
            response.context['task'].filter(task_note=task_1.task_note).exists()
        )
        self.assertFalse(
            response.context['task'].filter(task_note=task_2.task_note).exists()
        )
        self.assertFalse(
            response.context['task'].filter(task_note=task_4.task_note).exists()
        )
        # special case 'tag' - filtering for tag 1 returns only tag 1 itself
        self.assertTrue(
            response.context['tag'].filter(tag_name=tag_1.tag_name).exists()
        )
        self.assertFalse(
            response.context['tag'].filter(tag_name=tag_3.tag_name).exists()
        )

    def test_assignment_view_user_filter_context(self):
        """user filter applied"""

        # login testuser
        self.client.login(
            username='testuser_assignment_filter', password='B1z2nn60R4XUMmRoqcA7'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_filter')
        # get objects
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        artifact_2 = Artifact.objects.get(artifact_name='artifact_2')
        artifact_3 = Artifact.objects.get(artifact_name='artifact_3')
        artifact_4 = Artifact.objects.get(artifact_name='artifact_4')
        case_1 = Case.objects.get(case_name='case_1')
        case_2 = Case.objects.get(case_name='case_2')
        case_3 = Case.objects.get(case_name='case_3')
        case_4 = Case.objects.get(case_name='case_4')
        note_1 = Note.objects.get(note_title='note_1')
        note_2 = Note.objects.get(note_title='note_2')
        note_3 = Note.objects.get(note_title='note_3')
        note_4 = Note.objects.get(note_title='note_4')
        reportitem_1 = Reportitem.objects.get(reportitem_note='reportitem_1')
        reportitem_2 = Reportitem.objects.get(reportitem_note='reportitem_2')
        reportitem_3 = Reportitem.objects.get(reportitem_note='reportitem_3')
        reportitem_4 = Reportitem.objects.get(reportitem_note='reportitem_4')
        system_1 = System.objects.get(system_name='system_1')
        system_2 = System.objects.get(system_name='system_2')
        system_3 = System.objects.get(system_name='system_3')
        system_4 = System.objects.get(system_name='system_4')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        tag_2 = Tag.objects.get(tag_name='tag_2')
        tag_3 = Tag.objects.get(tag_name='tag_3')
        tag_4 = Tag.objects.get(tag_name='tag_4')
        task_1 = Task.objects.get(task_note='task_1')
        task_2 = Task.objects.get(task_note='task_2')
        task_3 = Task.objects.get(task_note='task_3')
        task_4 = Task.objects.get(task_note='task_4')

        # change config
        set_user_config(test_user, None, None, test_user)

        # get response
        response = self.client.get('/config/assignment/')
        # compare
        self.assertTrue(
            response.context['artifact']
            .filter(artifact_name=artifact_4.artifact_name)
            .exists()
        )
        self.assertTrue(
            response.context['case'].filter(case_name=case_4.case_name).exists()
        )
        self.assertTrue(
            response.context['note'].filter(note_title=note_4.note_title).exists()
        )
        self.assertTrue(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_4.reportitem_note)
            .exists()
        )
        self.assertTrue(
            response.context['system'].filter(system_name=system_4.system_name).exists()
        )
        self.assertTrue(
            response.context['tag'].filter(tag_name=tag_4.tag_name).exists()
        )
        self.assertTrue(
            response.context['task'].filter(task_note=task_4.task_note).exists()
        )
        self.assertFalse(
            response.context['artifact']
            .filter(artifact_name=artifact_1.artifact_name)
            .exists()
        )
        self.assertFalse(
            response.context['artifact']
            .filter(artifact_name=artifact_2.artifact_name)
            .exists()
        )
        self.assertFalse(
            response.context['artifact']
            .filter(artifact_name=artifact_3.artifact_name)
            .exists()
        )
        self.assertFalse(
            response.context['case'].filter(case_name=case_1.case_name).exists()
        )
        self.assertFalse(
            response.context['case'].filter(case_name=case_2.case_name).exists()
        )
        self.assertFalse(
            response.context['case'].filter(case_name=case_3.case_name).exists()
        )
        self.assertFalse(
            response.context['note'].filter(note_title=note_1.note_title).exists()
        )
        self.assertFalse(
            response.context['note'].filter(note_title=note_2.note_title).exists()
        )
        self.assertFalse(
            response.context['note'].filter(note_title=note_3.note_title).exists()
        )
        self.assertFalse(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_1.reportitem_note)
            .exists()
        )
        self.assertFalse(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_2.reportitem_note)
            .exists()
        )
        self.assertFalse(
            response.context['reportitem']
            .filter(reportitem_note=reportitem_3.reportitem_note)
            .exists()
        )
        self.assertFalse(
            response.context['system'].filter(system_name=system_1.system_name).exists()
        )
        self.assertFalse(
            response.context['system'].filter(system_name=system_2.system_name).exists()
        )
        self.assertFalse(
            response.context['system'].filter(system_name=system_3.system_name).exists()
        )
        self.assertFalse(
            response.context['tag'].filter(tag_name=tag_1.tag_name).exists()
        )
        self.assertFalse(
            response.context['tag'].filter(tag_name=tag_2.tag_name).exists()
        )
        self.assertFalse(
            response.context['tag'].filter(tag_name=tag_3.tag_name).exists()
        )
        self.assertFalse(
            response.context['task'].filter(task_note=task_1.task_note).exists()
        )
        self.assertFalse(
            response.context['task'].filter(task_note=task_2.task_note).exists()
        )
        self.assertFalse(
            response.context['task'].filter(task_note=task_3.task_note).exists()
        )
