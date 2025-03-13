import toml

def load_toml_config():
    try:
        with open('sf_config.toml', 'r') as config:
            db = toml.load(config)
            return db
    except FileNotFoundError:
        print("toml config not found")
    except toml.TomlDecodeError:
        print("Invalid toml format")