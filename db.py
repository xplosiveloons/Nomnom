
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

restriction_association_table=db.Table(
    "restriction_association",
    db.Column("recipe_id",db.Integer,db.ForeignKey("recipe.id")),
    db.Column("restriction_id",db.Integer,db.ForeignKey("restriction.id"))

)

class Recipe(db.Model):
    __tablename__="recipe"
    id= db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String,nullable=False)
    description=db.Column(db.String)
    favorited=db.Column(db.Boolean,nullable=False)
    ingredients=db.Column(db.String,nullable=False)

    #ingredients=db.relationship("Ingredient",cascade="delete")
    restrictions= db.relationship("Restriction",secondary=restriction_association_table,back_populates="recipes")

    def __init__(self,**kwargs):
        self.title=kwargs.get("title")
        self.description=kwargs.get("description")
        self.favorited=False
        self.ingredients=kwargs.get("ingredients")
        

    def serialize(self):
        return {
            "id": self.id,
            "title":self.title,
            "description": self.description,
            "favorited":self.favorited,

            "ingredients":self.ingredients,

            "restrictions":[r.simple_serialize() for r in self.restrictions]

        }

    def simple_serialize(self):
        return {
            "id": self.id,
            "title":self.title
            

        }

class Restriction(db.Model):
    __tablename__ = "restriction"
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String, nullable= False)
    description = db.Column(db.String, nullable=False)
    recipes= db.relationship('Recipe', secondary= restriction_association_table, back_populates = 'restrictions')
 
    def __init__(self, **kwargs):
        self.title=kwargs.get("title")
        self.description=kwargs.get("description")
 
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'recipes': [r.simple_serialize() for r in self.recipes]
        }
    
    def simple_serialize(self):
        return self.title  

class Plan(db.Model):
    __tablename__="plan"
    id= db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String, nullable= False)
    breakfast=db.Column(db.String, nullable= False)
    lunch=db.Column(db.String, nullable= False)
    dinner=db.Column(db.String, nullable= False)
    

 
    def __init__(self,**kwargs):
        
        self.day = kwargs.get("day")
        self.breakfast = kwargs.get("breakfast")
        self.lunch=kwargs.get('lunch')
        self.dinner=kwargs.get("dinner")
 
 
    def serialize(self):
        return {
            "id": self.id,
            "day": self.day,
            "breakfast": self.breakfast,
            "lunch":self.lunch,
            "dinner":self.dinner
            
        }
 
    def simple_serialize(self):
        return {
            "id": self.id,
            "day": self.day
        }


"""
class Meal(db.Model):
    __tablename__="meal"
    id= db.Column(db.Integer, primary_key=True)
 #Breakfast Lunch or Dinner
    day = db.Column(db.String, nullable= False)
    bld=db.Column(db.String,nullable=False)
    recipe_id= db.Column(db.Integer)
 
 
    def __init__(self,**kwargs):
        
        self.day = kwargs.get("day")
        self.bld=kwargs.get('bld')
        self.recipe_id=kwargs.get("recipe_id")
 
 
    def serialize(self):
        return {
            "id": self.id,

            "day": self.day,
            "bld": self.bld,
            "recipe": Recipe.query.filter_by(id=self.recipe_id).first()
 
        }
 
    def simple_serialize(self):
        return {
            "id": self.id,
            "day": self.day
        }
    """

"""
class Ingredient(db.Model):
    __tablename__="ingredient"
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,nullable=False)
    
    recipe_id=db.Column(db.Integer,db.ForeignKey("recipe.id"))
    


    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.recipe_id=kwargs.get("recipe_id")
        

    def serialize(self):
        return {
        "id": self.id,
        "name":self.name
        }
"""
    




    

