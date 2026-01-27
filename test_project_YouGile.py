from project_YouGile import ProjectYouGile


name = "TestCompany"
users = {"9cb5b2fc-ca2c-4a01-bafc-103ae55d2a57": "admin"}


api = ProjectYouGile('https://ru.yougile.com/api-v2/')


def test_create_project():
    # количество проектов до
    projects_before = api.get_project_list()
    len_before = len(projects_before)

    # создание проекта
    project_id = api.create_project('New_Project_Test', users)

    # количество проектов после
    projects_after = api.get_project_list()
    len_after = len(projects_after)

    assert len_after - len_before == 1

    # удаляем созданный проект
    api.edit_project(project_id, True, 'Del_Project_Test')

def test_get_project_with_id():
    title = 'Get_Project_Test'
    result = api.create_project(title, users)
    project_id = result['id']

    # обращаемся к проекту
    new_project = api.get_project_with_id(project_id)

    assert new_project['title'] == title
    assert new_project['users'] == users

    # удаляем созданный проект
    api.edit_project(project_id, True, 'Del_Project_Test')


def test_edit_project():
    title = 'Edit_Project_Test'

    result = api.create_project(title, users)

    project_id = result['id']

    api.edit_project(project_id, False, 'Edited_Project_Test')

    edited = api.get_project_with_id(project_id)

    assert edited['title'] == 'Edited_Project_Test'

    # удаляем созданный проект
    api.edit_project(project_id, True, 'Del_Project_Test')
