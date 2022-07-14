from pandas.compat._optional import (
    import_optional_dependency as import_optional_dependency,
)
from pandas.core.accessor import (
    PandasDelegate as PandasDelegate,
    delegate_names as delegate_names,
)
from pandas.core.arrays.sparse.array import SparseArray as SparseArray
from pandas.core.arrays.sparse.dtype import SparseDtype as SparseDtype
from pandas.core.dtypes.cast import find_common_type as find_common_type

class BaseAccessor:
    def __init__(self, data=...) -> None: ...

class SparseAccessor(BaseAccessor, PandasDelegate):
    @classmethod
    def from_coo(cls, A, dense_index: bool = ...): ...
    def to_coo(self, row_levels=..., column_levels=..., sort_labels: bool = ...): ...
    def to_dense(self): ...

class SparseFrameAccessor(BaseAccessor, PandasDelegate):
    @classmethod
    def from_spmatrix(cls, data, index=..., columns=...): ...
    def to_dense(self): ...
    def to_coo(self): ...
    @property
    def density(self) -> float: ...
