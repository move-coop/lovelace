# lovelace
Ada Lovelace was a pioneer of computer programming.

Read more about [here](https://en.wikipedia.org/wiki/Ada_Lovelace)

## Container Script Users
### utils.py
We recommend members copy this file into their own Github repository.

There are two key functions in this script:
1. `logger()`: This is simply a standard logger TMC often leverages
2. `setup_environment():` Given our commonly used naming conventions of Civis Platform
    parameters, this will automatically pull in the necessary credentials for the 
    Parson's GoogleBigQuery Class. You must include the two required parameters in the
    BigQuery Template Script below.

### BigQuery Template
Members can clone [this template script](https://platform.civisanalytics.com/spa/#/scripts/containers/256194736).

It includes two required parameters for using TMC's BigQuery:
- GOOGLE APPLICATION CREDENTIALS: Each member has their own in the dropdown formatted as 
    `{member_code} GCP Service Account JSON`
- GOOGLE CLOUD STORAGE BUCKET: Members will need to write in their own formatted as
    `bkt-tmc-mem-{member_code}-scratch`
