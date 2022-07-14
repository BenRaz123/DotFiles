import datetime
import sys
from decimal import Decimal
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, Sequence, Set, Tuple, Type, TypeVar, Union

from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models import Q
from django.db.models.fields import Field
from django.db.models.lookups import Lookup, Transform
from django.db.models.query import QuerySet
from django.db.models.sql.compiler import SQLCompiler, _AsSqlType
from django.db.models.sql.query import Query

if sys.version_info < (3, 8):
    from typing_extensions import Literal
else:
    from typing import Literal

class SQLiteNumericMixin:
    def as_sqlite(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...

_Self = TypeVar("_Self")
_Numeric = Union[float, Decimal]

class Combinable:
    ADD: str = ...
    SUB: str = ...
    MUL: str = ...
    DIV: str = ...
    POW: str = ...
    MOD: str = ...
    BITAND: str = ...
    BITOR: str = ...
    BITLEFTSHIFT: str = ...
    BITRIGHTSHIFT: str = ...
    BITXOR: str = ...
    def __neg__(self) -> CombinedExpression: ...
    def __add__(self, other: Optional[Union[datetime.timedelta, Combinable, _Numeric, str]]) -> CombinedExpression: ...
    def __sub__(self, other: Union[datetime.timedelta, Combinable, _Numeric]) -> CombinedExpression: ...
    def __mul__(self, other: Union[datetime.timedelta, Combinable, _Numeric]) -> CombinedExpression: ...
    def __truediv__(self, other: Union[Combinable, _Numeric]) -> CombinedExpression: ...
    def __mod__(self, other: Union[int, Combinable]) -> CombinedExpression: ...
    def __pow__(self, other: Union[_Numeric, Combinable]) -> CombinedExpression: ...
    def __and__(self, other: Union[Combinable, Q]) -> Q: ...
    def bitand(self, other: int) -> CombinedExpression: ...
    def bitleftshift(self, other: int) -> CombinedExpression: ...
    def bitrightshift(self, other: int) -> CombinedExpression: ...
    def bitxor(self, other: int) -> CombinedExpression: ...
    def __or__(self, other: Union[Combinable, Q]) -> Q: ...
    def bitor(self, other: int) -> CombinedExpression: ...
    def __radd__(self, other: Optional[Union[datetime.datetime, _Numeric, Combinable]]) -> CombinedExpression: ...
    def __rsub__(self, other: Union[_Numeric, Combinable]) -> CombinedExpression: ...
    def __rmul__(self, other: Union[_Numeric, Combinable]) -> CombinedExpression: ...
    def __rtruediv__(self, other: Union[_Numeric, Combinable]) -> CombinedExpression: ...
    def __rmod__(self, other: Union[int, Combinable]) -> CombinedExpression: ...
    def __rpow__(self, other: Union[_Numeric, Combinable]) -> CombinedExpression: ...
    def __rand__(self, other: Any) -> Combinable: ...
    def __ror__(self, other: Any) -> Combinable: ...

_SelfB = TypeVar("_SelfB", bound="BaseExpression")

class BaseExpression:
    is_summary: bool = ...
    filterable: bool = ...
    window_compatible: bool = ...
    def __init__(self, output_field: Optional[Field] = ...) -> None: ...
    def get_db_converters(self, connection: BaseDatabaseWrapper) -> List[Callable]: ...
    def get_source_expressions(self) -> List[Any]: ...
    def set_source_expressions(self, exprs: Sequence[Combinable]) -> None: ...
    @property
    def contains_aggregate(self) -> bool: ...
    @property
    def contains_over_clause(self) -> bool: ...
    @property
    def contains_column_references(self) -> bool: ...
    def resolve_expression(
        self: _SelfB,
        query: Any = ...,
        allow_joins: bool = ...,
        reuse: Optional[Set[str]] = ...,
        summarize: bool = ...,
        for_save: bool = ...,
    ) -> _SelfB: ...
    @property
    def conditional(self) -> bool: ...
    @property
    def field(self) -> Field: ...
    @property
    def output_field(self) -> Field: ...
    @property
    def convert_value(self) -> Callable: ...
    def get_lookup(self, lookup: str) -> Optional[Type[Lookup]]: ...
    def get_transform(self, name: str) -> Optional[Type[Transform]]: ...
    def relabeled_clone(self: _SelfB, change_map: Dict[Optional[str], str]) -> _SelfB: ...
    def copy(self: _SelfB) -> _SelfB: ...
    def get_group_by_cols(self: _SelfB, alias: Optional[str] = ...) -> List[_SelfB]: ...
    def get_source_fields(self) -> List[Optional[Field]]: ...
    def asc(self, **kwargs: Any) -> OrderBy: ...
    def desc(self, **kwargs: Any) -> OrderBy: ...
    def reverse_ordering(self) -> BaseExpression: ...
    def flatten(self) -> Iterator[BaseExpression]: ...
    def as_sql(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper) -> Any: ...
    def deconstruct(self) -> Any: ...  # fake

class Expression(BaseExpression, Combinable): ...

class CombinedExpression(SQLiteNumericMixin, Expression):
    connector: str = ...
    lhs: Combinable = ...
    rhs: Combinable = ...
    def __init__(
        self, lhs: Combinable, connector: str, rhs: Combinable, output_field: Optional[Field] = ...
    ) -> None: ...

class F(Combinable):
    name: str
    def __init__(self, name: str): ...
    def resolve_expression(
        self,
        query: Any = ...,
        allow_joins: bool = ...,
        reuse: Optional[Set[str]] = ...,
        summarize: bool = ...,
        for_save: bool = ...,
    ) -> F: ...
    def asc(self, **kwargs) -> OrderBy: ...
    def desc(self, **kwargs) -> OrderBy: ...
    def deconstruct(self) -> Any: ...  # fake

class ResolvedOuterRef(F): ...

class OuterRef(F):
    contains_aggregate: bool
    def resolve_expression(self, *args: Any, **kwargs: Any) -> ResolvedOuterRef: ...
    def relabeled_clone(self: _Self, relabels: Any) -> _Self: ...

class Subquery(BaseExpression, Combinable):
    template: str = ...
    query: Query = ...
    extra: Dict[Any, Any] = ...
    def __init__(self, queryset: Union[Query, QuerySet], output_field: Optional[Field] = ..., **extra: Any) -> None: ...

class Exists(Subquery):
    negated: bool = ...
    def __init__(self, queryset: Union[Query, QuerySet], negated: bool = ..., **kwargs: Any) -> None: ...
    def __invert__(self) -> Exists: ...

class OrderBy(Expression):
    template: str = ...
    nulls_first: bool = ...
    nulls_last: bool = ...
    descending: bool = ...
    expression: Union[Expression, F, Subquery] = ...
    def __init__(
        self,
        expression: Union[Expression, F, Subquery],
        descending: bool = ...,
        nulls_first: bool = ...,
        nulls_last: bool = ...,
    ) -> None: ...

class Value(Expression):
    value: Any = ...
    def __init__(self, value: Any, output_field: Optional[Field] = ...) -> None: ...

class RawSQL(Expression):
    params: List[Any]
    sql: str
    def __init__(self, sql: str, params: Sequence[Any], output_field: Optional[Field] = ...) -> None: ...

class Func(SQLiteNumericMixin, Expression):
    function: str = ...
    name: str = ...
    template: str = ...
    arg_joiner: str = ...
    arity: Optional[int] = ...
    source_expressions: List[Expression] = ...
    extra: Dict[Any, Any] = ...
    def __init__(self, *expressions: Any, output_field: Optional[Field] = ..., **extra: Any) -> None: ...

class When(Expression):
    template: str = ...
    condition: Any = ...
    result: Any = ...
    def __init__(self, condition: Any = ..., then: Any = ..., **lookups: Any) -> None: ...

class Case(Expression):
    template: str = ...
    case_joiner: str = ...
    cases: Any = ...
    default: Any = ...
    extra: Any = ...
    def __init__(
        self, *cases: Any, default: Optional[Any] = ..., output_field: Optional[Field] = ..., **extra: Any
    ) -> None: ...

class ExpressionWrapper(Expression):
    def __init__(self, expression: Union[Q, Combinable], output_field: Field): ...

class Col(Expression):
    target: Field
    alias: str
    contains_column_references: Literal[True] = ...
    possibly_multivalued: Literal[False] = ...
    def __init__(self, alias: str, target: Field, output_field: Optional[Field] = ...): ...

class Ref(Expression):
    def __init__(self, refs: str, source: Expression): ...

class ExpressionList(Func):
    def __init__(self, *expressions: Union[BaseExpression, Combinable], **extra: Any) -> None: ...

class Window(SQLiteNumericMixin, Expression):
    template: str = ...
    contains_aggregate: bool = ...
    contains_over_clause: bool = ...
    partition_by: Optional[ExpressionList]
    order_by: Optional[ExpressionList]
    def __init__(
        self,
        expression: BaseExpression,
        partition_by: Optional[Union[str, Iterable[Union[BaseExpression, F]], F, BaseExpression]] = ...,
        order_by: Optional[Union[Sequence[Union[BaseExpression, F]], Union[BaseExpression, F]]] = ...,
        frame: Optional[WindowFrame] = ...,
        output_field: Optional[Field] = ...,
    ) -> None: ...

class WindowFrame(Expression):
    template: str = ...
    frame_type: str = ...
    def __init__(self, start: Optional[int] = ..., end: Optional[int] = ...) -> None: ...
    def window_frame_start_end(
        self, connection: BaseDatabaseWrapper, start: Optional[int], end: Optional[int]
    ) -> Tuple[int, int]: ...

class RowRange(WindowFrame): ...
class ValueRange(WindowFrame): ...