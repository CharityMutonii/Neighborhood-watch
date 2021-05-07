from django.test import TestCase
from .models import *



class ProfileTestClass(TestCase):
    #Set up method

    def setUp(self):
        
        self.new_profile = Profile(user_id=2,hood_id=3,bio="testing", email='claire@gmail.com',name="claire",profile_pic="image.jpeg")
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    
    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def tearDown(self):
        Profile.objects.all().delete()

class AlertTestClass(TestCase):

    def setUp(self):
        
        self.new_user = User(username='claire', email='claire@gmail.com', password='weocode20')
        self.new_user.save()
        self.new_hood = Neighborhood(name="gacuriro", location="nyarutarama", occupants="10",health_contact="110", police_contact="300", hood_pic="cl.png", admin=self.new_user)
        self.new_hood.save()
        self.new_alert=alert(title="wedding",content="my  wedding",image='image.png',user=self.new_user, hood=self.new_hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_alert,alert))    

    def test_save_alert(self):
        self.new_alert.save_alert()
        alert = alert.objects.all()
        self.assertTrue(len(alert)>0)

    def test_delete_alert(self):
        self.new_alert.save_alert()
        self.new_alert.delete_alert()
        alert = alert.objects.all()
        self.assertTrue(len(alert)==0)

    def tearDown(self):
        alert.objects.all().delete()

class BuninessTestClass(TestCase):

    def setUp(self):
        
        
        self.new_business=Business(bName="car rentals",user_id=4, hood_id=2, bEmail="titusouko@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))    

    def test_save_business(self):
        self.new_business.create_business()
        business = Business.objects.all()
        self.assertTrue(len(business)>0)

   

    def test_delete_method(self):
        self.new_business.create_business()
        self.new_business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) is 0)

    def test_update_bussiness_method(self):
        self.new_business.create_business()
        new_name = 'travel agency' 
        update = self.new_business.update_business(self.new_business.id,new_name)
        self.assertEqual(update,new_name)
        
    def test_find_method(self):
        self.new_business.create_business()
        bussiness = self.new_business.find_business(self.new_business.id)
        self.assertEquals(bussiness.bName,'techs')

    def tearDown(self):
        Business.objects.all().delete()

class NeighborhoodTestClass(TestCase):

    def setUp(self):
        
        self.new_user = User(username='claire', email='claire@gmail.com', password='wecode20')
        self.new_user.save()
        self.new_hood = Neighborhood(name="gacuriro", location="nyarutarama", occupants="10",health_contact="123", police_contact="110", hood_pic="cl.png", admin=self.new_user)
       
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood,Neighborhood))    

    def test_delete_neighborhood(self):
        self.new_hood.create_neigborhood()
        self.new_hood.delete_neigborhood()
        hood = Neighborhood.objects.all()
        self.assertTrue(len(hood)==0)

    def test_update_neigborhood_method(self):
        self.new_hood.create_neigborhood()
        new_name = 'gacuriro' 
        update = self.new_hood.update_neighborhood(self.new_hood.id,new_name)
        self.assertEqual(update,new_name)

    def tearDown(self):
        Neighborhood.objects.all().delete() 