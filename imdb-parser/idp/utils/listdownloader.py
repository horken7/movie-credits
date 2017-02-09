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
import logging
import os
from ftplib import FTP
from .filehandler import FileHandler
from ..settings import *


def download():
    logging.info("Lists will downloaded from server:" + INTERFACES_SERVER)

    ftp = FTP(INTERFACES_SERVER)
    ftp.login()

    download_count = 0

    for list_item in LISTS:
        try:
            logging.info("Started to download list:" + list_item)
            r = ftp.retrbinary("RETR " + INTERFACES_DIRECTORY + list_item + ".list.gz", open(os.path.join(INPUT_DIR, list_item + ".list.gz"), "wb").write)
            logging.info(list_item + "list downloaded successfully")
            download_count = download_count + 1
            FileHandler.extract(FileHandler.get_full_path(list_item + ".list", True))
        except Exception as e:
            logging.error("There is a problem when downloading list " + list_item + "\n\t" + str(e))

    logging.info(str(download_count) + " lists are downloaded")
    ftp.quit()
