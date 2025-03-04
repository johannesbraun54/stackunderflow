from rest_framework import viewsets, generics, permissions
from forum_app.models import Like, Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer, LikeSerializer
from .permissions import IsOwnerOrAdmin, CustomQuestionPermission
from .throttling import QuestionThrottle, QuestionGetThrottle, QuestionPostThrottle
from rest_framework.throttling import ScopedRateThrottle, UserRateThrottle



class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [CustomQuestionPermission]
    throttle_classes = [UserRateThrottle]
    throttle_scope = 'question-scope'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    # def get_throttles(self):
    #     if self.action == 'list' or self.action == 'retrieve':
    #         return [QuestionGetThrottle()] 
        
    #     if self.action == 'create':
    #         return [QuestionPostThrottle()] 
        
    #     return []

class AnswerListCreateView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    def get_queryset(self):
        queryset = Answer.objects.all()
        
        content_param = self.request.query_params.get('content', None)
        if content_param is not None:
            queryset = queryset.filter(content__icontains=content_param)
        
        username_param = self.request.query_params.get('author', None)
        if username_param is not None:
            queryset = queryset.filter(author__username=username_param)
            
        question_title_param = self.request.query_params.get('question_title',None)
        if question_title_param is not None:
            queryset = queryset.filter(question__title__icontains=question_title_param)
            
        
        return queryset
            


class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsOwnerOrAdmin]


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
