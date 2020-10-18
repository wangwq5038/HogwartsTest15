import pytest


@pytest.mark.hogwarts
def test_env(env):
    print(f"执行的命令是: {env}")
