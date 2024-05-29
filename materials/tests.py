from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Lession, Course, Subscription
from users.models import User


# Create your tests here.

class MaterialsTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(
            email="admin@service.py"
        )
        self.course = Course.objects.create(title='DRFTests', description='DRF Tests description', owner=self.user)
        self.lession = Lession.objects.create(title='Tests',
                                              description='Tests description',
                                              course=self.course,
                                              owner=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_lession_create(self):
        """ Тестирование создания урока """
        data = {
            "title": "План урока",
            "description": "Плановый урок",
            "URL": "https://youtube.com/TeSt",
        }
        response = self.client.post('/lessions/create/', data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.assertEquals(
            response.json(),
            {'id': 2, "title": "План урока", "description": "Плановый урок", "preview": None,
             "URL": "https://youtube.com/TeSt",
             "course": None, "owner": 1}
        )

        self.assertTrue(Lession.objects.all().exists())

        self.assertEquals(Lession.objects.all().count(), 2)

    def test_lession_retrieve(self):
        """ Тестирование детального просмотра урока"""
        response = self.client.get(
            f'/lessions/{self.lession.pk}/'
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            {'id': 4, 'title': 'Tests', 'description': 'Tests description', 'preview': None, 'URL': '', 'course': 3,
             'owner': 3}
        )

    def test_lessions_list(self):
        """Тест просмотра списка уроков"""
        response = self.client.get(
            '/lessions/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()

        self.assertEquals(
            data.get('next'),
            None
        )

    def test_lession_update(self):
        data = {
            "title": "План теста",
            "URL": "https://youtube.com/pagination"
        }
        response = self.client.patch(
            f'/lessions/update/{self.lession.pk}/',
            data=data
        )
        new_data = response.json()

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            new_data.get('title'),
            "План теста"
        )

        self.assertEquals(
            self.lession.description,
            new_data.get('description')
        )

    def test_lession_delete(self):
        response = self.client.delete(
            f'/lessions/delete/{self.lession.pk}/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEquals(
            Lession.objects.all().count(),
            0
        )


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@service.py")
        self.user.set_password('1')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Python_29", owner=self.user)

    def test_subscribe(self):
        data = {
            "course": self.course.pk
        }
        response = self.client.post(
            '/course/subscribe/',
            data=data
        )
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {'message': 'Подписка включена'})

    def test_unsubscribe(self):
        data = {
            "course": self.course.pk
        }
        Subscription.objects.create(course=self.course, user=self.user)
        response = self.client.post(
            '/course/subscribe/',
            data=data
        )
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {'message': 'Подписка отключена'})
