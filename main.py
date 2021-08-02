import logging
import yaml

from prproto.tablesets import get_table_set
from prproto.source import LocalTableLoader

TABLE_SET_NAME = "on_trade"


# TODO: Problèmes d'imports circulaires créés par les types annotations
# TODO: Transfo / filtres juste mis dans des listes? Pattern Chain of responsability ?
# Idee: Unit test de fonction pandas: assert id différentes entre l'input et l'output (?)
# Validation steps : font appel à une conf globale: global_conf.STRONG_VALIDATION pour savoir si on lève exception.
# Cela a-t-il un sens que la validation puisse être faible ? Sinon argument du constructeur de la classe si pas utile d'exposer via la conf.
# Problème des objets collectifs: individualiser, pose notamment la question de la clé/de récupérer l'objet. Ces objets sont des genres de Mediator.


def main():
    logging.basicConfig(level='INFO')

    with open("config.yaml", "r") as file_handle:
        config = yaml.load(file_handle)

    config = config["local"]

    table_loader = LocalTableLoader(config=config)
    table_set = get_table_set(key=TABLE_SET_NAME)
    table_set.load(loader=table_loader)


if __name__ == "__main__":
    main()
