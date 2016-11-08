from django.core.management.base import BaseCommand, CommandError
from core.models import *
import random
import datetime



clients = ["Client " + str(n) for n in range(25)]
chains =  ["Chain " + str(n) for n in range(50)]


class Command(BaseCommand):


    def seed_demo_types(self):

        DemoType.objects.all().delete()

        types = [
            ("Cooking", 85),
            ("Assisted Sale", 50)
        ]
        for type_name, type_pay in types:
            the_type = DemoType()
            the_type.name = type_name
            the_type.ba_pay = type_pay
            the_type.save()

    def seed_regions(self):

        Region.objects.all().delete()

        regions = [
            "Midwest",
            "Northwest",
            "Northeast",
            "Southwest",
            "Southeast"
        ]
        for each in regions:
            region = Region()
            region.name = each
            region.save()


    def seed_chains(self):

        Chain.objects.all().delete()
        for n in range(12):
            chain = Chain()
            chain.name = "Chain " + str(n)
            chain.save()


    def seed_stores(self):

        Store.objects.all().delete()
        for n in range(25):
            store = Store()
            store.name = "Store " + str(n)
            store.address_1 = "1234 Mullberry Lane"
            store.address_2 = "4E"
            store.city = "Chicago"
            store.state = "IL"
            store.zip_code = "60622"
            store.region = random.choice(Region.objects.all())
            store.chain = random.choice(Chain.objects.all())
            store.save()

    def seed_store_contacts(self):

        StoreContact.objects.all().delete()
        for n, each_store in enumerate(Store.objects.all()):
            for _ in range(random.choice([1, 2, 3, 4])):
                store_contact = StoreContact()
                store_contact.name_last = "Last Name " + str(n) + "(sc)"
                store_contact.name_first = "First Name " + str(n)
                store_contact.email = "iamstorecontact@gmail.com"
                store_contact.phone = "(773) 432-2199"
                store_contact.store = each_store
                store_contact.save()
    
    def seed_clients(self):

        Client.objects.all().delete()
        for n in range(16):
            client = Client()
            client.name = "Client " + str(n)
            client.save()

    def seed_brands(self):

        Brand.objects.all().delete()
        for n in range(48):
            brand = Brand()
            brand.name = "Brand " + str(n)
            brand.client = random.choice(Client.objects.all())
            brand.save()

    def seed_products(self):

        Product.objects.all().delete()
        n = 0
        for each_brand in Brand.objects.all():
            for _ in range(random.choice([1, 2, 3])):
                product = Product()
                product.description = "Product " + str(n)
                product.brand = each_brand
                product.save()
                n += 1

    def seed_brand_ambassadors(self):

        BrandAmbassador.objects.all().delete()
        for n in range(100):
            ba = BrandAmbassador()
            ba.name_last = "Last Name " + str(n)
            ba.name_first = "First Name " + str(n)
            ba.address_1 = "1234 Mullberry Lane"
            ba.address_2 = "4E"
            ba.city = "Chicago"
            ba.state = "IL"
            ba.zip_code = "60622"
            ba.email = "iambrandambassador@gmail.com"
            ba.phone = "(773) 432-2199"
            ba.region = random.choice(Region.objects.all())
            ba.save()


    def seed_demos(self):

        Demo.objects.all().delete()
        for n in range(130):
            demo = Demo()
            demo.demo_type = random.choice(DemoType.objects.all())
            demo.date = datetime.date(2015, 10, 25)
            demo.start_time = datetime.time(11, 00)
            demo.end_time = datetime.time(3, 00)
            demo.store = random.choice(Store.objects.all())
            demo.brand = random.choice(Brand.objects.all())
            demo.brand_ambassador = random.choice(BrandAmbassador.objects.all())
            demo.save()
            demo.products.add(random.choice(Product.objects.filter(brand=demo.brand)))

    def handle(self, *args, **options):
        
        self.seed_demo_types()
        self.seed_regions()
        # self.seed_chains()
        # self.seed_stores()
        # self.seed_store_contacts()
        # self.seed_clients()
        # self.seed_brands()
        # self.seed_products()
        # self.seed_brand_ambassadors()
        # self.seed_demos()


