# SecuML
# Copyright (C) 2016-2019  ANSSI
#
# SecuML is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# SecuML is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with SecuML. If not, see <http://www.gnu.org/licenses/>.

factory = None


def get_factory():
    global factory
    if factory is None:
        factory = Factory()
    return factory


class Factory(object):

    def __init__(self):
        self.strategies = {}

    def register(self, class_name, class_obj):
        self.strategies[class_name] = class_obj

    def get_strategy(self, iteration, query_strategy):
        return self.strategies[query_strategy](iteration)
