from behave import *
from functions.Functions import Functions

use_step_matcher("re")


class StepsDefinitions:

    @given('I connect with endpoint (.*)')
    def step_impl(self, host):
        self._endpoint = Functions.get_full_host(self, host)
        return self._endpoint

    @step("I do a Get")
    def step_impl(self):
        self._response = Functions.do_a_get(self)
        return self._response

    @step("I print out the results of the response")
    def step_impl(self):
        Functions.print_api_response(self)