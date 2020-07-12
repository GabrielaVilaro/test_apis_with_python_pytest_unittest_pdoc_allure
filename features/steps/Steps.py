from behave import *
from functions.Functions import Functions

use_step_matcher("re")


class StepsDefinitions:

    @given('I connect with endpoint (.*)')
    def step_impl(self, host):
        self._endpoint = Functions.get_full_host(self, host)
        return self._endpoint
