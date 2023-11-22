#!/usr/bin/python3
""" Module for testing the console """
import unittest
import os
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
from models import storage


class TestConsole(unittest.TestCase):
    """ Class to test the HBNB console """

    @classmethod
    def setUpClass(cls):
        """ Set up test environment """
        cls.console = HBNBCommand()

    def tearDown(self):
        """ Clean up test environment """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def setUp(self):
        """ Reset storage for each test """
        storage.reload()
        FileStorage.__objects = {}

    def test_quit(self):
        """ Test the quit command"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_EOF(self):
        """ Test the EOF command """
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    def test_create_missing_classname(self):
        """ Test create command with missing class name """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())

    def test_create_invalid_classname(self):
        """ Test create command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

    def test_create_with_params(self):
        """ Test create command with initial parameters """
        create_cmd = ('create User email="test@example.com" password="test" '
                      'first_name="Jose"')
        with patch('sys.stdout', new=StringIO()) as fake_output:
            HBNBCommand().onecmd(create_cmd)
            usr_id = fake_output.getvalue().strip()
            self.assertIsNotNone(usr_id)

            show_cmd = f'show User {usr_id}'
            HBNBCommand().onecmd(show_cmd)
            usr_obj_output = fake_output.getvalue().strip()
            self.assertIn('test@example.com', usr_obj_output)
            self.assertIn('Jose', usr_obj_output)

    def test_create_with_string(self):
        """ Test create command with string parameter """
        cmd = 'create State name="California_is_sunny"'
        expected_part_output = "California is sunny"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.onecmd(cmd)
            state_id = fake_output.getvalue().strip()
            self.console.onecmd(f"show State {state_id}")
            self.assertIn(expected_part_output, fake_output.getvalue())

    def test_create_with_int(self):
        """ Test create command with integer parameter """
        cmd = 'create User age=35'
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.onecmd(cmd)
            user_id = fake_output.getvalue().strip()
            self.console.onecmd(f"show User {user_id}")
            self.assertIn("'age': 35", fake_output.getvalue())

    def test_create_with_float(self):
        """ Test create command with float parameter """
        cmd = 'create Place latitude=120.5'
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.onecmd(cmd)
            place_id = fake_output.getvalue().strip()
            self.console.onecmd(f"show Place {place_id}")
            self.assertIn("'latitude': 120.5", fake_output.getvalue())

    def test_create_with_wrong_data_type(self):
        """ Test create command with wrong data type parameter """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.onecmd('create User age="thirtyfive"')
            output = fake_output.getvalue()
            self.assertNotIn("thirtyfive", output)

    def test_create_with_overwriting_params(self):
        """ Test create command with overwriting parameters """
        cmd = ('create User email="original@example.com" '
               'email="overwrite@example.com"')
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.onecmd(cmd)
            user_id = fake_output.getvalue().strip()
            self.console.onecmd(f"show User {user_id}")
            self.assertIn("'email': 'overwrite@example.com'",
                          fake_output.getvalue())

    def test_create_with_extra_spaces(self):
        """ Test create command with extra spaces """
        cmd = 'create  User    email="test@example.com"   password="pass"'
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.onecmd(cmd)
            user_id = fake_output.getvalue().strip()
            self.console.onecmd(f"show User {user_id}")
            self.assertIn("'email': 'test@example.com'",
                          fake_output.getvalue())
            self.assertIn("'password': 'pass'", fake_output.getvalue())
