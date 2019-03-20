
import numpy as np
import pytest

from rtrace.rtrace import ray_x_plane, point_in_polygon

@pytest.mark.parametrize('p', [
    {
        'r0': np.array([ 1.0, 0.0, 0.0 ]), 'rd': np.array([ 1.0, 0.0, 0.0 ]),
        'pn': np.array([-1.0, 0.0, 0.0 ]), 'pp': np.array([ 2.0, 0.0, 0.0 ]),
        'expected': np.array([2.0, 0.0, 0.0])
    },
    {
        'r0': np.array([ 2.0, 3.0, 4.0 ]), 'rd': np.array([ .577, .577, .577 ]),
        'pn': np.array([-1.0, 0.0, 0.0 ]), 'pp': np.array([ 7.0, 0.0, 0.0 ]),
        'expected': np.array([7.0, 8.0, 9.0])
    }
])
def test_ray_x_plane(request, p):
    t = ray_x_plane(p['r0'], p['rd'], p['pp'], p['pn'], tol=1e-6)
    ri = p['r0'] + p['rd'] * t
    assert np.allclose(ri, p['expected'])

@pytest.mark.parametrize('p', [
    {
        'ri': np.array([0.5, 5.0, 0.9]), 'pn': np.array([0.0, 1.0, 0.0]),
        'poly_verts': np.array([
            [ 0.0, 5.0, 0.0 ], [ 0.5, 5.0, 0.5 ],
            [ 1.0, 5.0, 0.0 ], [ 0.5, 5.0, 1.0 ],
        ]),
        'assert': True
    },
    {
        'ri': np.array([0.01, 0.0, 0.02]), 'pn': np.array([0.0, 1.0, 0.0]),
        'poly_verts': np.array([
            [ 0.0, 0.0, 0.0 ], [ 0.5, 0.0, 0.5 ],
            [ 1.0, 0.0, 0.0 ], [ 0.5, 0.0, 1.0 ],
        ]),
        'assert': True
    },
])
def test_point_in_poly(request, p):
    assert point_in_polygon(p['ri'], p['poly_verts'], p['pn']) == p['assert']
