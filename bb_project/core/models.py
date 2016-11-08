from django.db.models import *


class DemoType(Model):

	name = CharField(max_length=255)
	ba_pay = FloatField()

	def as_dict(self):
		return {
			"id": self.id,
			"name": self.name,
			"ba_pay": self.ba_pay
		}


class Region(Model):

	name = CharField(max_length=255, unique=True)

	def __str__(self):
		return self.name


class Chain(Model):

	name = CharField(max_length=255, unique=True)

	def __str__(self):
		return self.name


class Store(Model):

	name = CharField(max_length=255, unique=True)
	address_1 = CharField(max_length=255, null=True)
	address_2 = CharField(max_length=255, null=True)
	city = CharField(max_length=255, null=True)
	state = CharField(max_length=255, null=True)
	zip_code = CharField(max_length=255, null=True)

	region = ForeignKey(Region, related_name="stores")
	chain = ForeignKey(Chain, related_name="stores")

	def __str__(self):
		return self.name

	def as_list(self):
		return [
			self.id,
			self.region.name,
			self.chain.name,
			self.name,
			" ".join([self.address_1, self.address_2]),
			self.city,
			self.state,
			self.zip_code
		]

	def as_dict(self):
		return {
			"id": self.id,
			"name": self.name,
			"address": " ".join([self.address_1, self.address_2]),
			"city": self.city,
			"state": self.state,
			"zip_code": self.zip_code,
			"region": self.region.name,
			"chain": self.chain.name
		}


class StoreContact(Model):

	name_last = CharField(max_length=255)
	name_first = CharField(max_length=255)
	title = CharField(max_length=255)
	email = EmailField(null=True)
	phone = CharField(max_length=255, null=True)

	store = ForeignKey(Store, related_name="store_contacts")

	def __str__(self):
		return " ".join([self.name_first, self.name_last])

	def as_list(self):

		return [
			self.id,
			self.name_last,
			self.name_first,
			self.title,
			self.email,
			self.phone
		]

	def as_dict(self):

		return {
			"id": self.id,
			"name_last": self.name_last,
			"name_first": self.name_first,
			"title": self.title,
			"email": self.email,
			"phone": self.phone
		}


class Client(Model):

	name = CharField(max_length=255, unique=True)

	def __str__(self):
		return self.name

	def as_list(self):

		return [
			self.id, 
			self.name
		]

	def as_dict(self):

		return {
			"id": self.id,
			"name": self.name,
		}


class Brand(Model):

	name = CharField(max_length=255, unique=True)

	client = ForeignKey(Client, related_name="brands")

	def __str__(self):
		return self.name


	def as_list(self):

		return [
			self.id,
			self.name,
			self.client.name
		]

	def as_dict(self):

		return {
			"id": self.id,
			"name": self.name,
			"client": self.client.name
		}


class Product(Model):

	description = CharField(max_length=255)

	brand = ForeignKey(Brand, related_name="products")

	def __str__(self):
		return self.description

	def as_dict(self):
		return {
			"id": self.id,
			"description": self.description
		}


class BrandAmbassador(Model):

	name_last = CharField(max_length=255)
	name_first = CharField(max_length=255)
	address_1 = CharField(max_length=255, null=True)
	address_2 = CharField(max_length=255, null=True)
	city = CharField(max_length=255, null=True)
	state = CharField(max_length=255, null=True)
	zip_code = CharField(max_length=255, null=True)
	email = EmailField(null=True)
	phone = CharField(max_length=255, null=True)

	region = ForeignKey(Region, related_name="brand_ambassadors")

	def __str__(self):
		return " ".join([self.name_first, self.name_last])


	def as_list(self):

		return [
			self.id,
			", ".join([self.name_last, self.name_first]),
			" ".join([self.address_1, self.address_2]),
			", ".join([self.city, self.state]),
			self.zip_code,
			self.email,
			self.phone
		]

	def as_dict(self):

		return {
			"id": self.id,
			"name_last": self.name_last,
			"name_first": self.name_first,
			"address": " ".join([self.address_1, self.address_2]),
			"city": self.city,
			"state": self.state,
			"zip_code": self.zip_code,
			"email": self.email,
			"phone": self.phone
		}


class Demo(Model):

	date = DateField(null=True)
	start_time = TimeField(null=True)
	end_time = TimeField(null=True)

	demo_type = ForeignKey(DemoType, related_name="demos")
	store = ForeignKey(Store, related_name="demos")
	brand = ForeignKey(Brand, related_name="demos")
	brand_ambassador = ForeignKey(BrandAmbassador, related_name="demos", null=True)
	products = ManyToManyField(Product, related_name="demos")


	def as_list(self):

		return [
			self.id,
			self.date.isoformat(),
			" - ".join([self.start_time.isoformat(), self.end_time.isoformat()]),
			self.demo_type.name,
			self.store.region.name,
			self.store.name,
			" ".join([self.store.address_1, self.store.address_2]),
			", ".join([self.store.city, self.store.state]) + " " + self.store.zip_code,
			self.brand.client.name,
			self.brand.name,
			self.brand_ambassador.name_first,
			self.brand_ambassador.name_last,
		]

	def as_dict(self):

		return {
			"id": self.id,
			"date": self.date.isoformat(),
			"time": " - ".join([self.start_time.isoformat(), self.end_time.isoformat()]),
			"demo_type": self.demo_type.name,
			"region": self.store.region.name,
			"store_name": self.store.name,
			"store_address": " ".join([self.store.address_1, self.store.address_2]),
			"store_city_state_zip": ", ".join([self.store.city, self.store.state]) + " " + self.store.zip_code,
			"client": self.brand.client.name,
			"brand": self.brand.name,
			"ba_name_first": self.brand_ambassador.name_first,
			"ba_name_last": self.brand_ambassador.name_last,
		}	


