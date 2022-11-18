from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from map.models import GroceryStoreAddresses, FarmersMarketAddresses, FireHouseAddresses
import geocoder
import time


# Create your tests here.

class FarmerMarketAddressProcessingTestCase(TestCase):
    def setUp(self):
        self.access_token = 'pk.eyJ1IjoiaGFtc2llIiwiYSI6ImNsODN4aWdmcjBhNHEzcGw4ZXYxMHcxaXkifQ.67o9saEURWg3rF02gZxGKg'
        self.address_model = FarmersMarketAddresses(farmer_address="535 MARCY AVE")
        self.invalid_address_model = FarmersMarketAddresses(farmer_address="!@#@!#@!$!!$@$@$@$@")


    def test_address_processing_success(self):
        g = geocoder.mapbox(self.address_model.farmer_address, key=self.access_token)
        latlong = g.latlng
        self.assertEqual(g.status_code, 200)
        self.assertEqual(latlong[0], 40.69699)
        self.assertEqual(latlong[1], -73.94938)

    def test_address_processing_failure(self):
        g = geocoder.mapbox(self.address_model.farmer_address, key=self.access_token)
        latlong = g.latlng
        self.assertEqual(g.status_code, 200)
        self.assertNotEqual(latlong[0], 23)
        self.assertNotEqual(latlong[1], -6)

    def test_address_processing_invalid_address(self):
        g = geocoder.mapbox(self.invalid_address_model.farmer_address, key=self.access_token)
        self.assertEqual(g.status_code,404)

class GroceryStoreTestCase(TestCase):
    def setUp(self):
        GroceryStoreAddresses.objects.create(lat="40", long="-73")

    def test_grocery_store_saved(self):
        grocery_store = GroceryStoreAddresses.objects.get(lat__exact="40")
        self.assertEqual(grocery_store.long, -73.0)

class FireHouseAddressTestCase(TestCase):
    def setUp(self):
        FireHouseAddresses.objects.create(lat="39", long="-34")

    def test_firehouse_saved(self):
        firehouse = FireHouseAddresses.objects.get(lat__exact="39")
        self.assertEqual(firehouse.long, -34)

class MapViewTestCase(TestCase):

    def test_map_template(self):
        response = self.client.get('/map/')
        self.assertEqual(response.templates[0].name, 'map.html')

    def test_map_response(self):
        response = self.client.get('/map/')
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        response = self.client.get('/map/')
        self.assertEqual(response.context['access_token'],
                         'pk.eyJ1IjoiaGFtc2llIiwiYSI6ImNsODN4aWdmcjBhNHEzcGw4ZXYxMHcxaXkifQ.67o9saEURWg3rF02gZxGKg')
        self.assertIsNotNone(response.context['addresses'])
        self.assertIsNotNone(response.context['farmer_addresses'])

class MapViewHTMLTestCase(LiveServerTestCase):
    def setUp(self):
        self.chromeOptions = webdriver.ChromeOptions()
        self.chromeOptions.add_argument("--disable-dev-shm-using")
        self.chromeOptions.add_argument("--remote-debugging-port=8000")

    def test_grocery_store_markers(self):
        selenium = webdriver.Chrome(chrome_options = self.chromeOptions)
        selenium.get('http://127.0.0.1:8000/map/')
        time.sleep(1)
        selenium.find_element(By.ID, 'button1').click()
        self.assertIsNotNone(selenium.find_element(By.CLASS_NAME, "mapboxgl-marker"))

    def test_farmer_market_markers(self):
        selenium = webdriver.Chrome(chrome_options = self.chromeOptions)
        selenium.get('http://127.0.0.1:8000/map/')
        time.sleep(1)
        selenium.find_element(By.ID, 'button2').click()
        self.assertIsNotNone(selenium.find_element(By.CLASS_NAME, "mapboxgl-marker"))

    def test_fire_station_markers(self):
        selenium = webdriver.Chrome(chrome_options = self.chromeOptions)
        selenium.get('http://127.0.0.1:8000/map/')
        time.sleep(1)
        selenium.find_element(By.ID, 'button3').click()
        self.assertIsNotNone(selenium.find_element(By.CLASS_NAME, "mapboxgl-marker"))

    def test_find_closest_business(self):
        selenium = webdriver.Chrome(chrome_options = self.chromeOptions)
        selenium.get('http://127.0.0.1:8000/map/')
        selenium.find_element(By.ID, 'button1').click()
        selenium.find_element(By.CLASS_NAME, 'mapboxgl-ctrl-geolocate').click()
        selenium.find_element(By.ID, 'find_nearest_business_button').click()
        time.sleep(1)
        self.assertIsNotNone(selenium.find_element(By.CLASS_NAME, "mapbox-directions-instructions"))

    def test_find_closest_business_with_no_markers_on_map(self):
        selenium = webdriver.Chrome(chrome_options = self.chromeOptions)
        selenium.get('http://127.0.0.1:8000/map/')
        selenium.find_element(By.CLASS_NAME, 'mapboxgl-ctrl-geolocate').click()
        selenium.find_element(By.ID, 'find_nearest_business_button').click()
        time.sleep(1)
        self.assertRaises(NoSuchElementException, selenium.find_element, By.ID, "mapbox-directions-instructions")


class HomePageViewTestCase(TestCase):
    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertEqual(response.templates[0].name, 'home.html')

    def test_homepage_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class AboutPageViewTestCase(TestCase):
    def test_aboutpage_template(self):
        response = self.client.get('/aboutme/')
        self.assertEqual(response.templates[0].name, 'aboutme.html')

    def test_aboutpage_response(self):
        response = self.client.get('/aboutme/')
        self.assertEqual(response.status_code, 200)

