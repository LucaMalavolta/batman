from . import _rsky

__all__ = ["detect"]


def detect():
    """Return whether batman's extensions were built with OpenMP support."""
    return _rsky._openmp_enabled()
