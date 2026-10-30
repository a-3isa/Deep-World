from unittest import mock

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import SimpleTestCase
from rest_framework.test import APIClient

from . import views


class StyleNameTests(SimpleTestCase):
    def test_accepts_model_names(self):
        for name in ['starry_night', 'wave-2', 'Mosaic']:
            with self.subTest(name=name):
                self.assertTrue(views.STYLE_NAME.fullmatch(name))

    def test_rejects_shell_and_path_characters(self):
        for name in ['x; rm -rf /', 'a b', '../secret', '$(id)', 'a|b', '']:
            with self.subTest(name=name):
                self.assertIsNone(views.STYLE_NAME.fullmatch(name))


class ImageEndpointTests(SimpleTestCase):
    @mock.patch.object(views, 'run_script')
    @mock.patch.object(views.fs, 'save', return_value='photo.png')
    def test_bad_style_is_refused_and_nothing_runs(self, _save, run_script):
        image = SimpleUploadedFile('photo.png', b'not really a png', content_type='image/png')
        response = APIClient().post('/', {'image': image, 'style': 'x; touch pwned'}, format='multipart')
        self.assertEqual(response.status_code, 400)
        run_script.assert_not_called()

    @mock.patch('builtins.open', mock.mock_open(read_data='203.0.113.7'))
    @mock.patch.object(views, 'run_script')
    @mock.patch.object(views.fs, 'save', return_value='photo.png')
    def test_good_style_runs_the_script_with_separate_arguments(self, _save, run_script):
        image = SimpleUploadedFile('photo.png', b'not really a png', content_type='image/png')
        response = APIClient().post('/', {'image': image, 'style': 'starry_night'}, format='multipart')
        self.assertEqual(response.status_code, 200)
        args = run_script.call_args.args
        self.assertEqual(args[0], 'test.py')
        self.assertTrue(args[1].endswith('photo.png'))
        self.assertEqual(args[2], 'starry_night')
