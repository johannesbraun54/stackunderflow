from django.contrib.auth.models import User
from forum_app.models import Question, Answer, Like


user1, _ = User.objects.get_or_create(username='alice', is_staff=True)
user1.set_password('asdasd')
user1.save()

user2, _ = User.objects.get_or_create(username='bob')
user2.set_password('asdasd')
user2.save()

user3, _ = User.objects.get_or_create(username='charlie')
user3.set_password('asdasd')
user3.save()

user4, _ = User.objects.get_or_create(username='dave')
user4.set_password('asdasd')
user4.save()

categories = [choice[0] for choice in Question.CATEGORY_CHOICES]


question1 = Question.objects.create(title='How to optimize a React component for performance?', content='I have a React component that is slow to render. What are some strategies to optimize it?', author=user1, category=categories[0])
question2 = Question.objects.create(title='Best practices for securing a Django application?', content='What are the best practices for securing a Django application against common web vulnerabilities?', author=user2, category=categories[1])
question3 = Question.objects.create(title='How to perform data cleaning in Python?', content='I have a large dataset that needs cleaning. What are the best libraries and methods to perform data cleaning in Python?', author=user3, category=categories[2])
question4 = Question.objects.create(title='Tips for creating a responsive web design?', content='What are some tips and best practices for creating a responsive web design that works well on all devices?', author=user4, category=categories[3])
question5 = Question.objects.create(title='How to set up a CI/CD pipeline for a Django project?', content='I want to set up a CI/CD pipeline for my Django project. What are the steps and best tools to use?', author=user1, category=categories[4])
question6 = Question.objects.create(title='How to secure a REST API?', content='What are the best practices for securing a REST API, especially in terms of authentication and authorization?', author=user2, category=categories[5])
question7 = Question.objects.create(title='How to handle state management in React?', content='What are the best practices for handling state management in a large React application?', author=user3, category=categories[0])
question8 = Question.objects.create(title='How to optimize database queries in Django?', content='I have some slow database queries in my Django application. What are some strategies to optimize them?', author=user4, category=categories[1])
question9 = Question.objects.create(title='How to perform exploratory data analysis in Python?', content='I have a new dataset and want to perform exploratory data analysis. What are the best libraries and methods to use in Python?', author=user1, category=categories[2])
question10 = Question.objects.create(title='How to create a mobile-first design?', content='What are the best practices for creating a mobile-first design that scales well to larger screens?', author=user2, category=categories[3])

Like.objects.create(user=user1, question=question1)
Like.objects.create(user=user2, question=question2)
Like.objects.create(user=user3, question=question3)
Like.objects.create(user=user4, question=question4)
Like.objects.create(user=user1, question=question5)
Like.objects.create(user=user2, question=question6)
Like.objects.create(user=user3, question=question7)
Like.objects.create(user=user4, question=question8)
Like.objects.create(user=user1, question=question9)
Like.objects.create(user=user2, question=question10)
Like.objects.create(user=user3, question=question1)
Like.objects.create(user=user4, question=question2)
Like.objects.create(user=user1, question=question3)
Like.objects.create(user=user2, question=question4)
Like.objects.create(user=user3, question=question5)
Like.objects.create(user=user4, question=question6)
Like.objects.create(user=user1, question=question7)
Like.objects.create(user=user2, question=question8)
Like.objects.create(user=user3, question=question9)
Like.objects.create(user=user4, question=question10)
# Like.objects.create(user=user1, question=question1) # UNIQUE constraint failed
# Like.objects.create(user=user2, question=question2) # UNIQUE constraint failed
# Like.objects.create(user=user3, question=question3) # UNIQUE constraint failed
# Like.objects.create(user=user4, question=question4) # UNIQUE constraint failed
# Like.objects.create(user=user1, question=question5) # UNIQUE constraint failed
# Like.objects.create(user=user2, question=question6) # UNIQUE constraint failed


