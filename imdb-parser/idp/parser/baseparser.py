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

import re
import logging
from abc import *
from ..utils.filehandler import FileHandler
from ..utils.regexhelper import RegExHelper
from ..utils.decorators import duration_logged
from ..utils.dbscripthelper import DbScriptHelper


class BaseParser(metaclass=ABCMeta):
    """
    Base class for all parser classes

    This class holds common methods for all parser classes and
    must be implemented by any Parser class

    Implementing classes' responsibilities are as follows:
    * Implement parse_into_tsv function
    * Implement parse_into_db function
    * Calculate fuckedUpCount and store in self.fuckedUpCount
    * Define following properties:
        - baseMatcherPattern
        - inputFileName
        - numberOfLinesToBeSkipped
        - scripts
    """

    seperator = "\t" #TODO: get from settings

    def __init__(self, preferences_map):
        self.mode = preferences_map['mode']
        self.filehandler = FileHandler(self.input_file_name, preferences_map)
        self.input_file = self.filehandler.get_input_file()

        if (self.mode == "TSV"):
          self.tsv_file = self.filehandler.get_tsv_file()
        elif (self.mode == "SQL"):
          self.sql_file = self.filehandler.get_sql_file()
          self.scripthelper = DbScriptHelper(self.db_table_info)
          self.sql_file.write(self.scripthelper.scripts['drop'])
          self.sql_file.write(self.scripthelper.scripts['create'])
          self.sql_file.write(self.scripthelper.scripts['insert'])

    @abstractmethod
    def parse_into_tsv(self, matcher):
        raise NotImplemented

    @abstractmethod
    def parse_into_db(self, matcher):
        raise NotImplemented

    @duration_logged
    def start_processing(self):
        '''
        Actual parsing and generation of scripts (tsv & sql) are done here.
        '''

        self.fucked_up_count = 0
        counter = 0
        number_of_processed_lines = 0

        for line in self.input_file : #assuming the file is opened in the subclass before here
            if(number_of_processed_lines >= self.number_of_lines_to_be_skipped):
                #end of data
                if(self.end_of_dump_delimiter != "" and self.end_of_dump_delimiter in line):
                    break

                matcher = RegExHelper(line)

                if(self.mode == "TSV"):
                    '''
                    give the matcher directly to implementing class
                     and let it decide what to do when regEx is matched and unmatched
                    '''
                    self.parse_into_tsv(matcher)
                elif(self.mode == "SQL"):
                    self.parse_into_db(matcher)
                else:
                    raise NotImplemented("Mode: " + self.mode)

            number_of_processed_lines +=  1

            #print("Processed lines: %d\r" % (number_of_processed_lines), end="")

        self.input_file.close()

        if(self.mode == "SQL"):
            self.sql_file.write(";\n COMMIT;")
            self.sql_file.close()

        if 'outputFile' in locals():
            self.output_file.flush()
            self.output_file.close()

        # fuckedUpCount is calculated in implementing class
        logging.info("Finished with " + str(self.fucked_up_count) + " fucked up line")

    def concat_regex_groups(self, group_list, col_list, matcher):
        ret_val = ""
        if col_list == None:
            ret_val = self.seperator.join('%s' % (matcher.group(i)) for i in group_list)
        else:
            for i in range(len(group_list)):
                if DbScriptHelper.keywords['string'] in self.db_table_info['columns'][col_list[i]]['colinfo']:
                    ret_val += "\"" + re.escape(matcher.group(group_list[i])) + "\", "
                else:
                    ret_val += matcher.group(group_list[i]) + ", "
            ret_val = ret_val[:-2]
        return ret_val

    ##### Below methods force associated properties to be defined in any derived class #####

    @abstractproperty
    def base_matcher_pattern(self):
        raise NotImplemented

    @abstractproperty
    def input_file_name(self):
        raise NotImplemented

    @abstractproperty
    def number_of_lines_to_be_skipped(self):
        raise NotImplemented

    @abstractproperty
    def db_table_info(self):
        raise NotImplemented

    @abstractproperty
    def end_of_dump_delimiter(self):
        raise NotImplemented
