# PIP Install Depended Modules
pip3 install -r requirements.txt -t .

# Run Python script
python3 csv-reader.py

# Transformation Configuration
```
logConfig: logger.yaml                  # Log config file path
networks:
- name: nma                             # Name of the network device
  lineDelimiter: '/n'                   # Default set in python already no need use this property
  fieldDelimiter: '|'                   # Field delimiter for a row
  header: TRUE|FALSE                    # Check if headers is present in the csv file or not 
  spec:                                 # Output fields mapping for each element
    - target: FirstName                 # Name of the column to be used in the output file
      source: name                      # If header row is present read value based on column name.
      sourceIndex:                      
      default:                          # Default Value to be used
      validate: regular expression      # Validate the value read from the source row if any
    - target: Contact
      source: 
      sourceIndex: 0                    # If header row is not present read value based on column index.
      default:                          # Default Value to be used
      validate: regular expression      # Validate the value read from the source row if any
```