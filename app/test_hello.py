import pytest
from hello import app, message


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_status_code(client):
    """Test that the root endpoint returns 200 OK."""
    response = client.get('/')
    assert response.status_code == 200


def test_hello_response_content(client):
    """Test that the response contains the expected message."""
    response = client.get('/')
    assert message.encode() in response.data


def test_hello_content_type(client):
    """Test that the response has the correct content type."""
    response = client.get('/')
    assert 'text/html' in response.content_type


def test_hello_response_is_not_empty(client):
    """Test that the response body is not empty."""
    response = client.get('/')
    assert len(response.data) > 0


def test_nonexistent_route_returns_404(client):
    """Test that accessing a non-existent route returns 404."""
    response = client.get('/nonexistent')
    assert response.status_code == 404


def test_post_method_not_allowed(client):
    """Test that POST method is not allowed on root endpoint."""
    response = client.post('/')
    assert response.status_code == 405


def test_put_method_not_allowed(client):
    """Test that PUT method is not allowed on root endpoint."""
    response = client.put('/')
    assert response.status_code == 405


def test_delete_method_not_allowed(client):
    """Test that DELETE method is not allowed on root endpoint."""
    response = client.delete('/')
    assert response.status_code == 405


def test_message_is_valid_greeting():
    """Test that the message is one of the expected greetings."""
    valid_messages = ["Hello, Sasha!", "Hello, World!"]
    assert message in valid_messages
