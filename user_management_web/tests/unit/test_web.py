from django.core.urlresolvers import resolve
import pytest
from user_management_web.views import main_control


def test_root_resolves_to_hello_world():
    found = resolve('/web/')
    assert found.func == main_control

def test_hello_world_contains_greeting(client):
    response = client.get('/web/')
    assert response.context['greeting'] == 'hello world'
