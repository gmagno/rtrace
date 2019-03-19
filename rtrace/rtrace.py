
import numpy as np


def ray_x_plane(r0, rd, pp, pn, tol=1e-6):
    '''Determines the intersection between a ray, defined by its origin position
        `r0` and direction vector `rd`, and a plane defined by its normal vector
        `pn` and a point `pp`. The distance from the ray's origin to the
        intersection point is computed and returned.

    Parameters
    ----------
    r0: a numpy.ndarray with shape (3,) representing the ray origin position
    rd: a numpy.ndarray with shape (3,) representing the ray direction vector
    pp: a numpy.ndarray with shape (3,) representing a point belonging to the
        plane
    pn: a numpy.ndarray with shape (3,) representing the plane normal vector
    tol: a float representing the tolerance when computing the dot product `vd`.

    Returns
    -------
    A float representing distance from the ray's origint to the intersection
    point between the ray and the plane. If the ray and plane do not intersect
    `inf` is returned. If the ray hits the plane's back `inf` is also returned.
    '''
    vd = np.dot(pn, rd)
    if vd > -tol:
        return np.inf
    v0 = np.dot(pn, pp - r0)
    t = v0 / vd
    if t < 0:
        return np.inf
    return t

def point_in_polygon(ri, poly_verts, pn):
    '''Checks if a point `ri` is inside a polygon defined by its vertices
    `poly_verts` and normal vector `pn`.

    Parameters
    ----------
    ri: a numpy.ndarray with shape (3,) representing the point coordinates to
        check if belongs to the polygon defined by `poly_verts`.
    poly_verts: a numpy.ndarray with shape (N, 3) representing the polygon's
    vertices.
    pn: a numpy.ndarray with shape (3,) representing the polygon normal vector.

    Returns
    -------
    True if `ri` is inside the polygon.
    '''
    throw_away = np.argmax(np.abs(pn))
    poly_verts -= ri
    poly_verts[:, throw_away] = np.zeros(poly_verts.shape[0])
    pass

def ray_x_polygon(r0, rd, pp, pn, poly_verts, tol=1e-6):
    '''

    Parameters
    ----------
    r0, rd, pp, pn, tol: check function `ray_x_plane()` parameters.
    poly_verts: check function `point_in_polygon()` parameters.
    '''
    t = ray_x_plane(r0, rd, pp, pn, tol)
    ri = r0 + rd*t  # intersection point
    is_inside = point_in_polygon(ri, poly_verts, pn)
    return ri, is_inside

def ray_x_sphere():
    pass

def main():
    ri = np.array([0.5, 0.0, 0.5])
    poly_verts = np.array([
        [ 0.0, 5.0, 0.0 ],
        [ 1.0, 5.0, 0.0 ],
        [ 1.0, 5.0, 1.0 ],
        [ 0.0, 5.0, 1.0 ],
    ])
    pn = np.array([0.0, 1.0, 0.0])
    point_in_polygon(ri, poly_verts, pn)

if __name__ == '__main__':
    main()
