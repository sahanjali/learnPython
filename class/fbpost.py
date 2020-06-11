from datetime import datetime

class FacebookPost:
    'Represent a fb post'
    def __init__(self, author, content):
        self.num_likes = 0
        self.author = author
        self.comments = []
        self.posted_date = datetime.now()
        self.content = content
    
    def add_like(self):
        self.num_likes = self.num_likes + 1
    
    def add_comment(self, comment):
        self.comments.append(comment)

    def display_post(self):
         print('------ FB POST ------')
         print('Author:{}'.format(self.author))
         print('Likes:', self.num_likes)
         print('PostedDate:', self.posted_date)
         print('Content:', self.content)
         print('Comments:', self.comments)
         print('----------------------')


fb1 = FacebookPost('Anjai Sah', 'Happy Birthday to the love of my life! Yay!')
fb1.display_post()
fb1.add_like()
fb1.display_post()
fb1.add_like()
fb1.add_comment('Happy Birthday PJ!')
fb1.display_post()

fbPost2 = FacebookPost('Pramod Jayswal', 'Thank you all for wishing me my bday')
fbPost2.display_post()



