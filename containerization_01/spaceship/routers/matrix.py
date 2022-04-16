from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get('')
def matrix() -> dict:
    a = np.random.sample((10, 10))
    b = np.random.sample((10, 10))
    product = a.dot(b)
    a = np.array2string(a)
    b = np.array2string(b)
    product = np.array2string(product)
    return {'msg': { 'matrix_a': a, 'matrix_b': b, 'product': product }}