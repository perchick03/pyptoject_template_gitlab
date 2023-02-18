from click.testing import CliRunner

from {{cookiecutter.project_name}}.cli import cli
from {{cookiecutter.project_name}} import __version__

def test_version():
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0
    assert __version__ in result.output