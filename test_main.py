#!/usr/bin/env python3
"""
Unit tests for main application module.
"""

import unittest
from unittest.mock import MagicMock, patch
from main import Application


class TestApplication(unittest.TestCase):
    """Test cases for Application class."""

    @patch("main.ConfigManager")
    def setUp(self, mock_config):
        """Set up test fixtures."""
        self.mock_config = mock_config
        self.app = Application()

    def test_application_initialization(self):
        """Test application initialization."""
        self.assertIsNotNone(self.app)
        self.assertIsNotNone(self.app.config)

    @patch("main.logger")
    def test_run_logs_start_and_end(self, mock_logger):
        """Test that run method logs start and end messages."""
        with patch.object(self.app, "process_data"):
            self.app.run()
            self.assertTrue(mock_logger.info.called)

    def test_process_data_completes(self):
        """Test that process_data completes without error."""
        self.app.process_data()  # Should not raise


class TestConfigManager(unittest.TestCase):
    """Test cases for ConfigManager class."""

    def test_default_config(self):
        """Test default configuration is loaded."""
        from config import ConfigManager

        config = ConfigManager()
        self.assertEqual(config.get("app_name"), "gitbranchtest")
        self.assertEqual(config.get("log_level"), "INFO")

    def test_config_get_set(self):
        """Test get and set methods."""
        from config import ConfigManager

        config = ConfigManager()
        config.set("test_key", "test_value")
        self.assertEqual(config.get("test_key"), "test_value")


if __name__ == "__main__":
    unittest.main()
