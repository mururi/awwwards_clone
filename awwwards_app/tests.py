from django.test import TestCase
from .models import Profile
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
        Profile.delete_profile(self.new_profile.id)
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_get_profile_by_id(self):
        profile = Profile.get_profile_by_id(1)
        self.assertEqual(profile.full_name, 'John Doe')