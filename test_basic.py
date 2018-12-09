import os
import json
from flask import Flask, render_template, redirect, request, url_for, session
import unittest
from flask_testing import TestCase
from app import app
import random
from bson.objectid import ObjectId


class finding_views(unittest.TestCase):
    """ This is a routing test to find the various paths to the site pages"""
    
    """ NOTE CREDIT IS DUE to my mentor Moosa Hassan for the following lines of helping code:
        content_type='multipart/form-data'
        data=dict( "list" )
        register_username='m' + str(random.randint(1,1000))
        print(dir(response))
        """
    
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app = Flask(__name__)
        app.config['SERVER_NAME'] 
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SECRET_KEY'] = 'secret'
        self.client = app.test_client()
        
        
        
        
    # executed after each test
    def tearDown(self):
        
        pass
 
    ###############
    #### tests ####
    ###############
    
    #Ensure the index page can be reached
    def test_index_page(self):
        response = app.test_client(self).get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The Chefs Desire", response.data)
       
    # Ensure the single_reciepe page can be reached
    def test_get_single_recipe_page(self):
        response = app.test_client(self).get('/single_recipe/5bd1642913092517e8e05064', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    
    # Ensure the add_recipe page can be reached
    def test_get_add_recipe_page(self):
        response = app.test_client(self).get('/add_recipe', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
     
    # Ensure the a recipe can be created
    """
    def test_insert_recipe(self):
        data=dict(
            name= "the insert test recipe name",
        cuisine="british",
        allergens="wheat",
        description="test",
        ingredients="apple",
        instructions="This is the description for the test recipe",
        prep_time="test",
        cook_time="test",
        recipe_yield="test",
        author="test",
        image="test",
        user="test"
            )
        with app.test_client(self) as client:
            with client.session_transaction() as session:
                session['user'] = 'test'
            response = client.post('/insert_recipe', content_type='multipart/form-data', data=data)
            print(dir(response))
            print(response.data)
            print(response.location)
            
            print(response.headers)
            self.assertEqual(response.status_code, 302)
            self.assertIn('http://localhost/single_recipe/', response.location)
            """
        
    
    # Ensure the edit_recipe page can be reached
    def tes_get_edit_recipe_page(self):
        response = app.test_client(self).get('/edit_recipe/5bd1616413092517e8e05062', follow_redirects=True)
        self.assertEqual(response.status_code, 200) 
        
    
    # Ensure a recipe can be edited and be redirect to that recipes single recipe page.
    def test_update_a_recipe(self):
        data=dict(
            name= "edited recipe",
        cuisine="Italian",
        allergens="eggs",
        description="edited test",
        ingredients="pear",
        instructions="edited test",
        prep_time="20 min",
        cook_time="10 min",
        recipe_yield="4",
        author="edited test author",
        image="https://www.themealdb.com/images/media/meals/rwuyqx1511383174.jpg",
        user="edited test user"
            )
        with app.test_client(self) as client:
            with client.session_transaction() as session:
                session['user'] = 'admin'
                
            response = client.post('/update_recipe/5c0cbfde13092515c9ecf1fa', content_type='multipart/form-data', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertIn('single_recipe/5c0cbfde13092515c9ecf1fa', response.location)
    
    
    """ # PASSES BUT DON'T WANT TO CREATE A USER EACH TIME IF IT'S NOT NECESSARY 
    # Ensure the registration page can be reached and that it sends the correct data. For the purpose of 
    # this test change the register_username to something that can also be used to test the login.
    def test_registration(self):
        data=dict(
        register_first_name="testuserfirstname",
        register_last_name="testuserlastname",
        register_username='m' + str(random.randint(1,1000)),
        register_email="email@email.com",
        register_password="testpassword",
        comfirm_password="testpassword"
        )
        response = app.test_client(self).post('/register', content_type='multipart/form-data', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello testuserfirstname", response.data)
        """
        
    
    # Ensure the sign in page can be reached and that it sends the correct data.
    def test_log_a_user_in(self):
        data=dict(
        signin_username="m155",
        signin_password="testpassword"
        )
        response = app.test_client(self).post('/signin', content_type='multipart/form-data', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello testuserfirstname", response.data)
        self.assertNotIn(b"Hello admin", response.data)
        
    
    # Ensure the user hasn't been signed in with an incorrect password. 
    def test_login__with_wrong_password(self):
        data=dict(
        signin_username="m496",
        signin_password="wrongpassword"
        )
        response = app.test_client(self).post('/signin', content_type='multipart/form-data', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Hello testuserfirstname", response.data)
        
      
    # Ensure the recipes page can be reached.
    def test_get_recipes_page(self):
        response = app.test_client(self).get('/recipes', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    # Ensure the most popular recipes page can be reached.
    def test_get_most_popular_recipes_page(self):
        response = app.test_client(self).get('/most_popular_recipes', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    # Ensure the most viewed recipes page can be reached.    
    def test_get_new_recipes_page(self):
        response = app.test_client(self).get('/new_recipes', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    
    # Ensure the most all recipes page can be reached.
    def test_get_all_recipes_page(self):
        response = app.test_client(self).get('/all_recipes', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    
    # Ensure find ingredients can be reached and that it searches for the correct criteria.
    def test_get_find_ingredient_page(self):
        data=dict(
        ingredient_category="mushroom"
        )   
        response = app.test_client(self).post('/find_ingredient', content_type='multipart/form-data', data=data, follow_redirects=False)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Yaki Udon",response.data)
        self.assertNotIn(b"Dal fry",response.data)
        
    
    # Ensure find cuisine can be reached and that it searches for the correct criteria.
    def test_get_find_cuisine_page(self):
        data=dict(
        cuisine_category="american"
        )  
        response = app.test_client(self).post('/find_cuisine', content_type='multipart/form-data', data=data, follow_redirects=False)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Pumpkin Pie",response.data)
        self.assertNotIn(b"Rock Cakes",response.data)
    
    
    # Ensure find allergens can be reached and that it searches for the correct criteria.
    def test_get_find_allergen_page(self):
        data=dict(
        allergen_category="wheat"
        ) 
        response = app.test_client(self).post('/find_allergen', content_type='multipart/form-data', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Eton Mess",response.data)
        self.assertNotIn(b"Pancakes",response.data)

    
    # Ensure find multiple categories can be reached and that it searches for the correct criteria.
    def test_get_find_multiple_categories_page(self):
        data=dict(
        find_cuisine="british",
        find_ingredient="flour",
        find_allergen="eggs"
        ) 
        response = app.test_client(self).post('/find_multiple_categories', content_type='multipart/form-data', data=data, follow_redirects=False)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Fish pie",response.data)
        self.assertNotIn(b"Carrot Cake",response.data)
        
    
    # Ensure update view count can be reached.
    def test_update_view_count(self):
        response = app.test_client(self).get('/update_view_count/5c0cbfde13092515c9ecf1fa')
        self.assertEqual(response.status_code, 302)
    
    # Ensure update like count can be reached.
    def test_update_like(self):
        response = app.test_client(self).get('/update_like/5c0cbfde13092515c9ecf1fa')
        self.assertEqual(response.status_code, 302)
 
if __name__ == "__main__":
    
    unittest.main()
    