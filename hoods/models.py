from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import datetime as dt

class Neighborhood(models.Model):
    name=models.CharField(max_length=40)
    location=models.CharField(max_length=40)
    occupants_count = models.PositiveIntegerField(default=0)
    health_contact = models.PositiveIntegerField()
    police_contact = models.PositiveIntegerField()
    hood_pic = models.ImageField(upload_to='images/')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()

    @classmethod
    def find_neigborhood(cls, hood_id):
        hood= cls.objects.get(id=hood_id)
        return hood

    @classmethod   
    def update_neighborhood(cls,id,name):
        cls.objects.filter(pk = id).update(name=name)
        new_name_object = cls.objects.get(name = name)
        new_name = new_name_object.name
        return new_name
    
    @classmethod   
    def update_occupants(cls,id,occupants):
        cls.objects.filter(pk = id).update(occupants=occupants)
        new_occupants_object = cls.objects.get(pk__id=id)
        new_occupants = new_name_object.occupants
        return new_occupants



    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profiles/',default='profiles/default.png')
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    bio= models.CharField(max_length=250)
    email=models.EmailField()
    location= models.CharField(max_length=250,default='add your general location')
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.first_name


class Business(models.Model):
    name=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='pictures/')
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    contacts=models.CharField(max_length=40, null=True)
    description=models.CharField(max_length=200,null=True)
    


    def __str__(self):
        return self.name

    @classmethod
    def search(cls,searchterm):
        search = Business.objects.filter(Q(name__icontains=searchterm)|Q(description__icontains=searchterm))
        return search

class Hospital(models.Model):
    name=models.CharField(max_length=100)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    contacts=models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.name

class Alert(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='posts',blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)


    def save_alert(self):
        self.save()

    def delete_alert(self):
        self.delete()
    
    @classmethod
    def get_single_alert(cls,id):
        return cls.objects.get(id=id)

    @classmethod   
    def update_alert(cls,id,content):
        cls.objects.filter(pk = id).update(title=content)
        new_name_object = cls.objects.get(pk=id)
        new_name = new_name_object.title
        return new_name

    def __str__(self):

        return self.title
    
    class Meta:
        ordering =['-date_posted']

