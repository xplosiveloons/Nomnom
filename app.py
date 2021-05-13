from db import db
from db import Recipe, Restriction, Plan
from flask import request
from flask import Flask
import json
import os

app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

def success_response(data, code=200):
    return json.dumps({"success":True, "data":data}),code
def failure_response(error, code=404):
    return json.dumps({"success":False, "error":error}),code 

@app.route("/") 

@app.route("/api/recipes/")
def get_all_recipes():
    return success_response([r.simple_serialize() for r in Recipe.query.all()]) 

@app.route("/api/recipes/favorited/")
def get_all_favorited_recipes():
    return success_response([r.simple_serialize() for r in Recipe.query.filter_by(favorited=True)])

 

@app.route("/api/recipes/", methods=["POST"])
def create_recipe():
    body=json.loads(request.data)
    title=body.get("title")
    if title is None:
        return failure_response("Title not found")
    description=body.get("description")
    if description is None:
        return failure_response("Description not found")
    ingredients=body.get("ingredients")
    if ingredients is None:
        return failure_response("Ingredients not found")
    new_recipe=Recipe(title=title, description=description, ingredients=ingredients)
    db.session.add(new_recipe)
    db.session.commit()
    return success_response(new_recipe.serialize(),201)

@app.route("/api/recipes/<int:recipe_id>/")
def get_recipe(recipe_id):
    recipe=Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        return failure_response("Recipe not found")
    return success_response(recipe.simple_serialize())


@app.route("/api/recipes/<int:recipe_id>/", methods =["DELETE"])
def delete_recipe(recipe_id):
    recipe=Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        return failure_response("Recipe not found")
    db.session.delete(recipe)
    db.session.commit()
    return success_response(recipe.serialize())

@app.route("/api/recipes/<int:recipe_id>/update_title/", methods=["POST"])
def update_recipe_title(recipe_id):
    recipe=Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        return failure_response("Recipe not found")
    body=json.loads(request.data)
    recipe.title=body.get("title",recipe.title)
    db.session.commit()
    return success_response(recipe.serialize())

@app.route("/api/recipes/<int:recipe_id>/update_description/", methods=["POST"])
def update_recipe_description(recipe_id):
    recipe=Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        return failure_response("Recipe not found")
    body=json.loads(request.data)
    recipe.description=body.get("description",recipe.description)
    db.session.commit()
    return success_response(recipe.serialize())

@app.route("/api/recipes/<int:recipe_id>/update_ingredients/", methods=["POST"])
def update_recipe_ingredients(recipe_id):
    recipe=Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        return failure_response("Recipe not found")
    body=json.loads(request.data)
    recipe.ingredients=body.get("ingredients",recipe.ingredients)
    db.session.commit()
    return success_response(recipe.serialize())

@app.route("/api/recipes/<int:recipe_id>/favorite/", methods=["GET"])
def change_favorite_status(recipe_id):
    recipe=Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        return failure_response("Recipe not found")
    recipe.favorited= not recipe.favorited
    db.session.commit()
    return success_response(recipe.serialize())


@app.route("/api/restrictions/", methods=["POST"])
def create_restriction():
    body=json.loads(request.data)
    title=body.get("title")
    if title is None:
        return failure_response("Title not found")
    description=body.get("description")
    if description is None:
        return failure_response("Description not found")
    
    new_restriction=Restriction(title=title,description=description)
    db.session.add(new_restriction)
    db.session.commit()
    return success_response(new_restriction.serialize(),201)


@app.route("/api/restrictions/<int:restriction_id>/")
def get_restriction(restriction_id):
    restriction=Restriction.query.filter_by(id=restriction_id).first()
    if restriction is None:
        return failure_response("Restriction not found")
    return success_response(restriction.serialize())

@app.route("/api/recipes/<int:recipe_id>/add_restriction/",methods=["POST"])
def assign_restriction(recipe_id):
    body=json.loads(request.data)
    recipe=Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        return failure_response("Recipe not found")
    restriction_id=body.get("restriction_id")
    if restriction_id is None:
        return failure_response("No Restriction ID")
    restriction=Restriction.query.filter_by(id=restriction_id).first()
    if restriction is None:
        return failure_response("No Restriction")
    recipe.restrictions.append(restriction)
    db.session.commit()
    return success_response(recipe.serialize())


@app.route("/api/plans/",methods=["POST"])
def create_plan():
    body=json.loads(request.data)
    breakfast=body.get("breakfast")
    if breakfast is None:
        return failure_response("Breakfast not found")
    day=body.get("day")
    if day is None:
        return failure_response("Day not found")
    lunch=body.get("lunch")
    if lunch is None:
        return failure_response("Lunch not found")
    dinner=body.get("dinner")
    if dinner is None:
        return failure_response("Dinner not found")
    new_plan=Plan(breakfast=breakfast, day=day, lunch=lunch, dinner=dinner)
    db.session.add(new_plan)
    db.session.commit()
    return success_response(new_plan.serialize(),201)

@app.route("/api/plans/",methods=["GET"])
def get_all_plans():
    return success_response([p.simple_serialize() for p in Plan.query.all()])


@app.route("/api/plans/<int:plan_id>/", methods =["DELETE"])
def delete_plan(plan_id):
    plan=Plan.query.filter_by(id=plan_id).first()
    if plan is None:
        return failure_response("Plan not found")
    db.session.delete(plan)
    db.session.commit()
    return success_response(plan.serialize())

@app.route("/api/plans/<int:plan_id>/")
def get_plan(plan_id):
    plan=Plan.query.filter_by(id=plan_id).first()
    if plan is None:
        return failure_response("Plan not found")
    return success_response(plan.serialize())






 






"""
@app.route("/api/recipes/<int:recipe_id>/ingredient/", methods=["POST"])
def create_ingredient(recipe_id):
    recipe_id=recipe_id
    if recipe_id is None:
        return failure_response("No recipe id found")
    recipe=Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        return failure_response("Recipe not found")
    body=json.loads(request.data)
    name = body.get("name")
    if name is None:
        return failure_response("No name")
    
    new_ingredient=Ingredient(name=name,recipe_id=recipe)
    db.session.add(new_ingredient)
    db.session.commit()
    return success_response(new_ingredient.serialize(),201)

@app.route("/api/recipes/<int:recipe_id>/ingredient/", methods=["POST"])
def add_ingredients(recipe_id):
    recipe_id=recipe_id
    if recipe_id is None:
        return failure_response("No recipe id found")
    recipe=Recipe.query.filter_by(id=recipe_id).first()
    if recipe is None:
        return failure_response("Recipe not found")
"""





# your routes here


if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    app.run(host="0.0.0.0", port=port)
