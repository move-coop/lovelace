# Civis Client Migration

Some members previously leveraged the Civis Python client to move data in and out of
Redshift. We strongly recommend moving to Parsons. Below, we translate some commonly
used functions.

In order to use the suggested functions, it's key that you copy `setup_environment()` 
into your Github repository, and make sure to use the `template_container_script.py`.

## Pandas to Parsons Tables
Most indivudals using the Civis Python client were leveraging Pandas in Python. Parsons,
TMC's package of choice, uses Parsons tables, which are based on petl. 

https://move-coop.github.io/parsons/html/stable/table.html

When you query BigQuery using Parsons, the output will be a Parsons Table. If you are
more comfortable using Pandas, you can transform a Parsons Table into a dataframe:
https://move-coop.github.io/parsons/html/stable/table.html#parsons.etl.tofrom.ToFrom.to_dataframe

## Translations

`civis.io.read_civis_sql(sql, database="TMC", use_pandas=True)` > `db.query(sql)`
`export_to_civis_file` > `tbl.to_csv()` # tbl being a Parsons Table
`base.EmptyResultError` > `if tbl.num_rows==0` # Parsons will deliver a tbl with 0 rows

### Keep Using
`civis_to_file`
`dataframe_to_file` 

## Civis Client
The Civis API can otherwise be used to trigger various Civis objects, be that scripts, 
workflows, etc. 