from src.constants.app import APP_NAME
from src.utils.pprint import banner
from src.cli.main import main
from saibyo.base.logs.logger import configure_logging

if __name__ == "__main__":
    configure_logging(APP_NAME, root_dir=".", logs_folder="logs")
    print(banner())
    main()
