from tinydb import Query, TinyDB
from tinydb.queries import QueryInstance
from tinydb.table import Document, Table


class TinyDatabase:
    db: TinyDB
    table: Table
    query_keys: list[str]

    def __init__(self, db_name: str, table_name: str, query_keys: list[str]) -> None:
        """Initialize the DAO with the database and table.

        Args:
            db_name (str): The name of the database.
            table_name (str): The name of the table.
            query_keys (list[str]): The list of query keys.
        """
        self.db = TinyDB(db_name, ensure_ascii=False, indent=4, encoding="utf-8")
        self.table = self.db.table(table_name, cache_size=None)
        self.query_keys = query_keys

    def generate_query(self, item: dict) -> QueryInstance:
        """Generate a query based on the provided item keys."""
        query = None
        for key in self.query_keys:
            if not query:
                query = Query()[key] == item[key]
            else:
                query = query & (Query()[key] == item[key])

        return query if query else Query()

    def create_one(self, item: dict) -> None:
        """Insert or update an item in the database.

        Args:
            item (dict[str, Any]): The item to be inserted or updated.
        """
        query: QueryInstance = self.generate_query(item)

        self.table.upsert(item, query)

    def find_by_id(self, item_keys: dict) -> dict | None:
        """Retrieve an item by its ID.

        Args:
            item_keys (dict[str, Any]): The keys of the item.

        Returns:
            Optional[Dict[str, Any]]: The retrieved item or None if not found.
        """
        query: QueryInstance = self.generate_query(item_keys)

        result: list[Document] = self.table.search(query)
        return result[0] if result else None

    def get_all(self) -> list[Document]:
        """Retrieve all items from the database.

        Returns:
            list[Document]: A list of all items.
        """
        return self.table.all()

    def drop_table(self) -> None:
        """Drop all data from table."""
        self.table.truncate()
