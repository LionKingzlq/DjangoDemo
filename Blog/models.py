from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.id).join(",").join(self.question_text).join(",").\
            join(self.pub_date.strftime("%Y-%m-%d %H:%M:%S"))


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id).join(",").join(self.choice_text)


class Author(models.Model):
    authorName = models.CharField(max_length=20)
    passWord = models.CharField(max_length=32)

    def __str__(self):
        return str(self.id).join(",").join(self.name).join(",").join(self.passWord)


class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    content = models.CharField(max_length=10000)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id).join(",").join(self.title).join(",").join(self.author_id).\
            join(",").join(self.content).join(",").join(self.votes)


class Tag(models.Model):
    tagName = models.CharField(max_length=10)
    tagTime = models.DateTimeField("date published")

    def __str__(self):
        return str(self.id).join(",").join(self.tagName).join(",").join(self.tagTime.strftime("%Y-%m-%d %H:%M:%S"))


class BlogTag(models.Model):
    blog = models.ForeignKey(Blog)
    tag = models.ForeignKey(Tag)

    def __str__(self):
        return str(self.blog_id).join(",").join(str(self.tag_id))