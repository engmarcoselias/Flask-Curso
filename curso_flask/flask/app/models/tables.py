from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.integer,prmary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.string)
    name = db.Column(db.string)
    email = db.Column(db.string, unique=True)

    def __init__(self,username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "User %r>" % self.username
    
    class Post(db.Model):
        __tablename__="post"

        id = db.Column(db.Integer, primary_key=True)
        content = db.Column(db.Text)
        user_id = db.Column(db.Integer,db.Foreignkey('users.id'))#foreignkey e uma relação entrea a tabela pai e a tabela filho

        user = db.relationship('User',foreign_keys=user_id)

        def __init__(self,content,user_id):
            self.content = content
            self.user_id = user_id

        def __repr__(self):
            return "<Post %r>" %self.id
        
    class Follow(db.MOdel):
        __tablename__ = "follow"

        id = db.Column(db.Integer, primary_key=True)
        user_id =db.Column(db.Integer, db.Foreignkey('users.id'))
        follower_id = db.Column(db.Integer, db.Foreignkey('users.id'))

        user = db.relationship('User',foreign_keys=user_id)
        follower = db.relationship('User',foreign_keys=user_id)