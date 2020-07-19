from airflow.plugins_manager import AirflowPlugin

# import helpers
import operators


# Defining the plugin class
class ETLPlugin(AirflowPlugin):
    name = "etl_plugin"
    operators = [
        operators.CreateTablesOperator,
        operators.CSVToTableOperator,
    ]
    # helpers = [
    #     helpers.read_sql
    # ]
