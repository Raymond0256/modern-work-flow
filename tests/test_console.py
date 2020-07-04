import click.testing
import pytest


from modern_work_flow import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.fixture
def mock_request_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolar sit amet",
    }
    return mock


def test_main_succeeds(runner, mock_request_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner, mock_request_get):
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output