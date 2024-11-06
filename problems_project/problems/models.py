from django.db import models

class Problem(models.Model):
    title = models.CharField(max_length=255)
    difficulty = models.IntegerField()  # Murakkablik darajasi (% formatida)
    time_limit = models.IntegerField()  # Vaqt chegarasi (ms)
    memory_limit = models.IntegerField()  # Xotira chegarasi (MB)
    description = models.TextField()  # Masala berilishi
    input_format = models.TextField()  # Kirish ma'lumotlari
    output_format = models.TextField()  # Chiqish ma'lumotlari
    example = models.TextField()  # Misol

    def __str__(self):
        return self.title
