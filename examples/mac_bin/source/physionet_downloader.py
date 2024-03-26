import argparse
import subprocess
import sys

def download_physionet_database(database_name):
    '''
    base_url = "https://physionet.org/physionet.org/files/"
    url = base_url + database_name
    '''
    subprocess.call(["wget", "-r", "-N", "-c", "-np", url])

def main():
    '''
    parser = argparse.ArgumentParser(description="PhysioNet Database Downloader")
    parser.add_argument("database_name", help="Name of the PhysioNet database")
    args = parser.parse_args()
    '''

    #download_physionet_database(args.database_name)
    download_physionet_database(sys.argv[2:])


if __name__ == "__main__":
    main()
