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

import datetime
import logging


def duration_logged(func):
    '''
    As the name suggests, calculates the execution duration of the function which is annotated by this decorator
    '''
    def inner(*args, **kwargs):
        start_time = datetime.datetime.now()
        ret_val = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        duration = (end_time - start_time).total_seconds() #difference of 2 datetime is a timedelta
        logging.info("Parsing took " + str(duration) + " seconds")
        return ret_val
    return inner