import os
import sys
from pytest import raises
# get main directory
__location__ = os.path.join(os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))), "..")
# add it to sys path for imports to work
sys.path.insert(0, os.path.join(__location__))
# import project-level modules

from avc.ArduinoComm import ArduinoComm, ArduinoCommException
from avc.ArduinoComm import Command, CommandException
from avc.ConfigReader import ConfigReader
from time import sleep


# TESTS:

def test_command_fullstring_with_only_command():
	command_string = "testcommand"
	command = Command.create_command(command_string)
	assert command.get_command() == command_string

def test_command_fullstring_with_values():
	command_string = "testcommand"
	value_string = "testvalue"
	full_string = command_string + "|" + value_string
	command = Command.create_command(full_string)
	assert command.get_command() == command_string
	assert command.get_values() == [value_string]

def test_command_only_command_given():
	command_string = "testcommand"
	command = Command(command_string)
	assert command.get_command() == command_string

def test_command_string_value():
	command_string = "testcommand"
	value_string = "testvalue"
	command = Command(command_string,value_string)
	assert command.get_command() == command_string
	assert command.get_values() == [value_string]

def test_command_list_value():
	command_string = "testcommand"
	value_string = "testvalue"
	command = Command(command_string,[value_string])
	assert command.get_command() == command_string
	assert command.get_values() == [value_string]

# END TESTS


# setup objects for this module
def setup_module(module):
	module.config = ConfigReader.read_json("conf.json")
	module.fakeconfig = ConfigReader.read_json("testconf.json")

def teardown_module(module):
	pass
# done setting up objects for this module

# set up for each function
def setup_function(function):
	pass

def teardown_function(function):
	pass
# done setting up objects for each function