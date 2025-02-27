from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from forum_app.models import Question
from forum_app.api.serializers import QuestionSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class LikeTests(APITestCase):
    
        def test_get_like(self):
            url = reverse('like-list')
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

class QuestionTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', is_staff=True, password='testpassword',)
        self.question = Question.objects.create(title='Test Question', content='Test Content', author=self.user, category='frontend')
        # self.client = APIClient()
        # self.client.login(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
     
     
    def test_list_post_question(self):
        url = reverse('question-list')
        data = {'title': 'Question1',
                'content': 'Content1',
                'author': self.user.id,
                'category':'frontend'}
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_detail_question(self):
        url = reverse('question-detail', kwargs={'pk': self.question.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        expected_data = QuestionSerializer(self.question).data
        self.assertEqual(response.data, expected_data)
        self.assertDictEqual(response.data, expected_data)
        self.assertJSONEqual(response.content, expected_data)
        self.assertContains(response, 'title')
        
    def test_delete_question(self):
        url = reverse('question-detail', kwargs={'pk':self.question.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
