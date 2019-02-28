from django.test import TestCase
from .models import Category, Location, Image
import datetime as dt


# Create your tests here.
class ImageTest(TestCase):
    def setUp(self):
        #newcategory
        self.cat = Category(name='education')
        self.cat.save()

        #newlocation
        self.loc = Location(name='Nairobi')
        self.loc.save()

        #newdate
        test_date = '2019-01-10'
        self.date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()

        #newimage
        self.img = Image(name='Awesome.jpg', category=self.cat, location=self.loc, post_date=self.date)

    def test_instance(self):
        self.assertTrue(isinstance(self.img, Image))

    def test_save_method(self):
        self.img.save_photo()
        photos = Image.objects.all()
        self.assertTrue(len(photos) > 0)

    def test_delete_image(self):
        self.img.save_photo()
        less = Image.objects.all().delete()
        self.assertTrue(len(less) == 0)

    def test_update_image(self):
        self.img.save_photo()
        photos = Image.objects.all().update()
        self.assertTrue(len(photos) > 0)

    def test_get_image_by_id(self, id):
        this_image = Image.objects.filter(id)
        self.assertTrue(len(this_image) > 0)

    def test_search_image(self, category):
        self.img.save_photo()

    def test_filter_by_location(self, location):
        self.img.save_photo()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()



