# YARFI - Yet Another Replacement For Init
# Copyright (C) 2014 Niklas Sombert
#
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

from yarfi.ServicesAndTargets import Target as Trg

class Target(Trg):
	def __init__(self):
		self.description = "Multi User Mode"
		self.depends_targets = ["gettys"]
		self.depends_services = ["dbus", "filesystem", "udev", "cron", "anacron"]
		self.conflicts = ["single"]
