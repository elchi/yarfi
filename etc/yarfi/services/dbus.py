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
class service:
	def __init__(self):
		self.description = "message bus"
		self.depends = ["filesystem"]
		self.conflicts = []
		self.respawn = True

	def start(self, args):
		os = args["os"]
		subprocess = args["subprocess"]
		try:
			os.mkdir("/var/run/dbus")
		except OSError as e:
			if e.errno == 17:
				pass
			else:
				raise
		passwd = open("/etc/passwd")
		for line in passwd:
			if line.startswith("messagebus"):
				uid = line.split(":")[2]
		passwd.close()
		group = open("/etc/group")
		for line in group:
			if line.startswith("messagebus"):
				gid = line.split(":")[2]
		group.close()
		os.chown("/var/run/dbus", uid, gid)
		
		subprocess.Popen(["dbus-uuidgen", "--ensure"]).wait()
		
		self.process = subprocess.Popen(["dbus-daemon", "--system"])

	def stop(self, args):
		os = args["os"]
		time = args["time"]
		self.process.terminate()
		if self.process.returncode == None:
			time.sleep(5)
			self.process.kill()
		os.remove("/var/run/dbus/pid")