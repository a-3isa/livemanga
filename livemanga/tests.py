from django.test import SimpleTestCase
from rest_framework.test import APIClient

from .serializers import MangaSerializer


class SafeNameTests(SimpleTestCase):
    def test_rejects_names_that_leave_the_folder(self):
        for bad in ['../etc', 'a/b', 'a\\b', 'C:x', '..', '.hidden', ' padded ', '']:
            with self.subTest(bad=bad):
                with self.assertRaises(Exception):
                    MangaSerializer._safe_path_part(bad)

    def test_accepts_plain_names(self):
        for good in ['one-piece', 'Chapter 12', 'gogo_ch1']:
            with self.subTest(good=good):
                self.assertEqual(MangaSerializer._safe_path_part(good), good)

    def test_upload_rejects_traversal_before_touching_the_disk(self):
        response = APIClient().post(
            '/mangaupload/',
            {'anime_name': '../../outside', 'chapter_name': '1', 'voices_number': 1},
            format='multipart',
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('anime_name', response.json())
