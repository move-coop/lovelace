# https://platform.civisanalytics.com/spa/#/scripts/containers/256194736

from utils import logger, setup_environment
from parsons import GoogleBigQuery, Table

def main(db: GoogleBigQuery):

	db.query("select * from dataset.table")


if __name__ == "__main__":
	setup_environment()
	db = GoogleBigQuery()
	main(db=db)