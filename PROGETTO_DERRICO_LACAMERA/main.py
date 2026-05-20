from Handler import Handler
from utils import read_file

if __name__ == "__main__":
    c_path = r".\resources\companies.txt"
    r_path = r".\resources\riders.txt"
    handler = Handler(riders_path=r_path, companies_path=c_path)
    handler.start()
    exit()
