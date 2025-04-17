from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


LEVEL_CHOICES = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
]


class Workout(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES)


    def __str__(self):
        return self.title

