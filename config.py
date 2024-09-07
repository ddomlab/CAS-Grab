import elabapi_python
import urllib3
import yaml
# TODO consider getting rid of config.yml

urllib3.disable_warnings()  # allows the connection
# configuration file with api key band url
with open("config.yml") as config_file:
    config = yaml.safe_load(config_file)

# Configure the api client TODO: move this to a new file
configuration = elabapi_python.Configuration()
with open(config["api_key_path"]) as keyfile:
    configuration.api_key["api_key"] = keyfile.read()
configuration.api_key_prefix["api_key"] = "Authorization"
configuration.host = config["url"]
configuration.debug = False
configuration.verify_ssl = False

# create an instance of the API class
api_client = elabapi_python.ApiClient(configuration)
# fix issue with Authorization header not being properly set by the generated lib
with open(config["api_key_path"]) as keyfile:
    api_client.set_default_header(
        header_name="Authorization", header_value=keyfile.read()
    )


def load_items_api():
    return elabapi_python.ItemsApi(api_client)
