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

import os


class DbScriptHelper(object):
    keywords = {
        'string': "VARCHAR",
        'number': "NUMERIC",
        'date': "DATE"
    }

    scripts = {
        'drop': "DROP TABLE ",
        'create': "CREATE TABLE ",
        'insert': "INSERT INTO "
    }

    def __init__(self, db_table_info):
        self.scripts = {
            'drop': "DROP TABLE ",
            'create': "CREATE TABLE ",
            'insert': "INSERT INTO "
        }
        self.scripts['drop'] += db_table_info['tablename'] + ";" + os.linesep
        self.scripts['create'] += db_table_info['tablename'] + "(" + ', '.join(filter(None, (', '.join('%s %s' % (col['colname'], col['colinfo']) for col in db_table_info['columns']), db_table_info['constraints']))) + ") CHARACTER SET utf8 COLLATE utf8_bin;" + os.linesep
        self.scripts['insert'] += db_table_info['tablename'] + "(" + ', '.join(col['colname'] for col in db_table_info['columns']) + ") VALUES" + os.linesep