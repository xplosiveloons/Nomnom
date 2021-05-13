
Get All Recipes
#GET /api/recipes/

Response
{
    "success": true,
    "data": [ 
        {
            "id": 1,
            "title": "Mac and Cheese"
            "description": "Pasta with Cheese",
            "favorited": True,
            "ingredients": "Pasta, Cheese",
            "restrictions": [<SERIALIZED RESTRICTION WITHOUT RECIPES>,...]

        },
        {
            "id": 2,
            "title": "PB n J"
            "description": "Peanut Butter and Jelly Sandwich",
            "favorited": False,
            "ingredients": "bread, peanut butter, jelly",
            "restrictions": [<SERIALIZED RESTRICTION WITHOUT RECIPES>,...]

        }
    
    ]
}

Get All Favorited Recipes

#GET /api/recipes/favorited/
 
Response
{
    "success": true,
    "data": [ 
        {
            "id": 1,
            "title": "Mac and Cheese"
            "description": "Pasta with Cheese",
            "favorited": True,
            "ingredients": "Pasta, Cheese",
            "restrictions": [<SERIALIZED RESTRICTION WITHOUT RECIPES>,...]

        },
        {
            "id": 3,
            "title": "Calzones"
            "description": "Bread and Cheese",
            "favorited": True,
            "ingredients": "Bread, Cheese, Sause, Pepper",
            "restrictions": [<SERIALIZED RESTRICTION WITHOUT RECIPES>,...]
    
    ]
}

Create Recipe

#POST  /api/recipes/
Request

{ 
    "title": <USER STRING INPUT>,
    "description": <USER STRING INPUT>,
    "ingredients": <USER STRING INPUT>

}

Response

{
    "success": true,
    "data": [ 
        {
            "id": 1,
            "title": "Mac and Cheese"
            "description": "Pasta with Cheese",
            "favorited": True,
            "ingredients": "Pasta, Cheese",
            "restrictions": [<SERIALIZED RESTRICTION WITHOUT RECIPES>,...]
        }
    ]
}



Get Recipe 
#GET /api/recipes/{id}/
Response
{
    "success": true,
    "data": {
            "id": <ID>,
            "title": <USER INPUT FOR TITLE>,
            "description": <USER INPUT FOR DESCRIPTION>,
            "favorited": <USER INPUT FOR FAVORITED>,
            "ingredients": <USER INPUT FOR INGREDIENTS>,
            "restrictions": [<SERIALIZED RESTRICTION WITHOUT RECIPES>,...]
    }
    
}

Delete Recipe
# dELETE /api/recipes/{id}/

Response
{
    "success": true,
    "data": {
            "id": <ID>,
            "title": <USER INPUT FOR TITLE>,
            "description": <USER INPUT FOR DESCRIPTION>,
            "favorited": <USER INPUT FOR FAVORITED>,
            "ingredients": <USER INPUT FOR INGREDIENTS>,
            "restrictions": [<SERIALIZED RESTRICTION WITHOUT RECIPES>,...]
    }
    
}

Update Recipe Title
#POST /api/recipes/{id}/update_title/

Request

{ 
    "title": <USER STRING INPUT>
    

}

Response

{
    "success": true,
    "data": [ 
        {
            "id": 1,
            "title": "Mac and Cheese"
            "description": "Pasta with Cheese",
            "favorited": True,
            "ingredients": "Pasta, Cheese",
            "restrictions": [<SERIALIZED RESTRICTION WITHOUT RECIPES>,...]
        }
    ]
}

Update Recipe Description
#POST /api/recipes/{id}/update_description/

Request

{ 
    "description": <USER STRING INPUT>
    

}

Response

{
    "success": true,
    "data": [ 
        {
            "id": 1,
            "title": "Mac and Cheese"
            "description": "Pasta with Cheese",
            "favorited": True,
            "ingredients": "Pasta, Cheese",
            "restrictions": [<SERIALIZED RESTRICTION WITHOUT RECIPES>,...]
        }
    ]
}


Update Recipe Ingredients
#POST /api/recipes/{id}/update_ingredients/

Request

{ 
    "ingredients": <USER STRING INPUT>
    

}

Response

{
    "success": true,
    "data": [ 
        {
            "id": 1,
            "title": "Mac and Cheese"
            "description": "Pasta with Cheese",
            "favorited": True,
            "ingredients": "Pasta, Cheese",
            "restrictions": [<SERIALIZED RESTRICTION WITHOUT RECIPES>,...]
        }
    ]
}

Change Recipe Favorited Status
#GET /api/recipes/{id}/favorite/


Response
{
    "success": true,
    "data": {
            "id": <ID>,
            "title": <USER INPUT FOR TITLE>,
            "description": <USER INPUT FOR DESCRIPTION>,
            "favorited": <USER INPUT FOR FAVORITED>,
            "ingredients": <USER INPUT FOR INGREDIENTS>,
            "restrictions": [<SERIALIZED RESTRICTION WITHOUT RECIPES>,...]
    }
    
}

Create Restriction
#POST /api/restrictions/

Request

{
    
    "title": <USER STRING INPUT>,
    "description": <USER STRING INPUT>
}


Response
{
    "success": true,
    "data": {
            "id": <ID>,
            "title": <USER INPUT FOR TITLE>,
            "description": <USER INPUT FOR DESCRIPTION>,
            "recipes": []
    }
}


Assign Restriction

#POST /api/recipes/<int:recipe_id>/add/
Request
{
    "restriction_id": <USER INPUT>
}
Response

Response
{
    "success": true,
    "data": {
            "id": <ID>,
            "title": <USER INPUT FOR TITLE>,
            "description": <USER INPUT FOR DESCRIPTION>,
            "recipes": [SERIALIZED RECIPE]
    }
}


Create Plan
#POST /api/plans/
Request
{ 
    
    "day": <USER STRING INPUT>,
    "breakfast": <USER STRING INPUT>,
    "lunch": <USER STRING INPUT>,
    "dinner": <USER STRING INPUT>

}

Response

{
    "success": true,
    "data": [ 
        {
            "id": 1,
            "day": "Monday"
            "breakfast": <USER STRING INPUT>,
            "lunch": <USER STRING INPUT>,
            "dinner": <USER STRING INPUT>
        }
    ]
}

Get All Plans
#POST /api/plans/

Response

{
    "success": true,
    "data": [ 
        {
            "id": 1,
            "day": "Monday",
            "breakfast": "Cereal",
            "lunch": "Mac and Cheese",
            "dinner":"Pasta"

        },
        {
            "id": 2,
            "day": "Tuesday",
            "breakfast": "Cereal",
            "lunch": "PB and J",
            "dinner":"Chicken and Rice"

        }
    
    ]
}

Delete Plan

#dELETE /api/plans/<int:plan_id>/

Response

{
    "success": true,
    "data": [ 
        {
            "id": 1,
            "day": "Monday"
            "breakfast": <USER STRING INPUT>,
            "lunch": <USER STRING INPUT>,
            "dinner": <USER STRING INPUT>
        }
    ]
}


Get Plan

#GET /api/plans/<int:plan_id>/

Response

{
    "success": true,
    "data": [ 
        {
            "id": 1,
            "day": "Monday"
            "breakfast": <USER STRING INPUT>,
            "lunch": <USER STRING INPUT>,
            "dinner": <USER STRING INPUT>
        }
    ]
}









