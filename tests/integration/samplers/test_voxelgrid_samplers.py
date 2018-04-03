import pytest

from pandas import DataFrame

from pyntcloud import PyntCloud
from pyntcloud.utils.array import point_in_array_2D


@pytest.mark.parametrize("sampling_method", [
    "voxelgrid_centers",
    "voxelgrid_centroids",
    "voxelgrid_nearest"
])
@pytest.mark.usefixtures("simple_pyntcloud")
def test_voxelgrid_sampling_return_type(simple_pyntcloud, sampling_method):
    voxelgrid_id = simple_pyntcloud.add_structure("voxelgrid")

    sample = simple_pyntcloud.get_sample(
        sampling_method,
        voxelgrid_id=voxelgrid_id)
    assert type(sample) == DataFrame

    sample = simple_pyntcloud.get_sample(
        sampling_method,
        voxelgrid_id=voxelgrid_id,
        as_PyntCloud=True)
    assert type(sample) == PyntCloud

@pytest.mark.parametrize("x_y_z,expected_n,expected_point", [
    (
        [2, 2, 2],
        2,
        [0.25, 0.25, 0.25]
    ),
    (
        [2, 1, 1],
        2,
        [0.25, 0.5, 0.5]
    )
])
@pytest.mark.usefixtures("simple_pyntcloud")
def test_voxelgrid_centers_expected_values(simple_pyntcloud, x_y_z, expected_n, expected_point):
    voxelgrid_id = simple_pyntcloud.add_structure(
        "voxelgrid",
        x_y_z=x_y_z)
    sample = simple_pyntcloud.get_sample(
        "voxelgrid_centers",
        voxelgrid_id=voxelgrid_id)
    assert len(sample) == expected_n
    assert point_in_array_2D(expected_point, sample.values)


@pytest.mark.parametrize("x_y_z,expected_n,expected_point", [
    (
        [2, 2, 2],
        2,
        [0.2, 0.2, 0.2]
    ),
    (
        [2, 1, 1],
        2,
        [0.2, 0.2, 0.2]
    )
])
@pytest.mark.usefixtures("simple_pyntcloud")
def test_voxelgrid_centroids_expected_values(simple_pyntcloud, x_y_z, expected_n, expected_point):
    voxelgrid_id = simple_pyntcloud.add_structure(
        "voxelgrid",
        x_y_z=x_y_z)
    sample = simple_pyntcloud.get_sample(
        "voxelgrid_centroids",
        voxelgrid_id=voxelgrid_id)
    assert len(sample) == expected_n
    assert point_in_array_2D(expected_point, sample.values)


@pytest.mark.parametrize("x_y_z,n_points,expected_n,expected_point", [
    (
        [2, 2, 2],
        1,
        2,
        [0.2, 0.2, 0.2]
    ),
    (
        [2, 2, 2],
        2,
        4,
        [0.1, 0.1, 0.1]
    ),
    (
        [2, 1, 1],
        1,
        2,
        [0.5, 0.5, 0.5]
    )
])
@pytest.mark.usefixtures("simple_pyntcloud")
def test_voxelgrid_nearest_expected_values(simple_pyntcloud, x_y_z, n_points, expected_n, expected_point):
    voxelgrid_id = simple_pyntcloud.add_structure(
        "voxelgrid",
        x_y_z=x_y_z)
    sample = simple_pyntcloud.get_sample(
        "voxelgrid_nearest",
        voxelgrid_id=voxelgrid_id,
        n=n_points)
    assert len(sample) == expected_n
    assert point_in_array_2D(expected_point, sample.values)

