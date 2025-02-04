import psycopg2


class QueryGenerator:
    """
    To customize a query generator, you would implement/override the following functions:
    __init__: for initializing the question-specific parameters (eg credentials for the database).
    generate_query: implement your query generation logic given a question. add your secret sauce here!

    The following function(s) are implemented, as these are common across all query generators:
    exec_query: executes the query generated by generate_query; only postgres for now. It has
        an implicit dependency on self.db_creds and self.verbose from __init__.
    """

    def __init__(self, **kwargs):
        pass

    def generate_query(
        self,
        question: str,
        instructions: str,
        k_shot_prompt: str,
        glossary: str,
        table_metadata_string: str,
    ) -> dict:
        # generate a query given a question, instructions and k-shot prompt
        # any hard-coded logic, prompt-engineering, table-pruning, api calls etc
        # should be completely contained within this function
        # do add try-except blocks to catch any errors and return an empty string
        # these are the keys that you should store in the returned dict:
        # query: the generated query
        # reason: the reason for the query
        # err: the error message if any
        # any other fields you might want to track (eg tokens used in query, latency etc)
        pass

    def exec_query(self, query: str) -> str:
        """
        Tries to execute a query and returns an error message if unsuccessful
        This function implicitly relies on self.db_creds from init
        """
        if self.db_type != "postgres":
            raise ValueError("Only postgres is supported for now")
        try:
            self.conn = psycopg2.connect(**self.db_creds)
            self.cur = self.conn.cursor()
            self.cur.execute(query)
            _ = self.cur.fetchall()
            self.cur.close()
            self.conn.close()
            return ""
        except Exception as e:
            if self.verbose:
                print(f"Error while executing query:\n{type(e)}, {e}")
            # cleanup connections
            if self.cur:
                self.cur.close()
            if self.conn:
                self.conn.close()
            return str(e)
