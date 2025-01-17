import json

from click.testing import CliRunner
import pytest

from watson_jira_next import cli


@pytest.fixture(scope="module")
def runner():
    return CliRunner()

def test_sync(runner):
    result = runner.invoke(cli.main, ["sync"])
    assert result.exit_code == 0

def test_logs(runner):
    result = runner.invoke(cli.main, ["logs"])
    assert result.exit_code == 0


