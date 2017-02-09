"""
This file is part of imdb-data-parser.

imdb-data-parser is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

imdb-data-parser is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with imdb-data-parser.  If not, see <http://www.gnu.org/licenses/>.
"""

import gzip
import os.path
import logging
from ..settings import *


class FileHandler(object):
    def __init__(self, list_name, preferences_map):
        self.list_name = list_name
        self.preferences_map = preferences_map

    def full_path(self):
        return os.path.join(self.preferences_map['input_dir'], self.list_name)

    def tsv_path(self):
        return os.path.join(self.preferences_map['output_dir'], self.list_name) + ".tsv"

    def sql_path(self):
        return os.path.join(self.preferences_map['output_dir'], self.list_name) + ".sql"

    def get_input_file(self):
        full_file_path = self.full_path()
        logging.info("Trying to find file: %s", full_file_path)
        if os.path.isfile(full_file_path):
            logging.info("File found: %s", full_file_path)
            return open(full_file_path, "r", encoding='iso-8859-1')

        logging.error("File cannot be found: %s", full_file_path)

        logging.info("Trying to find file: %s", full_file_path + ".gz")
        if os.path.isfile(full_file_path + ".gz"):
            logging.info("File found: %s", full_file_path + ".gz")
            if extract(full_file_path + ".gz") == 0:
                return open(full_file_path, "r", encoding='iso-8859-1')
            else:
                raise RuntimeError("Unknown error occured")

        logging.error("File cannot be found: %s", full_file_path + ".gz")

        raise RuntimeError("FileNotFoundError: %s", full_file_path)

#this part removed until python 3.3 becomes available for ubuntu LTS and debian
#
#   print("Trying to find file:", full_file_path)
#   if os.path.isfile(full_file_path):
#       print("File found:", full_file_path)
#       return gzip.open(full_file_path, 'rt')
#   print("File cannot be found:", full_file_path)

    def get_tsv_file(self):
        return open(self.tsv_path(), "w", encoding='utf-8')

    def get_sql_file(self):
        return open(self.sql_path(), "w", encoding='utf-8')

    def extract(gzip_path):
        try:
            logging.info("Started to extract list: %s", gzip_path)
            with gzip.open(gzip_path, "rb") as f:
                file_content = f.read()
            list_file = open(gzip_path[:-3], "wb")
            list_file.write(file_content)
            list_file.close()
            logging.info(gzip_path + " list extracted successfully")
        except Exception as e:
            logging.error("Error when extracting list: " + gzip_path + "\n\t" + str(e))
            return 1
        return 0

    def get_full_path(filename, isCompressed = False):
	    """
	    constructs a full path for a dump file in the INPUT_DIR
	    filename should be without '.list'
	    """
	    if(isCompressed):
	        return os.path.join(INPUT_DIR, filename) + ".gz"
	    else:
	        return os.path.join(INPUT_DIR, filename)