# tests/test_tracker.py
from click.testing import CliRunner
from fitness_tracker.tracker import main

def test_welcome_message():
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "Welcome to Fitness Tracker CLI!" in result.output
