import requests
import os
from dotenv import load_dotenv


load_dotenv()


class ProjectYouGile:
    def __init__(self):
        self.login = os.getenv('YOUGILE_LOGIN')
        self.password = os.getenv('YOUGILE_PASSWORD')
        self.company_id = os.getenv('YOUGILE_COMPANY_ID')
        self.user_id = os.getenv('YOUGILE_USER_ID')
        self.base_url = "https://ru.yougile.com/api-v2"
        
    def __get_token(self):
        """Получение токена авторизации"""
        url = f"{self.base_url}/auth/keys"
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": self.company_id
        }
        
        response = requests.post(url, json=payload)
        token_data = response.json()
        return token_data.get("key")
    
    def _get_auth_headers(self):
        """Получение заголовков с токеном авторизации"""
        return {
            "Authorization": f"Bearer {self.__get_token()}",
            "Content-Type": "application/json"
        }
    
    def get_projects_list(self):
        """Получение списка проектов"""
        url = f"{self.base_url}/projects"
        headers = self._get_auth_headers()
        
        response = requests.get(url, headers=headers)
        return response
    
    def create_project(self, title):
        """Создание нового проекта"""
        url = f"{self.base_url}/projects"
        headers = self._get_auth_headers()
        payload = {
            "title": title,
            "users": {
               self.user_id:"admin"
            }
        }
        
        response = requests.post(url, headers=headers, json=payload)
        return response
    
    def get_project_with_id(self, project_id):
        """Получение проекта по ID"""
        url = f"{self.base_url}/projects/{project_id}"
        headers = self._get_auth_headers()
        
        response = requests.get(url, headers=headers)
        return response
    
    def edit_project(self, project_id, title):
        """Редактирование существующего проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        headers = self._get_auth_headers()
        payload = {
            "title": title
        }
        
        response = requests.put(url, headers=headers, json=payload)
        return response
