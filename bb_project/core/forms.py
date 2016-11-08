from django.forms import ModelForm
from core.models import *


class ClientForm(ModelForm):

	class Meta:
		model = Client
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(ClientForm, self).__init__(*args, **kwargs)

		for field_name, field in self.fields.items():
			field.widget.attrs["class"] = "form-control"

class BrandForm(ModelForm):

	class Meta:
		model = Brand
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(BrandForm, self).__init__(*args, **kwargs)

		for field_name, field in self.fields.items():
			field.widget.attrs["class"] = "form-control"

class BrandAmbassadorForm(ModelForm):

	class Meta:
		model = BrandAmbassador
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(BrandAmbassadorForm, self).__init__(*args, **kwargs)

		for field_name, field in self.fields.items():
			field.widget.attrs["class"] = "form-control"

class StoreForm(ModelForm):

	class Meta:
		model = Store
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(StoreForm, self).__init__(*args, **kwargs)

		for field_name, field in self.fields.items():
			field.widget.attrs["class"] = "form-control"

class StoreContactForm(ModelForm):

	class Meta:
		model = StoreContact
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(StoreContactForm, self).__init__(*args, **kwargs)

		for field_name, field in self.fields.items():
			field.widget.attrs["class"] = "form-control"