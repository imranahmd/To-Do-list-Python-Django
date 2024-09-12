from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')
        # Create a task
        self.task = Task.objects.create(title='Test Task', description='Test Description', user=self.user)

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertEqual(self.task.user.username, 'testuser')
        self.assertFalse(self.task.is_complete)  # Assuming the default is incomplete

class TaskViewTest(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')
        # Log in the user
        self.client.login(username='testuser', password='password')
        # Create a task
        self.task = Task.objects.create(title='Test Task', description='Test Description', user=self.user)

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))  # Assuming your URL name for listing tasks is 'task_list'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_list.html')  # Adjust to your actual template name

    def test_task_create_view(self):
        response = self.client.post(reverse('task_create'), {'title': 'New Task', 'description': 'New Description'})
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after creation
        self.assertEqual(Task.objects.count(), 2)  # Two tasks now: one from setUp, one new

    def test_task_update_view(self):
        response = self.client.post(reverse('task_update', args=[self.task.id]), {'title': 'Updated Task'})
        self.task.refresh_from_db()
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after updating
        self.assertEqual(self.task.title, 'Updated Task')

    def test_task_delete_view(self):
        response = self.client.post(reverse('task_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after deletion
        self.assertEqual(Task.objects.count(), 0)  # Task should be deleted

