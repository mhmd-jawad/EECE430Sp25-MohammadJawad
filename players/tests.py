from django.test import TestCase, Client
from django.urls import reverse
from .models import VolleyPlayer


class VolleyPlayerModelTest(TestCase):
    def setUp(self):
        self.player = VolleyPlayer.objects.create(
            name='John Doe',
            date_joined='2025-01-15',
            position='Setter',
            salary=5000.00,
            contact_person='Jane Doe',
        )

    def test_player_creation(self):
        self.assertEqual(self.player.name, 'John Doe')
        self.assertEqual(self.player.position, 'Setter')
        self.assertEqual(str(self.player), f"{self.player.player_id} - John Doe (Setter)")


class VolleyPlayerViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.player = VolleyPlayer.objects.create(
            name='Alice Smith',
            date_joined='2025-03-01',
            position='Libero',
            salary=3000.00,
            contact_person='Bob Smith',
        )

    def test_player_list_view(self):
        response = self.client.get(reverse('player_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alice Smith')

    def test_add_player_get(self):
        response = self.client.get(reverse('add_player'))
        self.assertEqual(response.status_code, 200)

    def test_add_player_post(self):
        response = self.client.post(reverse('add_player'), {
            'name': 'New Player',
            'date_joined': '2025-06-01',
            'position': 'Setter',
            'salary': '4500.00',
            'contact_person': 'Coach A',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(VolleyPlayer.objects.filter(name='New Player').exists())

    def test_view_player_detail(self):
        response = self.client.get(reverse('view_player', args=[self.player.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alice Smith')

    def test_edit_player(self):
        response = self.client.post(reverse('edit_player', args=[self.player.pk]), {
            'name': 'Alice Updated',
            'date_joined': '2025-03-01',
            'position': 'Libero',
            'salary': '3500.00',
            'contact_person': 'Bob Smith',
        })
        self.assertEqual(response.status_code, 302)
        self.player.refresh_from_db()
        self.assertEqual(self.player.name, 'Alice Updated')

    def test_delete_player(self):
        response = self.client.post(reverse('delete_player', args=[self.player.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(VolleyPlayer.objects.filter(pk=self.player.pk).exists())
