from django.db.models import *
from users.models import User

class TimeStampedModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=100)
    content = TextField()
    view_count = IntegerField(default=0)
    image = ImageField(upload_to="img/")
    likes = ManyToManyField(User, related_name="liked_users")
    
    def __str__(self):
       return self.title

    def comments(self):
        return Comment.objects.filter(post=self)


class Comment(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE)
    post = ForeignKey(Post, on_delete=CASCADE)
    message = TextField()

    def __str__(self):
        return self.message

class Ingredient(TimeStampedModel):
    ingredient_name = CharField(max_length=100)

    def __str__(self):
       return self.ingredient_name


class Postingre(TimeStampedModel):
    post = ForeignKey(Post, on_delete=CASCADE)
    ingredient_name = ForeignKey(Ingredient, on_delete=CASCADE)
    quantity = CharField(max_length=100)

    def __str__(self):
       return self.quantity

       

        

# post-ingredient class를 넣어서 post_id, ingredient_id, ingredient(integer)양을 넣어서 1번 글에 3번 재료가 어느정도 있다 표시 가능
# 아니면 ingredient 모델을 새로 파서 그걸로 many_to_many 관계를 만들어도 됨
# <views.py>
# def create: 부분에
#     post = Post.objects.create           ->      post 먼저 보내주고 그 담에 재료 보내준다
#     post(ingredient)