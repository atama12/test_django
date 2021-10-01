from djongo import models # djongoのモデルを利用する

class Author(models.Model):
    name = models.TextField()
    age = models.IntegerField(blank=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.TextField()
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)