from django.test import TestCase

from people.factories.organization_factory import OrganizationFactory
from people.factories.edition_factory import EditionFactory
from people.models import Organization

class TestOrganization(TestCase):

    def test_create_organization(self):
        """This is an example of how to use Factories. """
        organization_count = Organization.objects.count()

        organization = OrganizationFactory()

        self.assertEqual(organization_count + 1,
                         Organization.objects.count(),
                         "A new organization was not created.")

    def test_get_unicode(self):
        """Testing if the url works"""
        url = "www.rosedu.org"
        organization = OrganizationFactory(url=url)
 
	self.assertEqual(str(organization), url,
                         "Organization conversion to unicode is broken.")
                         
                         
class TestRole(TestCase):

    def test_get_unicode(self):
        """Testing if the role conversion to unicode works"""
        name = "admin"
        role = RoleFactory(name=name)

        self.assertEqual(str(role), name,
                        "Role conversion to unicode is broken.")
class TestEdition(TestCase):

	def test_get_unicode(self):
		"""Testing if the Edition name conversion to unicode works"""
		name = "edition"	
		edition = EditionFactory(name = name)
		self.assertEqual(str(edition), name,
						"Edition name verversion to unicode works.")
		

