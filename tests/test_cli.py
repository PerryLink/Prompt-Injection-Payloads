"""Tests for CLI commands"""

import pytest
from click.testing import CliRunner
from prompt_injection_payloads.cli import main


@pytest.fixture
def runner():
    return CliRunner()


def test_main_help(runner):
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Prompt Injection Payloads" in result.output


def test_list_command(runner):
    result = runner.invoke(main, ["list"])
    assert result.exit_code == 0
    assert "Found" in result.output


def test_list_with_category(runner):
    result = runner.invoke(main, ["list", "--category", "role-hijacking"])
    assert result.exit_code == 0


def test_list_with_search(runner):
    result = runner.invoke(main, ["list", "--search", "DAN"])
    assert result.exit_code == 0


def test_list_with_severity(runner):
    result = runner.invoke(main, ["list", "--severity", "high"])
    assert result.exit_code == 0


def test_show_command(runner):
    result = runner.invoke(main, ["show", "rh-001"])
    assert result.exit_code == 0
    assert "DAN" in result.output


def test_show_invalid_id(runner):
    result = runner.invoke(main, ["show", "invalid-id"])
    assert result.exit_code == 0
    assert "not found" in result.output


def test_random_command(runner):
    result = runner.invoke(main, ["random"])
    assert result.exit_code == 0
    assert "Random Payload" in result.output


def test_random_with_category(runner):
    result = runner.invoke(main, ["random", "--category", "jailbreak"])
    assert result.exit_code == 0
