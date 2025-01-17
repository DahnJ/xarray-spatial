import pytest
import numpy as np

from xrspatial import aspect
from xrspatial import curvature
from xrspatial import slope
from xrspatial.analytics import summarize_terrain

from xrspatial.tests.general_checks import create_test_raster


@pytest.mark.parametrize("size", [(2, 4), (100, 150)])
@pytest.mark.parametrize(
    "dtype", [np.int32, np.int64, np.uint32, np.uint64, np.float32, np.float64]
)
def test_summarize_terrain(random_data):
    test_terrain = create_test_raster(random_data, name='myterrain')
    summarized_ds = summarize_terrain(test_terrain)
    variables = [v for v in summarized_ds]
    should_have = ['myterrain',
                   'myterrain-slope',
                   'myterrain-curvature',
                   'myterrain-aspect']
    assert variables == should_have

    np.testing.assert_allclose(summarized_ds['myterrain-slope'], slope(test_terrain))
    np.testing.assert_allclose(summarized_ds['myterrain-curvature'], curvature(test_terrain))
    np.testing.assert_allclose(summarized_ds['myterrain-aspect'], aspect(test_terrain))
