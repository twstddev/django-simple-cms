from django.test import TestCase
from menuitems.models import MenuItem
from django.forms import ModelForm
from django.forms.models import model_to_dict

class MenuItemForm( ModelForm ):
	class Meta:
		model = MenuItem

class MenuItemTestCase( TestCase ):
	"""
	Tests menu items model.
	"""
	def setUp( self ):
		self.m_model = MenuItem.objects.create(
			title = "Home",
			url = "/",
		)

	def test_allows_saving_valid_model( self ):
		"""
		Simple checks that valid model is VALID.
		"""
		self.assertTrue( self.check_form_is_valid() )

	def test_requires_title_to_be_set( self ):
		"""
		Makes sure that title is required.
		"""
		self.m_model.title = ""

		self.assertFalse( self.check_form_is_valid() )

	def test_requires_url_to_be_set( self ):
		"""
		Makes sure that url is required.
		"""
		self.m_model.url = ""
		
		self.assertFalse( self.check_form_is_valid() )

	def test_works_as_a_tree( self ):
		"""
		Checks if menu items can act as a tree and be nested.
		"""
		self.m_model.save()

		self.assertEqual( self.m_model.children.count(), 0 )

		child_item = self.m_model.children.create(
			title = "About",
			url = "about"
		)

		self.assertEqual( child_item.parent.id, self.m_model.id )
		self.assertEqual( self.m_model.children.count(), 1 )

	def get_form_for_model( self ):
		return MenuItemForm(
			instance = self.m_model,
			data = model_to_dict( self.m_model )
		)

	def check_form_is_valid( self ):
		model_form = self.get_form_for_model()
		return model_form.is_valid()

