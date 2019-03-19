
import numpy as np
import pytest

from rtrace.rtrace import ray_x_plane

def test_ray_x_plane1(request):
    r0 = np.array([ 1.0, 0.0, 0.0 ])
    rd = np.array([ 1.0, 0.0, 0.0 ])
    pn = np.array([-1.0, 0.0, 0.0 ])
    pp = np.array([ 2.0, 0.0, 0.0 ])
    t = ray_x_plane(r0, rd, pp, pn, tol=1e-6)
    ri = r0 + rd*t
    assert np.allclose(ri, np.array([2.0, 0.0, 0.0]))

def test_ray_x_plane2(request):
    r0 = np.array([  2.0,    3.0,    4.0   ])
    rd = np.array([  0.577,  0.577,  0.577 ])
    pn = np.array([ -1.0,    0.0,    0.0   ])
    pp = np.array([  7.0,    0.0,    0.0   ])
    t = ray_x_plane(r0, rd, pp, pn, tol=1e-6)
    ri = r0 + rd*t
    assert np.allclose(ri, np.array([7.0, 8.0, 9.0]))
