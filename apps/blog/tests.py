from django.test import TestCase
from .models import Category, Post


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Projetos')
        return super().setUp()
    

    def test_category_name(self):
        category = Category.objects.get(name='Projetos')
        self.assertEqual(category.name, 'Projetos')
        

class PostTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Teste')
        Post.objects.create(title='Post de Teste', content='Conteudo do post', category='Teste')
        return super().setUp()
    

    def test_post_title(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Post de Teste')
    
    def test_post_catogory_id(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.category.id, 1)

    