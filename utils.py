import os
import logging
import json

logger = logging.getLogger(__name__)
_handler = logging.StreamHandler()
_formatter = logging.Formatter('%(levelname)s %(message)s')
_handler.setFormatter(_formatter)
logger.addHandler(_handler)
logger.setLevel('INFO')

def setup_environment():
    """
    Sets up environment variables used for Parsons classes.

    The Civis Container script should include the following parameters:
    - GOOGLE_APPLICATION_CREDENTIALS: {member_code} GCP Service Account JSON
    - GCS_BUCKET: bkt-tmc-mem-{member_code}-scratch
    """
    
    json_format_app_cred=json.loads(os.environ.get(f"GOOGLE_APPLICATION_CREDENTIALS_PASSWORD"),strict=False)
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json.dumps(json_format_app_cred)
    os.environ['GCS_TEMP_BUCKET'] = os.environ.get('GCS_BUCKET')

    return None