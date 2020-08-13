from django.db import models


class Text(models.Model):
    text = models.TextField()

    def __str__(self):
        return "{}...".format(self.text[:50])


class Word(models.Model):
    FREQUENCY = (
        ("high", "high"),
        ("average", "average"),
        ("low", "low"),
    )
    word = models.CharField(max_length=40)
    amount = models.PositiveIntegerField()
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=10, choices=FREQUENCY)

    def __str__(self):
        return self.word
