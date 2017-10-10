# -*- coding: utf-8 -*_

import pytest
from meucandidato.app import create_app


@pytest.fixture
def app():
    return create_app()
