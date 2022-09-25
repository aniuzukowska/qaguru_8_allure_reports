from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_1_github_name_issue():
    browser.open("https://github.com")

    s(".header-search-input").click()
    s(".header-search-input").send_keys("aniuzukowska/qaguru_7_model")
    s(".header-search-input").submit()

    s(by.link_text("aniuzukowska/qaguru_7_model")).click()

    s("#issues-tab").click()

    s(by.partial_text("test")).should(be.visible)

