class Comment:
    def __init__(self, user, comment):
        self.user: User = user
        self.comment: str = comment

class Post:
    postId = 100
    
    def __init__(self, post: str):
        Post.postId += 1
        self.post_id = Post.postId
        self.post_content = post
        self._likes: int = 0
        self._comment: list[Comment] = []
        

class User:
    userId = 0
    
    def __init__(self, user_name: str):
        User.userId += 1
        self.user_id = User.userId
        self.user_name = user_name
        self.posts: dict[int, Post] = {}
        self._follow: set[int] = set()
        
    def user_posts(self):
        head = ["Post ID", "Post Content"]
        print(f"{head[0]:10} {head[1]:10}")
        print("_" * 45)
        for val in self.posts.values():
            print(f"{val.post_id:<10} {val.post_content:<10}")
        
class Inventory:
    
    def __init__(self):
        self._user_list: dict[int, User] = {}
        self._post_list: dict[int, Post] = {}
        
class SocialMediaEngine:
    
        
    def __init__(self):
        self.invetory = Inventory()
        self._user_list = self.invetory._user_list
        self._post_list = self.invetory._post_list
        
    def createUser(self, user_name: str):
        user = User(user_name)
        self._user_list[user.user_id] = user
        print(f"User '{user_name}' created successfully. User ID: {user.user_id}")
        
    def userFollowAndUnfollow(self, action:str, source_id:int, target_id:int):
        source_user = self._user_list[source_id]
        target_user = self._user_list[target_id]
        
        if action.lower() == 'f':
            target_user._follow.add(source_id)
        else:
            target_user._follow.remove(source_id)
        
        print(f"User {source_id} ({source_user.user_name}) is now following User {target_id} ({target_user.user_name})")
        print(f"Now, User {target_id} ({target_user.user_name}) have {len(target_user._follow)} followers")
        
    def createPost(self, user_id, content):
        user = self._user_list[user_id]
        post = Post(content)
        user.posts[post.post_id] = post
        
        self._post_list[post.post_id] = post
        
        print(f"User {user.user_id} ({user.user_name}) posts")
        user.user_posts()
        
    def postLikeAndCommand(self, action:str, user_id:int, post_id:int):
        user = self._user_list[user_id]
        post = self._post_list[post_id]
        
        
        if action.lower() == "l":
            post._likes += 1
        else:
            content = input("Enter the Comment : ")
            comment = Comment(user, content)
            post._comment.append(comment)
            
    def viweNewsFeed(self, user_id):
        user = self._user_list[user_id]
        post = user.posts
        
        print("=" *  50)
        print(f"NEWS FEED FOR USER: {user.user_name} ({user.user_id})")
        print("=" * 50)
        for val in self._post_list.values():
            print(f"Post ID : {val.post_id}")
            print(f"Content : {val.post_content}")
            print(f"Likes: {val._likes} | Comments : {len(val._comment)}")
            for com in val._comment:
                print(f"Comment by {com.user.user_name}: {com.comment}")

if __name__ == "__main__":
    sme = SocialMediaEngine()
    
    while True:
        option = int(input("""
              1. Create User
              2. Follow / Unfollow User
              3. Create Post
              4. Like/ Comment on Post
              5. View News Feed
              6. Exit
              Select an Option (1-6) : """))
        
        if option == 1:
            name = input("Enter the user name : ")
            sme.createUser(name)
            
        elif option == 2:
            ans = input("Enter Action Type (F/U) : ")
            source_id = int(input("Enter Source User ID : "))
            target_id = int(input("Enter Target User ID : "))
            if source_id in sme._user_list and target_id in sme._user_list:
                sme.userFollowAndUnfollow(ans, source_id, target_id)
            else:
                print("Given source or target id is invalid")
                
        elif option == 3:
            user_id = int(input("Enter User ID : "))
            content = input("Enter the Post : ")
            if user_id in sme._user_list:
                sme.createPost(user_id, content)
                
        elif option == 4:
            action = input("Enter Action Type (L/C) : ")
            user_id = int(input("Enter the User ID : "))
            if user_id in sme._user_list:
                post_id = int(input("Enter the Post ID : "))
                if post_id in sme._post_list:
                    sme.postLikeAndCommand(action, user_id, post_id)
                else:
                    print("Invalid Post ID")
            else:
                print("Invalid User ID")
        elif option == 5:
            user_id = int(input("Enter User Id"))
            sme.viweNewsFeed(user_id)
        else:
            break
        