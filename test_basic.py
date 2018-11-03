import os
import json
from flask import Flask, render_template, redirect, request, url_for, session
import unittest
from flask_testing import TestCase
from app import app
import random


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
        app.app_context().push()
        app.config['SERVER_NAME'] 
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.client = app.test_client()
        print("set up")
        
        
    # executed after each test
    def tearDown(self):
        print("tear down")
        pass
 
    ###############
    #### tests ####
    ###############
    """
    # Ensure the index page can be reached
    def test_index(self):
        response = app.test_client(self).get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The Chefs Desire", response.data)
        print("index found")"""
    """    
    # Ensure the single_reciepe page can be reached
    def test_single_recipe(self):
        response = app.test_client(self).get('/single_recipe/5bd1616413092517e8e05062', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("single recipe found")"""
    
    """
    # Ensure the add_recipe page can be reached
    def test_add_recipe(self):
        response = app.test_client(self).get('/add_recipe', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("add recipe found//", "response location =", response.location) 
        """
    """
    # Ensure the insert_recipe page can be reached
    def test_insert_recipe(self):
        data=dict(
            name= "recipe",
        cuisine="british",
        allergens="wheat",
        description="test",
        ingredients="apple",
        instructions="test",
        prep_time="test",
        cook_time="test",
        recipe_yield="test",
        author="test",
        image="test",
        user="test"
            )
        response = app.test_client(self).post('/insert_recipe', content_type='multipart/form-data', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print(response.location)
        print("insert recipe found//", "response location =", response.location) """
        
    """    
    # Ensure the edit_recipe page can be reached
    def test_edit_recipe(self):
        response = app.test_client(self).get('/edit_recipe/5bd1616413092517e8e05062', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("edit recipe found") """
        
    """
    # Ensure the edit_recipe page can be reached
    def test_update_recipe(self):
        response = app.test_client(self).post('/update_recipe/5bd1616413092517e8e05062', follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        print("update recipe found")"""
    
    
    """
    # Ensure the registration page can be reached and that it sends the correct data. For the purpose of 
    this test change the register_username to something that can also be used to test the login.
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
        print("register found//", "response location =", response.location) 
        """
    """
    # Ensure the sign in page can be reached and that it sends the correct data.
    def test_login(self):
        data=dict(
        signin_username="m496",
        signin_password="testpassword"
        )
        response = app.test_client(self).post('/signin', content_type='multipart/form-data', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello testuserfirstname", response.data)
        self.assertNotIn(b"Hello admin", response.data)
        print(dir(response))
        print(response.status)"""
    """ 
    # Ensure the user hasn't been signed in with an incorrect password. 
    def test_login_wrong_password(self):
        data=dict(
        signin_username="m496",
        signin_password="wrongpassword"
        )
        response = app.test_client(self).post('/signin', content_type='multipart/form-data', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Hello testuserfirstname", response.data)
        print(response.location)"""
        
    """   
    # Ensure the recipes page can be reached.
    def test_recipes(self):
        response = app.test_client(self).get('/recipes', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("recipes found")"""
    """   
    # Ensure the most popular recipes page can be reached.
    def test_most_popular_recipes(self):
        response = app.test_client(self).get('/most_popular_recipes', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("most popular recipes found")"""
    """    
    # Ensure the most viewed recipes page can be reached.    
    def test_most_viewed_recipes(self):
        response = app.test_client(self).get('/most_viewed_recipes', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("most viewed recipes found")"""
    """    
    # Ensure the most all recipes page can be reached.
    def test_all_recipes(self):
        response = app.test_client(self).get('/all_recipes', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("all recipes found") """
        
    """
    # Ensure find ingredients can be reached and that it searches for the correct criteria.
    def test_find_ingredient(self):
        data=dict(
        ingredient_category="mushroom"
        )   
        response = app.test_client(self).post('/find_ingredient', content_type='multipart/form-data', data=data, follow_redirects=False)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Yaki Udon",response.data)
        self.assertNotIn(b"Dal fry",response.data)
        print("find ingredient found")"""
        
    """
    # Ensure find cuisine can be reached and that it searches for the correct criteria.
    def test_find_cuisine(self):
        data=dict(
        cuisine_category="american"
        )  
        response = app.test_client(self).post('/find_cuisine', content_type='multipart/form-data', data=data, follow_redirects=False)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Pumpkin Pie",response.data)
        self.assertNotIn(b"Rock Cakes",response.data)
        print("find cuisine found") """
    
    """
    # Ensure find allergens can be reached and that it searches for the correct criteria.
    def test_find_allergen(self):
        data=dict(
        allergen_category="wheat"
        ) 
        response = app.test_client(self).post('/find_allergen', content_type='multipart/form-data', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Eton Mess",response.data)
        self.assertNotIn(b"Pancakes",response.data)
        print("find allergen found") """
        
        
    """
    # Ensure find multiple categories can be reached and that it searches for the correct criteria.
    def test_find_multiple_categories(self):
        data=dict(
        find_cuisine="british",
        find_ingredient="flour",
        find_allergen="eggs"
        ) 
        response = app.test_client(self).post('/find_multiple_categories', content_type='multipart/form-data', data=data, follow_redirects=False)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Fish pie",response.data)
        self.assertNotIn(b"Carrot Cake",response.data)
        print("find multiple categories found")"""
    """    
    # Ensure update view count can be reached.
    def test_update_view_count(self):
        response = app.test_client(self).get('/update_view_count/5bd1616413092517e8e05062', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("update view found")"""
    """    
    # Ensure update like count can be reached.
    def test_update_like(self):
        response = app.test_client(self).get('/update_like/5bd1616413092517e8e05062', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("update like found") """
 
if __name__ == "__main__":
    
    unittest.main()
    