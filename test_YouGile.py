import pytest
from project_YouGile import ProjectYouGile


@pytest.fixture
def api():
    return ProjectYouGile()


@pytest.fixture
def created_project(api):
    """Создает проект для тестов и возвращает его ID"""
    response = api.create_project("Тестовый проект для редактирования")
    assert response.status_code == 201
    project_data = response.json()
    project_id = project_data['id']
    yield project_id


def test_get_projects_list_positive(api):
    """Позитивный тест получения списка проектов"""
    response = api.get_projects_list()
    assert response.status_code == 200

    projects = response.json()["content"]
    assert isinstance(projects, list)


def test_create_project_positive(api):
    """Позитивный тест создания проекта"""
    test_title = "Новый тестовый проект"
    response = api.create_project(test_title)
    assert response.status_code == 201
    
    project_data = response.json()
    assert 'id' in project_data

    project_id = project_data['id']
    get_response = api.get_project_with_id(project_id)
    assert get_response.status_code == 200
    
    retrieved_project = get_response.json()
    assert retrieved_project['id'] == project_id
    assert retrieved_project['title'] == test_title

def test_get_project_with_id_positive(api, created_project):
    """Позитивный тест получения проекта по ID"""
    response = api.get_project_with_id(created_project)
    assert response.status_code == 200
    
    project_data = response.json()
    assert project_data['id'] == created_project


def test_edit_project_positive(api, created_project):
    """Позитивный тест редактирования проекта"""
    new_title = "Обновленное название проекта"
    
    response = api.edit_project(created_project, new_title)
    assert response.status_code == 200
    

    get_response = api.get_project_with_id(created_project)
    assert get_response.status_code == 200
    
    updated_project = get_response.json()
    assert updated_project['title'] == new_title


def test_create_project_without_title(api):
    """Негативный тест: создание проекта без title"""
    response = api.create_project("")
    assert response.status_code == 400

def test_create_project_invalid_json(api):
    """Негативный тест: создание проекта с некорректным JSON"""
    response = api.create_project(None)
    assert response.status_code in [400, 422, 500]

def test_get_nonexistent_project(api):
    """Негативный тест: получение несуществующего проекта"""
    non_existent_id = "non_existent_id_12345"
    response = api.get_project_with_id(non_existent_id)
    assert response.status_code == 404

def test_edit_nonexistent_project(api):
    """Негативный тест: редактирование несуществующего проекта"""
    non_existent_id = "non_existent_id_12345"
    response = api.edit_project(non_existent_id, "Новое название")
    assert response.status_code == 404

def test_edit_project_without_title(api, created_project):
    """Негативный тест: редактирование проекта с пустым title"""
    response = api.edit_project(created_project, "")
    assert response.status_code == 400
