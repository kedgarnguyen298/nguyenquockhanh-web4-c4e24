import mlab
from models.user import User
from models.post import Post

mlab.connect()

# a_random_user = User.objects(username="huong").first()
# if a_random_user is None:
#     print("User not found")
# else:
#     new_post = Post(title="Bai viet so 3 cua huong",
#                     content="Huongday huhu",
#                     owner=a_random_user)
#     new_post.save()
#     print("Done")

# Post => Owner
# for post in Post.objects():
#     print(post.title, "by", post.owner.username)

# Owner => Posts
user = User.objects(username="khanh").first()
posts = Post.objects(owner=user)
for post in posts:
    print(post.title)
