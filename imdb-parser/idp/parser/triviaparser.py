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

from .baseparser import *


class TriviaParser(BaseParser):
    """
    RegExp: /((.+?) (.*))|\n/g
    pattern: ((.+?) (.*))|\n
    flags: g
    2 capturing groups:
       group 1: (.+?)   type of the line
       group 2: (.*)    if the line-type is - then this line is plot, not the whole but one line of it
                        if the line-type is # then this line is movie
    """

    # properties
    base_matcher_pattern = "((.+?) (.*))|\n"
    input_file_name = "trivia.list"
    number_of_lines_to_be_skipped = 15
    db_table_info = {
        'tablename' : 'trivia',
        'columns' : [
            {
                'colname' : '',
                'colinfo' : DbScriptHelper.keywords['string'] + '(255) NOT NULL'
            }
        ],
        'constraints' : ''
    }
    end_of_dump_delimiter = ""

    title = ""
    trivia = ""

    def __init__(self, preferences_map):
        super(TriviaParser, self).__init__(preferences_map)
        self.first_one = True

    def parse_into_tsv(self, matcher):
        is_match = matcher.match(self.base_matcher_pattern)

        if(is_match):
            if(matcher.group(2) == "#"): #Title
                self.title = matcher.group(3)
            elif(matcher.group(2) == "-"): #Descriptive text
                self.trivia = matcher.group(3)
            elif(matcher.group(2) == " "):
                self.trivia += ' ' + matcher.group(3)
            else:
                self.tsv_file.write(self.title + self.seperator + self.trivia + "\n")
        else:
            logging.critical("This line is fucked up: " + matcher.get_last_string())
            self.fucked_up_count += 1

    def parse_into_db(self, matcher):
        #TODO
        pass
