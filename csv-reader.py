import csv
import yaml
import logging.config

# load configuration
# Get Configuration
csv_config ={}
with open('csv-config.yaml', 'r') as cf:
    csv_config = yaml.safe_load(cf.read())
    print("#### CSV Configuration ....")
    print(csv_config)
    logging.info("CSV Transformation Configuration: {0}".format(csv_config))

# yaml file based logging
with open(csv_config.get('logConfig'), 'r') as log:
    logging_config = yaml.safe_load(log.read())
    logging.config.dictConfig(logging_config)

# Get the logger specified in the file
logger = logging.getLogger(__name__)
logger.info("Configuration loaded successfully")

def process(csvFile, network):
    logger.info("Process Input parameters: {0}  {1}".format(csvFile, network))
    # based on the network name get config for a particular network from the csv_config
    # ... add code
    mapping = csv_config.get('networks').get(network)
    logger.info("Network: {0} Mapping: {1}".format(network, mapping))

    # read the csv file
    output = None
    with open(csvFile, 'r') as file:
        output = readCSV(file, mapping)
 
    # write output to a yaml file  
    writeToYaml(mapping.get('outputFile'), output) 
    return output   
 
def writeToYaml(file, data):
    ff = open(file, 'w')
    yaml.dump(data, ff)

def readCSV(file, mapping):
   
    # Iterate over the csv file and call transform for each record in the csv file  
    logger.info("Field Delimiter: {0} ".format(mapping.get('fieldDelimiter')))
    csv_iterator = csv.reader(file, delimiter=mapping.get('fieldDelimiter'))
    output = []
    # for each record in the csv file
    header = None
    print(mapping.get('header'))
    if mapping.get('header'):
        header = next(csv_iterator)

    for row in csv_iterator:
        # call transformation     
        output.append(transform(row,header, mapping.get('spec')))
        
    return output

def transform(row, header, spec): 
    # perform transformation on the record based on the mapping 
    logger.info("Row Specification: {0} ".format(spec))
    logger.info("Row element: {0} ".format(row))
    logger.info("Header element: {0} ".format(header))

    dict = {}
    for element in spec:
        key, value = extract(element, row, header)
        logger.info("Key: {0} Value: {1} ".format(key, value))
        dict[key] = value
    
    return dict


def extract(element, row, header):
    # Get the output value 
    logger.info("Element: {0} ".format(element))
    logger.info("Row: {0} ".format(row))
    
    sourceIndex = element.get('sourceIndex')
    source = element.get('source')
    default = element.get('default')

    value = None
    if sourceIndex is not None:
        value = row[sourceIndex]
    elif source is not None:
        value = row[header.index(source)]
    else:
        value = default

    return element.get('target'), value



# Transform CSV File without Header
#result = process('data/sample-file1.csv', 'nma')
#logger.info("Output : {0} ".format(result))

# Transform CSV FIle with Header
result = process('data/sample-file1-with-header.csv', 'gc')
logger.info("Output : {0} ".format(result))
