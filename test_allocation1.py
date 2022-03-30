from theater import Theater
import pytest
import filecmp

@pytest.fixture(scope="function")

def dummy_Theater():
	return Theater ("data3.txt",10,20, 3)


def test_reserve(dummy_Theater):
	assert filecmp.cmp(dummy_Theater.seatReservation(), "ot3.txt", shallow=False)