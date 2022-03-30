
from theater import Theater
import pytest
import filecmp

@pytest.fixture(scope="function")

def dummy_Theater():
	return Theater ("data1.txt",10,20, 3)


def test_reserve(dummy_Theater):
	print(dummy_Theater.seatReservation())
	assert filecmp.cmp(dummy_Theater.seatReservation(), "ot1.txt", shallow=False)
