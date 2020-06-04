class animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(20), nullable = False)
 
class fruits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(10), nullable = False)
 
class colour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(10), nullable = False)