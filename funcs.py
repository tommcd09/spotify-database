def print_rows(cursor):
    """Takes a SQLite cursor, fetches all rows and prints them line by line."""
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("No results")
    else:
        for row in rows:
            print(row)


def execute_print(query, cursor):
    """Takes a SQLite query and cursor, executes and prints rows line by line."""
    cursor.execute(query)
    print_rows(cursor)


def split_explode(df, col, delimiter):
    """Takes a DataFrame, column, and delimiter, splits column
    at delimiter and explodes rows.
    """
    df[col] = [item.split(delimiter) for item in df[col]]
    df = df.explode(col, ignore_index=True)
    return df
