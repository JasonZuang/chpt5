from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
# Create your tests here.

class BlogTests(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username = 'testuser',
			email = 'test@email.com',
			password = 'secret'
			)
		self.post = Post.objects.create(
			title = 'Test Post',
			body = 'Test Body',
			author = self.user,
			)
	
	def test_string_representation(self):
		post = Post(title='A sample title')
		self.assertEqual(str(post),post.title)

	def test_post_content(self):
		self.assertEqual(f'{self.post.title}','Test Post')
		self.assertEqual(f'{self.post.author}','testuser')
		self.assertEqual(f'{self.post.body}','Test Body')


