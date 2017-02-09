imdb-data-parser
================

Parses the IMDB dumps into CSV and Relational Database insert queries
Uses IMDB dumps from: http://www.imdb.com/interfaces

imdb-data-parser is a free software licensed by GPLv3.


Requirements
================
* Python 3.x

Configuring
================
All configuration data stays at `idp/settings.py.example`

You need to copy this file as `settings.py` and edit this file before running the project

    cd idp
    cp settings.py.example settings.py
    your_favourite_editor settings.py

You also need to have dump files at `INPUT_DIR` and you can download dump files from one of the FTP addresses on http://www.imdb.com/interfaces.

Besides that you can make `imdb-data-parser` dowload dumps for you by giving `-u` argument:

	~/imdb-data-parser$ ./imdbparser.py -u

Executing
---------

    ~/imdb-data-parser$ ./imdbparser.py

You can use -h parameter to see list of optional arguments

    ~/imdb-data-parser$ ./imdbparser.py -h

SQL Dumps
---------
You can use mode parameter to create SQL dumps

    ~/imdb-data-parser$ ./imdbparser.py -h

Default configuration of MySQL doesn't allow insert data more than 16MB. You need to change your mysql max_allowed_packet size to insert sql dumps.

    max_allowed_packet      = 256M

Our movies data includes series, videos, tv shows for now. You can exclude them by this command:

     grep -v '("\\"' movies.list.sql | grep -v '\\(VG\\)' | grep -v "\\(TV\\)" | grep -v "{" | grep -v "????" | grep -v "(V\\\)" > movies.sql

Note: SQL dumps tested with only mysql.
