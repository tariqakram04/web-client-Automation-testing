from pages.requirements_page import RequirementsPage
from utilities.wait_utils import WaitUtils

class RequirementsActions:
    def __init__(self, page):
        self.page = page
        self.req_page = RequirementsPage(page)
        self.wait = WaitUtils(page)

    def create_requirement_if_not_exists(self, folder, name, desc, criticality, gxp):
        self.wait.wait_for_element(self.page.get_by_text("Requirements"))
        self.req_page.expand_folder_if_collapsed("Requirements")
        self.req_page.go_to_requirements()
        if not self.req_page.requirement_exists(name):
            self.req_page.create_requirement_fields(name, desc, criticality, gxp)
            self.req_page.click_submit()
        else:
            self.wait.wait_for_element(self.page.get_by_text(folder))
            self.req_page.click_folder(folder)

        

    def verify_phase_draft(self):
        self.wait.wait_until_value(self.req_page.get_phase_combobox(), "Draft")
