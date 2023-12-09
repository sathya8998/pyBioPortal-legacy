import ruamel.yaml
from conf_build import VERSION, URL_ARCHIVE

def update_version_in_yaml(new_version):
    file_path = '../meta.yaml'

    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True  # maintain double quotes around values

    with open(file_path, 'r') as file:
        data = yaml.load(file) 

    # update version value
    data['package']['version'] = new_version
    data['source']['url'] = f"{URL_ARCHIVE}/pybioportal-v{new_version}.tar.gz"

    with open(file_path, 'w') as file:
        yaml.dump(data, file)

update_version_in_yaml(VERSION)
