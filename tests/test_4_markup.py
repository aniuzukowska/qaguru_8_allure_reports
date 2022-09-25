import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "annazukowska")
@allure.feature("Задачи в репозитории")
@allure.story("Проверка названия задачи")
@allure.link("https://github.com", name="Testing")
def test_4_github_name_issue():
    with allure.step("Открываем главную страницу:"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий:"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("aniuzukowska/qaguru_7_model")
        s(".header-search-input").submit()

    with allure.step("Переходим по ссылке репозитория:"):
        s(by.link_text("aniuzukowska/qaguru_7_model")).click()

    with allure.step("Открываем таб Issues:"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с названием test:"):
        s(by.partial_text("test")).should(be.visible)




