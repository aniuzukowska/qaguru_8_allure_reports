import allure
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_3_github_name_issue():
    open_git_hub()
    search_for_repository("aniuzukowska/qaguru_7_model")
    go_to_repository("aniuzukowska/qaguru_7_model")
    open_issue_tab()
    should_see_issue_with_number("test")


@allure.step("Открываем главную страницу:")
def open_git_hub():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}:")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}:")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues:")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с названием {name}:")
def should_see_issue_with_number(name):
    s(by.partial_text(name)).click()


