import unittest


from tests.add_activity_ATS import AddActivity_ATS
from tests.edit_activity_ATS import Edit
from tests.organization_signup import Org_Signup_ATS
from tests.search_activity import SearchActivity_ATS
from tests.test_addact_admin import AddActivityAdminATS
from tests.test_addorganization_admin import AddOrgAdmin
from tests.test_addprofile_admin import AddProfileAdminATS
from tests.test_forgot_password import forgotPassword
from tests.volunteer_signup import VolunteerSignupATS
from tests.volunteer_login import VolLogin
from tests.applying_for_activity import apply
from tests.delete_activity_ATS import Delete

tc1 = unittest.TestLoader().loadTestsFromTestCase(AddActivity_ATS)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Edit)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Org_Signup_ATS)
tc4 = unittest.TestLoader().loadTestsFromTestCase(AddOrgAdmin)
tc5 = unittest.TestLoader().loadTestsFromTestCase(AddProfileAdminATS)
tc6 = unittest.TestLoader().loadTestsFromTestCase(VolunteerSignupATS)
tc7 = unittest.TestLoader().loadTestsFromTestCase(VolLogin)
tc8 = unittest.TestLoader().loadTestsFromTestCase(forgotPassword)
tc9 = unittest.TestLoader().loadTestsFromTestCase(SearchActivity_ATS)
tc10 = unittest.TestLoader().loadTestsFromTestCase(AddActivityAdminATS)
tc11 = unittest.TestLoader().loadTestsFromTestCase(Delete)
tc12 = unittest.TestLoader().loadTestsFromTestCase(apply)


TestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10, tc11, tc12, ])
unittest.TextTestRunner().run(TestSuite)
