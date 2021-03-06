# makeblog - A simple offline Blog.
# Copyright (C) 2013-2015 Stefan J. Betz <info@stefan-betz.net>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from os import chdir
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from sys import exit


class TCPServerReusable(TCPServer):
    allow_reuse_address = True


class Server(object):
    """
    A Simple testing Server for simple Blogs.
    """

    def __init__(self):
        chdir('dst/')
        self.httpd = TCPServerReusable(('127.0.0.1', 8000),
                                       SimpleHTTPRequestHandler)
        chdir('..')

    def serve(self):  # pragma: no cover
        print("Starting Webserver for http://127.0.0.1:8000/")
        try:
            chdir('dst/')
            self.httpd.serve_forever()
        except KeyboardInterrupt:
            exit()
