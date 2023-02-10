import uvicorn

from orm_model import test_db_connection
from recount_statistic import recount_statistic

if __name__ == "__main__":
    if test_db_connection():
        recount_statistic()
        uvicorn.run("webserv:app", host="127.0.0.1", port=8080, log_level="info")
