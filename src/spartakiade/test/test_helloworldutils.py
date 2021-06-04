# import stdlibs

# import 3rdparty libs
import pytest

# import local libs
from spartakiade.utils import helloworldutils


def test_greet():
    assert helloworldutils.greet("testuser").startswith("Hello testuser")
