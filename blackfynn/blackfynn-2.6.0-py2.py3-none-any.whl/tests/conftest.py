import os
from datetime import datetime
from uuid import uuid4

import pytest

from blackfynn import Blackfynn
from tests.utils import create_test_dataset, current_ts, get_test_client


@pytest.fixture(scope='session')
def client():
    """
    Login via API, return client. Login information, by default, will be taken from
    environment variables, so ensure those are set properly before testing. Alternatively,
    to force a particular user, adjust input arguments as necessary.
    """
    return get_test_client()


@pytest.fixture(scope='session')
def client2():
    api_token = os.environ.get('BLACKFYNN_API_TOKEN2')
    api_secret = os.environ.get('BLACKFYNN_API_SECRET2')
    assert api_token != "", "Must define BLACKFYNN_API_TOKEN2"
    assert api_secret != "", "Must define BLACKFYNN_API_SECRET2"

    bf = get_test_client(api_token=api_token, api_secret=api_secret)
    return bf


@pytest.fixture(scope='session')
def session_id():
    return "{}-{}".format(str(datetime.now()), str(uuid4())[:4])


@pytest.fixture(scope='session')
def dataset(client):
    """
    Test Dataset to be used by other tests.
    """
    ds = create_test_dataset(client)
    ds_id = ds.id
    all_dataset_ids = [x.id for x in client.datasets()]
    assert ds_id in all_dataset_ids

    # surface test dataset to other functions. Everything after the yield
    # serves as teardown code for the fixture
    yield ds

    # remove
    client._api.datasets.delete(ds)

    all_dataset_ids = [x.id for x in client.datasets()]
    assert ds_id not in all_dataset_ids
    assert not ds.exists
    assert not hasattr(ds, 'parent')


@pytest.fixture(scope='session')
def test_organization(client):
    return [o for o in client.organizations() if o.name == 'Blackfynn'][0]
