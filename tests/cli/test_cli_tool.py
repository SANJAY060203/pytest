import sys
from src.cli_tool import main

def test_cli(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["cli_tool", "hello"])
    main()
    assert capsys.readouterr().out.strip() == "olleh"
