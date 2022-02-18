import random
import uuid
from typing import Callable

import pytest

from scripts.folder_copy import DuplicatedFileNames
from scripts.models import get_timestamp
from scripts.models import Node
from scripts.models import ResourceType
from scripts.neo4j_helper import Neo4jPathCheck


@pytest.fixture
def create_node(faker) -> Callable[..., Node]:
    def _create_node(global_entity_id=None, name=None, labels=None, archived=None) -> Node:
        if global_entity_id is None:
            global_entity_id = f'{uuid.uuid4()}-{get_timestamp()}'

        if name is None:
            name = faker.word()

        if labels is None:
            labels = [random.choice(list(ResourceType))]

        if archived is None:
            archived = faker.pybool()

        return Node(
            {
                'global_entity_id': global_entity_id,
                'name': name,
                'labels': labels,
                'archived': archived,
            }
        )

    return _create_node


@pytest.fixture
def duplicated_files():
    yield DuplicatedFileNames()


@pytest.fixture
def path_check():
    yield Neo4jPathCheck('zone')
