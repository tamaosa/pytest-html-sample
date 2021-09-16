from datetime import datetime
from py.xml import html  # type: ignore
import pytest

import docstring_parser


def pytest_html_report_title(report):
    report.title = "ナベアツ テスト仕様書"


def pytest_configure(config):
    config._metadata["Version"] = "9.9.9"


def pytest_html_results_table_header(cells):
    del cells[1:]
    cells.insert(0, html.th("Tests"))
    cells.insert(1, html.th("Expects"))
    cells.append(html.th("Time", class_="sortable time", col="time"))


def pytest_html_results_table_row(report, cells):
    del cells[1:]
    cells.insert(0, html.td(report.tests))
    cells.insert(1, html.td(report.expects))
    cells.append(html.td(datetime.now(), class_="col-time"))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    docstring = docstring_parser.parse(str(item.function.__doc__))
    report.tests = docstring["Tests"]
    report.expects = docstring["Expects"]
