import pytest

from weather_app import app, db


@pytest.fixture(scope="module")
def application():

    # Setup
    app.config.update({
        "TESTING": True,
    })
    app.config.update({
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db',
    })

    db.create_all()

    # The testing itself
    yield app

    # Teardown
    db.drop_all()


@pytest.fixture()
def client(application):
    return application.test_client()
