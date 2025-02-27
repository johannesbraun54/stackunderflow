from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from forum_app.models import Answer, Question
from forum_app.api.serializers import AnswerSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class AnswerTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='der_tester', password='der_test')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.question = Question.objects.create(
            title='Test Question', content='Test Content', author=self.user, category='frontend')
        self.question.save()
        self.answer = Answer.objects.create(content="Das ist eine Beispielantwort!",
                                            author=self.user,
                                            question=self.question)

    def test_create_answer(self):
        url = reverse('answer-list-create')
        data = {
            "content": "Das ist eine Beispielantwort!",
            "author": self.user.id,
            "question": self.question.id
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_answer_list(self):
        url = reverse('answer-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_answer_detail(self):
        new_data = {
            "content": "Das ist eine Beispielantwort!",
            "author": self.user.id,
            "question": self.question.id,
        }

        url = reverse('answer-detail', kwargs={'pk': self.answer.id})
        expected_content = 'Das ist ein Test!'
        self.answer.content = 'Das ist ein Test!'
        self.answer.user = self.user
        response = self.client.put(url, new_data, format='json')
        self.assertEqual(expected_content, self.answer.content)
