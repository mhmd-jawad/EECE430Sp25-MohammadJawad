from django.db import models


POSITION_CHOICES = [
    ('Setter', 'Setter'),
    ('Outside Hitter', 'Outside Hitter'),
    ('Middle Blocker', 'Middle Blocker'),
    ('Opposite Hitter', 'Opposite Hitter'),
    ('Libero', 'Libero'),
    ('Defensive Specialist', 'Defensive Specialist'),
]


class VolleyPlayer(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_joined = models.DateField()
    position = models.CharField(max_length=30, choices=POSITION_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    contact_person = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.player_id} - {self.name} ({self.position})"
