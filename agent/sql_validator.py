
import sqlglot
from sqlglot import exp


ALLOWED_STATEMENTS = (
    exp.Select,
    exp.Union,
)


def validate_sql(query: str) -> bool:

    try:
        statements = sqlglot.parse(query, read="sqlite")

        # Reject empty or multiple statements
        if len(statements) != 1 or statements[0] is None:
            return False

        statement = statements[0]

        # Allow only SELECT and UNION queries
        if not isinstance(statement, ALLOWED_STATEMENTS):
            return False

        # Reject SELECT INTO
        if statement.find(exp.Into):
            return False

        return True

    except sqlglot.errors.ParseError:
        return False
