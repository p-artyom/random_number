from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework.test import APIClient

User = get_user_model()


class UrlsTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = mixer.blend(User)

        cls.number = mixer.blend('number.Number')

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.authorized_user = APIClient()
        cls.authorized_user.force_authenticate(cls.user)

        cls.urls = {
            'numbers': '/api/number/',
            'number': f'/api/number/{cls.number.id}/',
            'unknown_number': '/api/number/99/',
            'docs': '/api/docs/',
            'get_random_number': '/api/get_random_number/',
        }

    def test_http_statuses_get_request(self) -> None:
        '''URL-адрес возвращает соответствующий статус при GET запросе.'''

        urls_statuses_users = (
            (self.urls.get('numbers'), HTTPStatus.OK, self.authorized_user),
            (self.urls.get('numbers'), HTTPStatus.UNAUTHORIZED, self.client),
            (self.urls.get('number'), HTTPStatus.OK, self.authorized_user),
            (self.urls.get('number'), HTTPStatus.UNAUTHORIZED, self.client),
            (
                self.urls.get('unknown_number'),
                HTTPStatus.NOT_FOUND,
                self.authorized_user,
            ),
            (
                self.urls.get('unknown_number'),
                HTTPStatus.UNAUTHORIZED,
                self.client,
            ),
            (self.urls.get('docs'), HTTPStatus.OK, self.client),
            (
                self.urls.get('get_random_number'),
                HTTPStatus.OK,
                self.authorized_user,
            ),
            (
                self.urls.get('get_random_number'),
                HTTPStatus.UNAUTHORIZED,
                self.client,
            ),
        )
        for url, status, user in urls_statuses_users:
            with self.subTest(url=url, status=status, user=user):
                self.assertEqual(user.get(url).status_code, status)

    def test_http_statuses_post_request(self) -> None:
        '''URL-адрес возвращает соответствующий статус при POST запросе.'''

        urls_statuses_users_data = (
            (
                self.urls.get('numbers'),
                HTTPStatus.METHOD_NOT_ALLOWED,
                self.authorized_user,
                {},
            ),
            (
                self.urls.get('number'),
                HTTPStatus.METHOD_NOT_ALLOWED,
                self.authorized_user,
                {},
            ),
            (
                self.urls.get('get_random_number'),
                HTTPStatus.METHOD_NOT_ALLOWED,
                self.authorized_user,
                {},
            ),
        )
        for url, status, user, data in urls_statuses_users_data:
            with self.subTest(url=url, status=status, user=user):
                self.assertEqual(
                    user.post(url, data=data, format='json').status_code,
                    status,
                )
