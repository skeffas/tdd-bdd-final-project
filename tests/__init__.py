# test/test__init__.py

import unittest
from flask import Flask
from service import config
from service.common import log_handlers

class TestServiceInitialization(unittest.TestCase):

    def setUp(self):
        # Create a Flask app for testing
        self.app = Flask(__name__)
        self.app.config.from_object(config)

        # Set up logging for testing
        log_handlers.init_logging(self.app, "test.log")

    def tearDown(self):
        # Clean up resources after testing (if needed)
        pass

    def test_config_database_uri(self):
        # Check if the SQLALCHEMY_DATABASE_URI is set correctly
        expected_database_uri = "postgresql://postgres:postgres@localhost:5432/postgres"
        self.assertEqual(self.app.config['SQLALCHEMY_DATABASE_URI'], expected_database_uri)

    def test_config_secret_key(self):
        # Check if the SECRET_KEY is set correctly
        expected_secret_key = "sup3r-s3cr3t"
        self.assertEqual(self.app.config['SECRET_KEY'], expected_secret_key)

    def test_init_db_failure(self):
        # Test initialization failure (this should trigger lines 53-56)
        with self.assertRaises(Exception):
            with self.app.app_context():
                from service import models
                models.init_db(self.app)

if __name__ == '__main__':
    unittest.main()