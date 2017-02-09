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


class PlotParser(BaseParser):
    """
    RegExp: /(.+?): (.*)/g
    pattern: (.+?): (.*)
    flags: g
    2 capturing groups: 
       group 1: (.+?)   type of the line
       group 2: (.*)    if the line-type is PL then this line is plot, not the whole but one line of it
                        if the line-type is MV then this line is movie
    """
  
    # properties
    base_matcher_pattern = "(.+?): (.*)"
    input_file_name = "plot.list"
    number_of_lines_to_be_skipped = 15
    db_table_info = {
        'tablename' : 'plot',
        'columns' : [
            {'colname' : 'title', 'colinfo' : DbScriptHelper.keywords['string'] + '(255) NOT NULL'},
            {'colname' : 'plot', 'colinfo' : DbScriptHelper.keywords['string'] + '(4000)'}
        ],
        'constraints' : 'PRIMARY KEY(title)'
    }
    end_of_dump_delimiter = ""

    def __init__(self, preferences_map):
        super(PlotParser, self).__init__(preferences_map)
        self.first_one = True

        # specific to this class
        self.title = ""
        self.plot = ""

    def parse_into_tsv(self, matcher):
        is_match = matcher.match(self.base_matcher_pattern)

        if(is_match):
            if(matcher.group(1) == "MV"): #Title
                if(self.title != ""):
                    self.tsv_file.write(self.title + self.seperator + self.plot + "\n")

                self.plot = ""
                self.title = matcher.group(2)

            elif(matcher.group(1) == "PL"): #Descriptive text
                self.plot += matcher.group(2)
            elif(matcher.group(1) == "BY"):
                pass
            else:
                logging.critical("Unhandled abbreviation: " + matcher.group(1) + " in " + line)
        #else:
            #just ignore this part, useless lines

        """
            FIXME: this parsing  misses the last entry
                need to execute following just after looping the input file's lines:
            # Covers the last item
            outputFile.write(title + self.seperator + plot + "\n")

            consider writing to the file in "BY:" condition
        """

    def parse_into_db(self, matcher):
        is_match = matcher.match(self.base_matcher_pattern)

        if(is_match):
            if(matcher.group(1) == "MV"): #Title
                if(self.title != ""):
                    if(self.first_one):
                        self.sql_file.write("(\"" + self.title + "\", \"" + self.plot + "\")")
                        self.first_one = False;
                    else:
                        self.sql_file.write(",\n(\"" + self.title + "\", \"" + self.plot + "\")")

                self.plot = ""
                self.title = matcher.group(2)

            elif(matcher.group(1) == "PL"): #Descriptive text
                self.plot += matcher.group(2)
            elif(matcher.group(1) == "BY"):
                pass
            else:
                logging.critical("Unhandled abbreviation: " + matcher.group(1) + " in " + line)
