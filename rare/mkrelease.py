import random

from setuptools_scm import ScmVersion


def mkversion(ver: ScmVersion) -> str:
    return f"{ver.tag}.{ver.distance}"


def mkname() -> str:
    from legendary.core import LegendaryCore

    core = LegendaryCore()
    core.login()

    return " ".join(
        map(
            lambda game: game.app_name,
            random.choices(list(filter(lambda x: len(x.app_name) != 32, core.get_game_list(False))), k=2),
        )
    )
