from django.test import TestCase
from .models import Profile, Project, Rate
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):
    '''
    Test class to test the behaviour of the Profile class
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
       
        # Creating a new user
        self.new_user = User(username = 'Doe', password = 'pass', email = 'johndoe@company.com')
        self.new_user.save()

        # Creating a new profile
        self.new_profile = Profile(id = 1, full_name = 'John Doe', bio = 'Test short bio', user = self.new_user)
        self.new_profile.save()

    def test_instance(self):
        '''
        Method to test if the new_profile object is an instance of the Profile model
        '''

        self.assertTrue(self.new_profile, Profile)

    def test_delete_method(self):
        '''
        Method to test the delete profile method
        '''
        Profile.delete_profile(self.new_profile.id)
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_get_profile_by_id(self):
        '''
        Method to test the get_profile_by_id method
        '''
        profile = Profile.get_profile_by_id(1)
        self.assertEqual(profile.full_name, 'John Doe')

class ProjectTestClass(TestCase):
    '''
    Test class to test the behaviour of the Project class
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
       
        # Creating a new user
        self.new_user = User(username = 'Doe', password = 'pass', email = 'johndoe@company.com')
        self.new_user.save()

        # Creating a new project
        self.new_project = Project(id = 1, title = 'My project title', description = 'Test description', live_link = 'http://127.0.0.1:8000/', user = self.new_user)
        self.new_project.save()

    def test_instance(self):
        '''
        Method to test if the new_project object is an instance of the Project model
        '''

        self.assertTrue(self.new_project, Project)

    def test_delete_project(self):
        '''
        Method to test the delete_project method
        '''
        Project.delete_project(self.new_project.id)
        project = Project.objects.all()
        self.assertTrue(len(project) == 0)

    def test_get_project_by_id(self):
        '''
        Method to test the get_project_by_id method
        '''
        project = Project.get_project_by_id(1)
        self.assertEqual(project.title, 'My project title')

class RateTestClass(TestCase):
    '''
    Test class to test the behaviour of the Rate class
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
       
        # Creating a new user
        self.new_user = User(username = 'Doe', password = 'pass', email = 'johndoe@company.com')
        self.new_user.save()

        # Creating a new project
        self.new_project = Project(id = 1, title = 'My project title', description = 'Test description', live_link = 'http://127.0.0.1:8000/', user = self.new_user)
        self.new_project.save()

        # Creating a new Rating
        self.new_rating = Rate(id = 1, design = 5, usability = 6, creativity = 7, project = self.new_project, user = self.new_user)
        self.new_rating.save()
    
    def test_instance(self):
        '''
        Method to test if the new_rating object is an instance of the Rate model
        '''

        self.assertTrue(self.new_rating, Rate)

    def test_delete_rate(self):
        '''
        Method to test the delete_rate method
        '''
        Rate.delete_rate(self.new_rating.id)
        ratings = Rate.objects.all()
        self.assertTrue(len(ratings) == 0)

    def test_get_rate_by_id(self):
        '''
        Method to test the get_rate_by_id method
        '''
        rating = Rate.get_rate_by_id(1)
        self.assertEqual(rating.usability, 6)