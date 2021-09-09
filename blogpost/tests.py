from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Blog

# Create your tests here.




class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_post = Blog.objects.create(
            author = testuser1,
            title = 'This is the title',
            body = 'This is the body'
        )
        test_post.save()

    def test_blog_content(self):
        post = Blog.objects.get(id=1)
        actual_author = str(post.author)
        actual_title = str(post.title)
        actual_body = str(post.body)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_title, 'This is the title')
        self.assertEqual(actual_body, 'This is the body')