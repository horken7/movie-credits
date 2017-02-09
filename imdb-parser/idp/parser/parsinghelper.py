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

import logging
import traceback
from idp import settings


class ParsingHelper(object):
    """
    ParsingHelper manages parsing order
    """

    @staticmethod
    def parse_one(item, preferences_map):

        def get_parser_class_for(item_name):
            """
            Thanks to http://stackoverflow.com/a/452981
            """
            kls = "idp.parser." + item_name + "parser." + item_name.title() + "Parser"
            parts = kls.split('.')
            module = ".".join(parts[:-1])
            m = __import__( module )
            for comp in parts[1:]:
                m = getattr(m, comp)
            return m

        try:
            ParserClass = get_parser_class_for(item)
        except Exception as e:
            logging.error("No parser found for: " + item + "\n\tException is: " + str(e))
            return 1
        logging.info("___________________")
        logging.info("Parsing " + item + "...")
        parser = ParserClass(preferences_map)
        try:
            parser.start_processing()
        except Exception as e:
            logging.error("Exception occured while parsing item: " + item + "\n\tException is: " + str(e))
            traceback.print_exc()
        logging.info("Parsing finished for item: " + item)

    @staticmethod
    def parse_all(preferences_map):
        for item in settings.LISTS:
            ParsingHelper.parse_one(item, preferences_map)
        logging.info("All parsing finished.")

if __name__ == "__main__":
    """
    For debugging purposes
    """
    print("Parsing only one file for debugging purposes...")
    preferences_map = {
        "mode":"TSV",
        "inputDir": "../../samples/imdb_lists/",
        "outputDir": "../../samples/idp_files/"
    }
    ParsingHelper.parse_one("movies", preferences_map)
