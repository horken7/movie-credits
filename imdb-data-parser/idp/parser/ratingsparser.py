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


class RatingsParser(BaseParser):
    """
    RegExp: /\s*(\S*)\s*(\S*)\s*(\S*)\s*((.*? \(\S{4,}\)) ?(\(\S+\))? ?(?!\{\{SUSPENDED\}\})(\{(.*?) ?(\(\S+?\))?\})? ?(\{\{SUSPENDED\}\})?)$/gm
    pattern: \s*(\S*)\s*(\S*)\s*(\S*)\s*((.*? \(\S{4,}\)) ?(\(\S+\))? ?(?!\{\{SUSPENDED\}\})(\{(.*?) ?(\(\S+?\))?\})? ?(\{\{SUSPENDED\}\})?)$
    flags: gm
    10 capturing groups:
        group 1: (\S*)                               distribution
        group 2: (\S*)                               votes
        group 3: (\S*)                               rank
        group 4: #TITLE (UNIQUE KEY)
        group 5: (.*? \(\S{4,}\))                    movie name + year
        group 6: (\(.+\))                            type ex:(TV)
        group 7: (\{(.*?)\s?(\(.+?\))\})             series info ex: {Ally Abroad (#3.1)}
        group 8: (.*?)                               episode name ex: Ally Abroad
        group 9: (\(.+?\))                           episode number ex: (#3.1)
        group 10: (\{\{SUSPENDED\}\})                is suspended?
    """
  
    # properties
    base_matcher_pattern = "\s*(\S*)\s*(\S*)\s*(\S*)\s*((.*? \(\S{4,}\)) ?(\(\S+\))? ?(?!\{\{SUSPENDED\}\})(\{(.*?) ?(\(\S+?\))?\})? ?(\{\{SUSPENDED\}\})?)$"
    input_file_name = "ratings.list"
    number_of_lines_to_be_skipped = 28
    db_table_info = {
        'tablename' : 'ratings',
        'columns' : [
            {'colname' : 'distribution', 'colinfo' : DbScriptHelper.keywords['string'] + '(127) NOT NULL'},
            {'colname' : 'votes', 'colinfo' : DbScriptHelper.keywords['string'] + '(127)'},
            {'colname' : 'rank', 'colinfo' : DbScriptHelper.keywords['string'] + '(127)'},
            {'colname' : 'title', 'colinfo' : DbScriptHelper.keywords['string'] + '(255) NOT NULL'}
        ],
        'constraints' : 'PRIMARY KEY(title)'
    }
    end_of_dump_delimiter = ""

    def __init__(self, preferences_map):
        super(RatingsParser, self).__init__(preferences_map)
        self.first_one = True

    def parse_into_tsv(self, matcher):
        is_match = matcher.match(self.base_matcher_pattern)

        if(is_match):
            self.tsv_file.write(self.concat_regex_groups([1,2,3,4], None, matcher) + "\n")
        else:
            logging.critical("This line is fucked up: " + matcher.get_last_string())
            self.fucked_up_count += 1

    def parse_into_db(self, matcher):
        is_match = matcher.match(self.base_matcher_pattern)

        if(is_match):
            if(self.first_one):
                self.sql_file.write("(" + self.concat_regex_groups([1,2,3,4], [0,1,2,3], matcher) + ")")
                self.first_one = False;
            else:
                self.sql_file.write(",\n(" + self.concat_regex_groups([1,2,3,4], [0,1,2,3], matcher) + ")")
        else:
            logging.critical("This line is fucked up: " + matcher.get_last_string())
            self.fucked_up_count += 1
