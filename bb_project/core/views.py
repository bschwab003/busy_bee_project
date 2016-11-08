from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from core.models import *
from core.forms import *
import json

###############################################################################################
# Demo
###############################################################################################

class DemoList(ListView):

	headers = [
		("Name",50),
	]
	queryset = Demo.objects.all()
	template_name = 'core/list_demos.html'
	title = "Demo Master"


class ScheduleDemos(TemplateView):

	template_name = 'core/schedule_demos.html'
	title = "Scheduler"

	def post(self, request, *args, **kwargs):

		client_id = request.POST.get("client", None)
		brand_id = request.POST.get("brand", None)	
		demo_type_id = request.POST.get("demo_type", None)
		product_ids = request.POST.getlist("product", None)

		demo_counts = []
		for key, last_value in request.POST.items():
			x = key.split("_")
			if x[0] == "store" and last_value != '':
				for each in request.POST.getlist(key, None):
					demo_counts.append((int(x[1]), int(each)))

		# Create Demos
		for store_id, count in demo_counts:
			for i in range(count):
				demo = Demo()
				demo.demo_type = DemoType.objects.get(id=demo_type_id)
				demo.store = Store.objects.get(id=store_id)
				demo.brand = Brand.objects.get(id=brand_id)
				demo.save()
				for product_id in product_ids:
					demo.products.add(Product.objects.get(id=product_id))

		return HttpResponse("Successful POST")


###############################################################################################
# List Views
###############################################################################################

class ClientList(ListView):

	headers = [
		("Name",50),
	]
	queryset = Client.objects.all()
	template_name = 'core/list_objects.html'
	title = "Client Master"

class BrandList(ListView):

	headers = [
		("Name", 50),
		("Client", 20),
	]
	queryset = Brand.objects.all()
	template_name = 'core/list_objects.html'
	title = "Brand Master"

class BrandAmbassadorList(ListView):

	headers = [
		("Name", 16),
		("Address", 20),
		("City, State", 10),
		("Zip", 5),
		("E-Mail", 15),
		("Phone", 10),
	]
	queryset = BrandAmbassador.objects.all()
	template_name = 'core/list_objects.html'
	title = "Brand Ambassador Master"
	update_delete_url = "brand_ambassadors"

class StoreList(ListView):

	headers = [
		("Region", 5),
		("Chain", 15),
		("Name", 20),
		("Address", 25),
		("City", 10),
		("State", 5),
		("Zip", 5),
		
	]
	queryset = Store.objects.all()
	template_name = 'core/list_objects.html'
	title = "Store Master"
	update_delete_url = "stores"

class StoreContactList(ListView):

	headers = [
		("Last Name", 15),
		("First Name", 15),
		("Title", 20),
		("E-Mail", 20),
		("Phone", 10),
	]
	queryset = StoreContact.objects.all()
	template_name = 'core/list_objects.html'
	title = "Store Contact Master"
	update_delete_url = "store_contacts"


###############################################################################################
# Create Views
###############################################################################################

class CreateClient(CreateView):

	model = Client
	form_class = ClientForm
	template_name = 'core/base_form.html'
	title = "Create Client"
	success_url = "/clients"

class CreateBrand(CreateView):

	model = Brand
	form_class = BrandForm
	template_name = 'core/base_form.html'
	title = "Create Brand"
	success_url = "/brands"

class CreateBrandAmbassador(CreateView):

	model = BrandAmbassador
	form_class = BrandAmbassadorForm
	template_name = 'core/base_form.html'
	title = "Create Brand Ambassador"
	success_url = "/brand_ambassadors"

class CreateStore(CreateView):

	model = Store
	form_class = StoreForm
	template_name = 'core/base_form.html'
	title = "Create Store"
	success_url = "/stores"

class CreateStoreContact(CreateView):
	
	model = StoreContact
	form_class = StoreContactForm
	template_name = 'core/base_form.html'
	title = "Create Store Contact"
	success_url = "/store_contacts"


###############################################################################################
# Update Views
###############################################################################################

class UpdateClient(UpdateView):

	model = Client
	form_class = ClientForm
	template_name = 'core/base_form.html'
	title = "Update Client"
	success_url = "clients"

class UpdateBrand(UpdateView):

	model = Brand
	form_class = BrandForm
	template_name = 'core/base_form.html'
	title = "Update Brand"
	success_url = "brands"

class UpdateBrandAmbassador(UpdateView):
	
	model = BrandAmbassador
	form_class = BrandAmbassadorForm
	template_name = 'core/base_form.html'
	title = "Update Brand Ambassador"
	success_url = "brand_ambassadors"

class UpdateStore(UpdateView):

	model = Store
	form_class = StoreForm
	template_name = 'core/base_form.html'
	title = "Update Store"
	success_url = "stores"

class UpdateStoreContact(UpdateView):

	model = StoreContact
	form_class = StoreContactForm
	template_name = 'core/base_form.html'
	title = "Update Store Contact"
	success_url = "store_contacts"

###############################################################################################
# Delete Views
###############################################################################################


###############################################################################################
# Ajax Calls
###############################################################################################

def ajax_clients(request):

	d = [each.as_dict() for each in Client.objects.all()]
	return HttpResponse(json.dumps(d), content_type='application/json')

def ajax_demo_types(request):

	d = [each.as_dict() for each in DemoType.objects.all()]
	return HttpResponse(json.dumps(d), content_type='application/json')


def ajax_stores(request):

	d = [each.as_dict() for each in Store.objects.all()]
	return HttpResponse(json.dumps(d), content_type='application/json')

def ajax_store_contacts(request):

	d = [each.json_safe() for each in StoreContact.objects.all()]
	return HttpResponse(json.dumps(d), content_type='application/json')

def ajax_brands(request, client_id):

	d = [each.as_dict() for each in Brand.objects.filter(client_id=client_id)]
	return HttpResponse(json.dumps(d), content_type='application/json')

def ajax_products(request, brand_id):

	d = [each.as_dict() for each in Product.objects.filter(brand_id=brand_id)]
	return HttpResponse(json.dumps(d), content_type='application/json')

def ajax_brand_ambassadors(request):

	d = [each.json_safe() for each in BrandAmbassador.objects.all()]
	return HttpResponse(json.dumps(d), content_type='application/json')

def ajax_demos(request):

	d = [each.json_safe() for each in Demo.objects.all()]
	return HttpResponse(json.dumps(d), content_type='application/json')