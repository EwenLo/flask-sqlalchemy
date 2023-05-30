import sqlalchemy
import sqlalchemy.orm


class SQLAlchemy:
    ##############################
    ### Sqlalchemy Sub Classes ###
    ##############################
    class ARRAY(sqlalchemy.ARRAY):
        pass

    class AdaptedConnection(sqlalchemy.AdaptedConnection):
        pass

    class Alias(sqlalchemy.Alias):
        pass

    class AliasedReturnsRows(sqlalchemy.AliasedReturnsRows):
        pass

    class AssertionPool(sqlalchemy.AssertionPool):
        pass

    class AsyncAdaptedQueuePool(sqlalchemy.AsyncAdaptedQueuePool):
        pass

    class BIGINT(sqlalchemy.BIGINT):
        pass

    class BINARY(sqlalchemy.BINARY):
        pass

    class BLOB(sqlalchemy.BLOB):
        pass

    class BOOLEAN(sqlalchemy.BOOLEAN):
        pass

    class BaseDDLElement(sqlalchemy.BaseDDLElement):
        pass

    class BaseRow(sqlalchemy.BaseRow):
        pass

    class BigInteger(sqlalchemy.BigInteger):
        pass

    class BinaryExpression(sqlalchemy.BinaryExpression):
        pass

    class BindParameter(sqlalchemy.BindParameter):
        pass

    class BindTyping(sqlalchemy.BindTyping):
        pass

    class Boolean(sqlalchemy.Boolean):
        pass

    class BooleanClauseList(sqlalchemy.BooleanClauseList):
        pass

    class CHAR(sqlalchemy.CHAR):
        pass

    class CLOB(sqlalchemy.CLOB):
        pass

    class CTE(sqlalchemy.CTE):
        pass

    class CacheKey(sqlalchemy.CacheKey):
        pass

    class Case(sqlalchemy.Case):
        pass

    class Cast(sqlalchemy.Cast):
        pass

    class CheckConstraint(sqlalchemy.CheckConstraint):
        pass

    class ChunkedIteratorResult(sqlalchemy.ChunkedIteratorResult):
        pass

    class ClauseElement(sqlalchemy.ClauseElement):
        pass

    class ClauseList(sqlalchemy.ClauseList):
        pass

    class CollectionAggregate(sqlalchemy.CollectionAggregate):
        pass

    class Column(sqlalchemy.Column):
        pass

    class ColumnClause(sqlalchemy.ColumnClause):
        pass

    class ColumnCollection(sqlalchemy.ColumnCollection):
        pass

    class ColumnDefault(sqlalchemy.ColumnDefault):
        pass

    class ColumnElement(sqlalchemy.ColumnElement):
        pass

    class ColumnOperators(sqlalchemy.ColumnOperators):
        pass

    class Compiled(sqlalchemy.Compiled):
        pass

    class CompoundSelect(sqlalchemy.CompoundSelect):
        pass

    class Computed(sqlalchemy.Computed):
        pass

    class Connection(sqlalchemy.Connection):
        pass

    class Constraint(sqlalchemy.Constraint):
        pass

    class CreateEnginePlugin(sqlalchemy.CreateEnginePlugin):
        pass

    class CursorResult(sqlalchemy.CursorResult):
        pass

    class DATE(sqlalchemy.DATE):
        pass

    class DATETIME(sqlalchemy.DATETIME):
        pass

    class DDL(sqlalchemy.DDL):
        pass

    class DDLElement(sqlalchemy.DDLElement):
        pass

    class DECIMAL(sqlalchemy.DECIMAL):
        pass

    class DOUBLE(sqlalchemy.DOUBLE):
        pass

    class Date(sqlalchemy.Date):
        pass

    class DateTime(sqlalchemy.DateTime):
        pass

    class DefaultClause(sqlalchemy.DefaultClause):
        pass

    class Delete(sqlalchemy.Delete):
        pass

    class Dialect(sqlalchemy.Dialect):
        pass

    class Double(sqlalchemy.Double):
        pass

    class Engine(sqlalchemy.Engine):
        pass

    class Enum(sqlalchemy.Enum):
        pass

    class ExceptionContext(sqlalchemy.ExceptionContext):
        pass

    class Executable(sqlalchemy.Executable):
        pass

    class ExecutableDDLElement(sqlalchemy.ExecutableDDLElement):
        pass

    class ExecutionContext(sqlalchemy.ExecutionContext):
        pass

    class Exists(sqlalchemy.Exists):
        pass

    class Extract(sqlalchemy.Extract):
        pass

    class FLOAT(sqlalchemy.FLOAT):
        pass

    class FallbackAsyncAdaptedQueuePool(sqlalchemy.FallbackAsyncAdaptedQueuePool):
        pass

    class FetchedValue(sqlalchemy.FetchedValue):
        pass

    class Float(sqlalchemy.Float):
        pass

    class ForeignKey(sqlalchemy.ForeignKey):
        pass

    class ForeignKeyConstraint(sqlalchemy.ForeignKeyConstraint):
        pass

    class FromClause(sqlalchemy.FromClause):
        pass

    class FromGrouping(sqlalchemy.FromGrouping):
        pass

    class FrozenResult(sqlalchemy.FrozenResult):
        pass

    class Function(sqlalchemy.Function):
        pass

    class FunctionElement(sqlalchemy.FunctionElement):
        pass

    class FunctionFilter(sqlalchemy.FunctionFilter):
        pass

    class GenerativeSelect(sqlalchemy.GenerativeSelect):
        pass

    class Grouping(sqlalchemy.Grouping):
        pass

    class HasCTE(sqlalchemy.HasCTE):
        pass

    class HasPrefixes(sqlalchemy.HasPrefixes):
        pass

    class HasSuffixes(sqlalchemy.HasSuffixes):
        pass

    class INT(sqlalchemy.INT):
        pass

    class INTEGER(sqlalchemy.INTEGER):
        pass

    class Identity(sqlalchemy.Identity):
        pass

    class Index(sqlalchemy.Index):
        pass

    class Insert(sqlalchemy.Insert):
        pass

    class Inspector(sqlalchemy.Inspector):
        pass

    class Integer(sqlalchemy.Integer):
        pass

    class Interval(sqlalchemy.Interval):
        pass

    class IteratorResult(sqlalchemy.IteratorResult):
        pass

    class JSON(sqlalchemy.JSON):
        pass

    class Join(sqlalchemy.Join):
        pass

    class Label(sqlalchemy.Label):
        pass

    class LambdaElement(sqlalchemy.LambdaElement):
        pass

    class LargeBinary(sqlalchemy.LargeBinary):
        pass

    class Lateral(sqlalchemy.Lateral):
        pass

    class MappingResult(sqlalchemy.MappingResult):
        pass

    class MergedResult(sqlalchemy.MergedResult):
        pass

    class MetaData(sqlalchemy.MetaData):
        pass

    class NCHAR(sqlalchemy.NCHAR):
        pass

    class NUMERIC(sqlalchemy.NUMERIC):
        pass

    class NVARCHAR(sqlalchemy.NVARCHAR):
        pass

    class NestedTransaction(sqlalchemy.NestedTransaction):
        pass

    class Null(sqlalchemy.Null):
        pass

    class NullPool(sqlalchemy.NullPool):
        pass

    class Numeric(sqlalchemy.Numeric):
        pass

    class Operators(sqlalchemy.Operators):
        pass

    class Over(sqlalchemy.Over):
        pass

    class PickleType(sqlalchemy.PickleType):
        pass

    class Pool(sqlalchemy.Pool):
        pass

    class PoolProxiedConnection(sqlalchemy.PoolProxiedConnection):
        pass

    class PoolResetState(sqlalchemy.PoolResetState):
        pass

    class PrimaryKeyConstraint(sqlalchemy.PrimaryKeyConstraint):
        pass

    class QueuePool(sqlalchemy.QueuePool):
        pass

    class REAL(sqlalchemy.REAL):
        pass

    class ReleaseSavepointClause(sqlalchemy.ReleaseSavepointClause):
        pass

    class Result(sqlalchemy.Result):
        pass

    class ResultProxy(sqlalchemy.ResultProxy):
        pass

    class ReturnsRows(sqlalchemy.ReturnsRows):
        pass

    class RollbackToSavepointClause(sqlalchemy.RollbackToSavepointClause):
        pass

    class RootTransaction(sqlalchemy.RootTransaction):
        pass

    class Row(sqlalchemy.Row):
        pass

    class RowMapping(sqlalchemy.RowMapping):
        pass

    class SMALLINT(sqlalchemy.SMALLINT):
        pass

    class SQLColumnExpression(sqlalchemy.SQLColumnExpression):
        pass

    class SavepointClause(sqlalchemy.SavepointClause):
        pass

    class ScalarResult(sqlalchemy.ScalarResult):
        pass

    class ScalarSelect(sqlalchemy.ScalarSelect):
        pass

    class Select(sqlalchemy.Select):
        pass

    class SelectBase(sqlalchemy.SelectBase):
        pass

    class SelectLabelStyle(sqlalchemy.SelectLabelStyle):
        pass

    class Selectable(sqlalchemy.Selectable):
        pass

    class Sequence(sqlalchemy.Sequence):
        pass

    class SingleonThreadPool(sqlalchemy.SingleonThreadPool):
        pass

    class SmallInteger(sqlalchemy.SmallInteger):
        pass

    class StatementLambdaElement(sqlalchemy.StatementLambdaElement):
        pass

    class StaticPool(sqlalchemy.StaticPool):
        pass

    class String(sqlalchemy.String):
        pass

    class Subquery(sqlalchemy.Subquery):
        pass

    class TEXT(sqlalchemy.TEXT):
        pass

    class TIME(sqlalchemy.TIME):
        pass

    class TIMESTAMP(sqlalchemy.TIMESTAMP):
        pass

    class Table(sqlalchemy.Table):
        pass

    class TableClause(sqlalchemy.TableClause):
        pass

    class TableSample(sqlalchemy.TableSample):
        pass

    class TableValuedAlias(sqlalchemy.TableValuedAlias):
        pass

    class Text(sqlalchemy.Text):
        pass

    class TextAsFrom(sqlalchemy.TextAsFrom):
        pass

    class TextClause(sqlalchemy.TextClause):
        pass

    class TextualSelect(sqlalchemy.TextualSelect):
        pass

    class Time(sqlalchemy.Time):
        pass

    class Transaction(sqlalchemy.Transaction):
        pass

    class TryCast(sqlalchemy.TryCast):
        pass

    class Tuple(sqlalchemy.Tuple):
        pass

    class TupleType(sqlalchemy.TupleType):
        pass

    class TwoPhaseTransaction(sqlalchemy.TwoPhaseTransaction):
        pass

    class TypeClause(sqlalchemy.TypeClause):
        pass

    class TypeCoerce(sqlalchemy.TypeCoerce):
        pass

    class TypeCompiler(sqlalchemy.TypeCompiler):
        pass

    class TypeDecorator(sqlalchemy.TypeDecorator):
        pass

    class URL(sqlalchemy.URL):
        pass

    class UUID(sqlalchemy.UUID):
        pass

    class UnaryExpression(sqlalchemy.UnaryExpression):
        pass

    class Unicode(sqlalchemy.Unicode):
        pass

    class UnicodeText(sqlalchemy.UnicodeText):
        pass

    class UniqueConstraint(sqlalchemy.UniqueConstraint):
        pass

    class Update(sqlalchemy.Update):
        pass

    class UpdateBase(sqlalchemy.UpdateBase):
        pass

    class Uuid(sqlalchemy.Uuid):
        pass

    class VARBINARY(sqlalchemy.VARBINARY):
        pass

    class VARCHAR(sqlalchemy.VARCHAR):
        pass

    class Values(sqlalchemy.Values):
        pass

    class ValuesBase(sqlalchemy.ValuesBase):
        pass

    class Visitable(sqlalchemy.Visitable):
        pass

    class WithinGroup(sqlalchemy.WithinGroup):
        pass

    class alias(sqlalchemy.alias):
        pass

    class asc(sqlalchemy.asc):
        pass

    class between(sqlalchemy.between):
        pass

    class bindparam(sqlalchemy.bindparam):
        pass

    class case(sqlalchemy.case):
        pass

    class cast(sqlalchemy.cast):
        pass

    class collate(sqlalchemy.collate):
        pass

    class column(sqlalchemy.column):
        pass

    class cte(sqlalchemy.cte):
        pass

    class delete(sqlalchemy.delete):
        pass

    class desc(sqlalchemy.desc):
        pass

    class distinct(sqlalchemy.distinct):
        pass

    class exists(sqlalchemy.exists):
        pass

    class extract(sqlalchemy.extract):
        pass

    class false(sqlalchemy.false):
        pass

    class func(sqlalchemy.func):
        pass

    class funcfilter(sqlalchemy.funcfilter):
        pass

    class insert(sqlalchemy.insert):
        pass

    class inspect(sqlalchemy.inspect):
        pass

    class intersect(sqlalchemy.intersect):
        pass

    class join(sqlalchemy.join):
        pass

    class label(sqlalchemy.label):
        pass

    class lateral(sqlalchemy.lateral):
        pass

    class literal(sqlalchemy.literal):
        pass

    class modifier(sqlalchemy.modifier):
        pass

    class null(sqlalchemy.null):
        pass

    class nullsfirst(sqlalchemy.nullsfirst):
        pass

    class nullslast(sqlalchemy.nullslast):
        pass

    class outerjoin(sqlalchemy.outerjoin):
        pass

    class outparam(sqlalchemy.outparam):
        pass

    class over(sqlalchemy.over):
        pass

    class select(sqlalchemy.select):
        pass

    class table(sqlalchemy.table):
        pass

    class tablesample(sqlalchemy.tablesample):
        pass

    class text(sqlalchemy.text):
        pass

    class true(sqlalchemy.true):
        pass

    class union(sqlalchemy.union):
        pass

    class update(sqlalchemy.update):
        pass

    class values(sqlalchemy.values):
        pass

    ##################################
    ### Sqlalchemy ORM Sub Classes ###
    ##################################
    class AliasOption(sqlalchemy.orm.AliasOption):
        pass

    class AppenderQuery(sqlalchemy.orm.AppenderQuery):
        pass

    class AttributeEventToken(sqlalchemy.orm.AttributeEventToken):
        pass

    class AttributeEvents(sqlalchemy.orm.AttributeEvents):
        pass

    class AttributeState(sqlalchemy.orm.AttributeState):
        pass

    class Bundle(sqlalchemy.orm.Bundle):
        pass

    class CascadeOptions(sqlalchemy.orm.CascadeOptions):
        pass

    class ClassManager(sqlalchemy.orm.ClassManager):
        pass

    class ColumnProperty(sqlalchemy.orm.ColumnProperty):
        pass

    class Composite(sqlalchemy.orm.Composite):
        pass

    class CompositeProperty(sqlalchemy.orm.CompositeProperty):
        pass

    class DeclarativeBase(sqlalchemy.orm.DeclarativeBase):
        pass

    class DeclarativeBaseNoMeta(sqlalchemy.orm.DeclarativeBaseNoMeta):
        pass

    class DeclarativeMeta(sqlalchemy.orm.DeclarativeMeta):
        pass

    class DynamicMapped(sqlalchemy.orm.DynamicMapped):
        pass

    class FromStatement(sqlalchemy.orm.FromStatement):
        pass

    class IdentityMap(sqlalchemy.orm.IdentityMap):
        pass

    class InspectionAttr(sqlalchemy.orm.InspectionAttr):
        pass

    class InspectionAttrExtensionType(sqlalchemy.orm.InspectionAttrExtensionType):
        pass

    class InspectionAttrInfo(sqlalchemy.orm.InspectionAttrInfo):
        pass

    class InstanceEvents(sqlalchemy.orm.InstanceEvents):
        pass

    class InstanceState(sqlalchemy.orm.InstanceState):
        pass

    class InstrumentationEvents(sqlalchemy.orm.InstrumentationEvents):
        pass

    class InstrumentedAttribute(sqlalchemy.orm.InstrumentedAttribute):
        pass

    class KeyFuncDict(sqlalchemy.orm.KeyFuncDict):
        pass

    class Load(sqlalchemy.orm.Load):
        pass

    class LoaderCallableStatus(sqlalchemy.orm.LoaderCallableStatus):
        pass

    class LoaderCriteriaOption(sqlalchemy.orm.LoaderCriteriaOption):
        pass

    class MANYTOMANY(sqlalchemy.orm.MANYTOMANY):
        pass

    class MANYTOONE(sqlalchemy.orm.MANYTOONE):
        pass

    class Mapped(sqlalchemy.orm.Mapped):
        pass

    class MappedAsDataclass(sqlalchemy.orm.MappedAsDataclass):
        pass

    class MappedClassProtocol(sqlalchemy.orm.MappedClassProtocol):
        pass

    class MappedCollection(sqlalchemy.orm.MappedCollection):
        pass

    class MappedColumn(sqlalchemy.orm.MappedColumn):
        pass

    class MappedSQLExpression(sqlalchemy.orm.MappedSQLExpression):
        pass

    class Mapper(sqlalchemy.orm.Mapper):
        pass

    class MapperEvents(sqlalchemy.orm.MapperEvents):
        pass

    class MapperProperty(sqlalchemy.orm.MapperProperty):
        pass

    class NotExtension(sqlalchemy.orm.NotExtension):
        pass

    class ONETOMANY(sqlalchemy.orm.ONETOMANY):
        pass

    class ORMDescriptor(sqlalchemy.orm.ORMDescriptor):
        pass

    class ORMExecuteState(sqlalchemy.orm.ORMExecuteState):
        pass

    class PassiveFlag(sqlalchemy.orm.PassiveFlag):
        pass

    class PropComparator(sqlalchemy.orm.PropComparator):
        pass

    class Query(sqlalchemy.orm.Query):
        pass

    class QueryContext(sqlalchemy.orm.QueryContext):
        pass

    class QueryEvents(sqlalchemy.orm.QueryEvents):
        pass

    class QueryPropertyDescriptor(sqlalchemy.orm.QueryPropertyDescriptor):
        pass

    class QueryableAttribute(sqlalchemy.orm.QueryableAttribute):
        pass

    class Relationship(sqlalchemy.orm.Relationship):
        pass

    class RelationshipDirection(sqlalchemy.orm.RelationshipDirection):
        pass

    class RelationshipProperty(sqlalchemy.orm.RelationshipProperty):
        pass

    class SQLORMExpression(sqlalchemy.orm.SQLORMExpression):
        pass

    class Session(sqlalchemy.orm.Session):
        pass

    class SessionEvents(sqlalchemy.orm.SessionEvents):
        pass

    class SessionTransaction(sqlalchemy.orm.SessionTransaction):
        pass

    class SessionTransactionOrigin(sqlalchemy.orm.SessionTransactionOrigin):
        pass

    class Synonym(sqlalchemy.orm.Synonym):
        pass

    class SynonymProperty(sqlalchemy.orm.SynonymProperty):
        pass

    class UOWTransaction(sqlalchemy.orm.UOWTransaction):
        pass

    class UserDefinedOption(sqlalchemy.orm.UserDefinedOption):
        pass

    class WriteOnlyCollection(sqlalchemy.orm.WriteOnlyCollection):
        pass

    class WriteOnlyMapped(sqlalchemy.orm.WriteOnlyMapped):
        pass

    class aliased(sqlalchemy.orm.aliased):
        pass

    class backref(sqlalchemy.orm.backref):
        pass

    class composite(sqlalchemy.orm.composite):
        pass

    class defaultload(sqlalchemy.orm.defaultload):
        pass

    class defer(sqlalchemy.orm.defer):
        pass

    class deferred(sqlalchemy.orm.deferred):
        pass

    class foreign(sqlalchemy.orm.foreign):
        pass

    class immediateload(sqlalchemy.orm.immediateload):
        pass

    class join(sqlalchemy.orm.join):
        pass

    class joinedload(sqlalchemy.orm.joinedload):
        pass

    class lazyload(sqlalchemy.orm.lazyload):
        pass

    class mapper(sqlalchemy.orm.mapper):
        pass

    class noload(sqlalchemy.orm.noload):
        pass

    class outerjoin(sqlalchemy.orm.outerjoin):
        pass

    class raiseload(sqlalchemy.orm.raiseload):
        pass

    class reconstructor(sqlalchemy.orm.reconstructor):
        pass

    class registry(sqlalchemy.orm.registry):
        pass

    class relationship(sqlalchemy.orm.relationship):
        pass

    class remote(sqlalchemy.orm.remote):
        pass

    class selectinload(sqlalchemy.orm.selectinload):
        pass

    class sessionmaker(sqlalchemy.orm.sessionmaker):
        pass

    class subqueryload(sqlalchemy.orm.subqueryload):
        pass

    class synonym(sqlalchemy.orm.synonym):
        pass

    class undefer(sqlalchemy.orm.undefer):
        pass

    class validates(sqlalchemy.orm.validates):
        pass