Answer.objects.create(content='You can use React.memo to optimize your component.', author=user1, question=question1)
Answer.objects.create(content='Use Django\'s built-in security features like CSRF protection and secure password hashing.', author=user2, question=question2)
Answer.objects.create(content='You can use pandas for data cleaning in Python.', author=user3, question=question3)
Answer.objects.create(content='Use media queries and flexible grid layouts for responsive design.', author=user4, question=question4)
Answer.objects.create(content='Use tools like Jenkins or GitHub Actions for CI/CD.', author=user1, question=question5)
Answer.objects.create(content='Use OAuth2 for authentication and role-based access control for authorization.', author=user2, question=question6)
Answer.objects.create(content='Use React\'s Context API or Redux for state management.', author=user3, question=question7)
Answer.objects.create(content='Use Django\'s select_related and prefetch_related for query optimization.', author=user4, question=question8)
Answer.objects.create(content='Use pandas and matplotlib for exploratory data analysis in Python.', author=user1, question=question9)
Answer.objects.create(content='Start with a mobile-first approach and use CSS media queries to adjust for larger screens.', author=user2, question=question10)
Answer.objects.create(content='Another tip is to use lazy loading for images.', author=user3, question=question1)
Answer.objects.create(content='Consider using Django\'s built-in security middleware.', author=user4, question=question2)
Answer.objects.create(content='You can also use NumPy for numerical operations in data cleaning.', author=user1, question=question3)
Answer.objects.create(content='Ensure your design is fluid and uses relative units like percentages.', author=user2, question=question4)
Answer.objects.create(content='Automate testing as part of your CI/CD pipeline.', author=user3, question=question5)






# question1 = Question.objects.create(title='Question 1', content='Content of question 1', author=user1, category=categories[0])
# question2 = Question.objects.create(title='Question 2', content='Content of question 2', author=user2, category=categories[1])
# question3 = Question.objects.create(title='Question 3', content='Content of question 3', author=user3, category=categories[2])
# question4 = Question.objects.create(title='Question 4', content='Content of question 4', author=user4, category=categories[3])
# question5 = Question.objects.create(title='Question 5', content='Content of question 5', author=user1, category=categories[4])
# question6 = Question.objects.create(title='Question 6', content='Content of question 6', author=user2, category=categories[5])
# question7 = Question.objects.create(title='Question 7', content='Content of question 7', author=user3, category=categories[0])
# question8 = Question.objects.create(title='Question 8', content='Content of question 8', author=user4, category=categories[1])
# question9 = Question.objects.create(title='Question 9', content='Content of question 9', author=user1, category=categories[2])
# question10 = Question.objects.create(title='Question 10', content='Content of question 10', author=user2, category=categories[3])


# Like.objects.create(user=user1, question=question1)
# Like.objects.create(user=user2, question=question2)
# Like.objects.create(user=user3, question=question3)
# Like.objects.create(user=user4, question=question4)
# Like.objects.create(user=user1, question=question5)
# Like.objects.create(user=user2, question=question6)
# Like.objects.create(user=user3, question=question7)
# Like.objects.create(user=user4, question=question8)
# Like.objects.create(user=user1, question=question9)
# Like.objects.create(user=user2, question=question10)
# Like.objects.create(user=user3, question=question1)
# Like.objects.create(user=user4, question=question2)
# Like.objects.create(user=user1, question=question3)
# Like.objects.create(user=user2, question=question4)
# Like.objects.create(user=user3, question=question5)
# Like.objects.create(user=user4, question=question6)
# Like.objects.create(user=user1, question=question7)
# Like.objects.create(user=user2, question=question8)
# Like.objects.create(user=user3, question=question9)
# Like.objects.create(user=user4, question=question10)
# Like.objects.create(user=user1, question=question1)
# Like.objects.create(user=user2, question=question2)
# Like.objects.create(user=user3, question=question3)
# Like.objects.create(user=user4, question=question4)
# Like.objects.create(user=user1, question=question5)
# Like.objects.create(user=user2, question=question6)


# Answer.objects.create(content='Answer 1', author=user1, question=question1)
# Answer.objects.create(content='Answer 2', author=user2, question=question2)
# Answer.objects.create(content='Answer 3', author=user3, question=question3)
# Answer.objects.create(content='Answer 4', author=user4, question=question4)
# Answer.objects.create(content='Answer 5', author=user1, question=question5)
# Answer.objects.create(content='Answer 6', author=user2, question=question6)
# Answer.objects.create(content='Answer 7', author=user3, question=question7)
# Answer.objects.create(content='Answer 8', author=user4, question=question8)
# Answer.objects.create(content='Answer 9', author=user1, question=question9)
# Answer.objects.create(content='Answer 10', author=user2, question=question10)
# Answer.objects.create(content='Answer 11', author=user3, question=question1)
# Answer.objects.create(content='Answer 12', author=user4, question=question2)
# Answer.objects.create(content='Answer 13', author=user1, question=question3)
# Answer.objects.create(content='Answer 14', author=user2, question=question4)
# Answer.objects.create(content='Answer 15', author=user3, question=question5)