# https://platform.civisanalytics.com/spa/#/scripts/containers/256194736

from utils import logger, setup_environment
from parsons import GoogleBigQuery, Table
import civis

def main(db: GoogleBigQuery, client: civis.APIClient):
	
    script_id = 12345
    sql = client.scripts.get_sql(script_id)
    db.query(sql)


if __name__ == "__main__":
	setup_environment()
	db = GoogleBigQuery()
	client = civis.APIClient()

	main(db=db, client=client)