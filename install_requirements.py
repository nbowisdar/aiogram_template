import subprocess
import os


def install_package(package_name):
    command = "pip install " + package_name
    subprocess.check_call(command)


def delete_file(file_path):
    os.remove(file_path)


if __name__ == "__main__":
    install_package("aiogram --pre")
    install_package("-r requirements.txt")

    from loguru import logger

    logger.info("All libraries installed!")
