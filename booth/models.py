from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_editor(self):
        self.save()

class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location


class Image(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    post_date = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.name

    def save_photo(self):
        self.save()

    def update_image(self):
        self.update()

    @classmethod
    def get_image_by_id(cls,self):
        image_id = self.id
        this_pic = cls.objects.filter(id = image_id)
        return this_pic

    @classmethod
    def search_image(cls, parameter):
        img = cls.objects.filter(category__category__icontains=parameter)
        return img

    @classmethod
    def filter_by_location(cls, location):
        this_pic = cls.objects.filter(location__location__icontains=location)
        return this_pic


