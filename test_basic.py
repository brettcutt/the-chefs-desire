import os
import json
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import unittest
from app import app

class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app = Flask(__name__)
        
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        
        print("set up")
        
        
    # executed after each test
    def tearDown(self):
        print("tear down")
        pass
 
    ###############
    #### tests ####
    ###############
 
    def test_index(self):
        response = app.test_client(self).get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("index found")
        
    def test_single_recipe(self):
        response = app.test_client(self).get('/single_recipe/5bd1616413092517e8e05062', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("single recipe found")
    
    
    def test_valid_user_registration(self):
        data = {
        "username":"admin"        
        }
        
        response = app.test_client(self).post('/register', data=dict(data))
        self.assertEqual(response.status_code, 302)
        self.assertIn(b'admin', response.data)
        
 
 
 
if __name__ == "__main__":
    
    unittest.main()
    