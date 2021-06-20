from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.forms import NoteForm
from dfirtrack_main.models import Case
from dfirtrack_main.models import Casepriority
from dfirtrack_main.models import Casestatus
from dfirtrack_main.models import Notestatus
from dfirtrack_main.models import Tag
from dfirtrack_main.models import Tagcolor


class NoteFormTestCase(TestCase):
    """ note form tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_note', password='i6mefWrT8pAMwzZj8VCf')

        # create object
        casepriority_1 = Casepriority.objects.create(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.create(casestatus_name='casestatus_1')

        # create object
        Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
            casepriority = casepriority_1,
            casestatus = casestatus_1,
        )

        # create object
        Notestatus.objects.create(notestatus_name='notestatus_1')

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        # create object
        Tag.objects.create(tag_name='tag_1', tagcolor = tagcolor_1)

    def test_note_title_form_label(self):
        """ test form label """

        # get object
        form = NoteForm()
        # compare
        self.assertEqual(form.fields['note_title'].label, 'Note title (*)')

    def test_note_content_form_label(self):
        """ test form label """

        # get object
        form = NoteForm()
        # compare
        self.assertEqual(form.fields['note_content'].label, 'Note (*)')

    def test_note_case_form_label(self):
        """ test form label """

        # get object
        form = NoteForm()
        # compare
        self.assertEqual(form.fields['case'].label, 'Corresponding case')

    def test_notestatus_form_label(self):
        """ test form label """

        # get object
        form = NoteForm()
        # compare
        self.assertEqual(form.fields['notestatus'].label, 'Notestatus (*)')

    def test_note_tag_form_label(self):
        """ test form label """

        # get object
        form = NoteForm()
        # compare
        self.assertEqual(form.fields['tag'].label, 'Tags')

    def test_note_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = NoteForm(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_note_title_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = NoteForm(data = {
            'note_title': 'note_1',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_note_content_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = NoteForm(data = {
            'note_title': 'note_1',
            'note_content': 'lorem impsum',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_note_notestatus_form_filled(self):
        """ test minimum form requirements / VALID """

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # get object
        form = NoteForm(data = {
            'note_title': 'note_1',
            'note_content': 'lorem impsum',
            'notestatus': notestatus_1.notestatus_id,
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_note_case_form_filled(self):
        """ test additional form content """

        # get objects
        case_1 = Case.objects.get(case_name='case_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # get object
        form = NoteForm(data = {
            'note_title': 'note_1',
            'note_content': 'lorem impsum',
            'notestatus': notestatus_1.notestatus_id,
            'case': case_1.case_id,
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_note_tag_form_filled(self):
        """ test additional form content """

        # get objects
        tag_1 = Tag.objects.get(tag_name='tag_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # get object
        form = NoteForm(data = {
            'note_title': 'note_1',
            'note_content': 'lorem impsum',
            'notestatus': notestatus_1.notestatus_id,
            'tag': [tag_1.tag_id, ],
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_note_title_proper_chars(self):
        """ test for max length """

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # get object
        form = NoteForm(data = {
            'note_title': 'n' * 250,
            'note_content': 'lorem impsum',
            'notestatus': notestatus_1.notestatus_id,
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_note_title_too_many_chars(self):
        """ test for max length """

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # get object
        form = NoteForm(data = {
            'note_title': 'n' * 251,
            'note_content': 'lorem impsum',
            'notestatus': notestatus_1.notestatus_id,
        })
        # compare
        self.assertFalse(form.is_valid())
