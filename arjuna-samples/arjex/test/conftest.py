import pytest

from arjuna.engine.pytest import PytestHooks

try:
    from arjex.lib.resource.group import *
except ModuleNotFoundError:
    pass

try:
    from arjex.lib.resource.module import *
except ModuleNotFoundError:
    pass

try:
    from arjex.lib.resource.test import *
except ModuleNotFoundError:
    pass


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    result = yield
    PytestHooks.add_screenshot_for_result(item, result)


def pytest_generate_tests(metafunc):
    PytestHooks.configure_group_for_test(metafunc)


def pytest_collection_modifyitems(items, config):
    PytestHooks.select_tests(items, config)