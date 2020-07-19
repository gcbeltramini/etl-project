COPY {schema_name:s}.{table_name:s}
FROM '{file_name:s}'
WITH (
  FORMAT csv,
  DELIMITER '{delimiter_char:s}',
  HEADER TRUE,
  ENCODING 'utf-8'
  );
