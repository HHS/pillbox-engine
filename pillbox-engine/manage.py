#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.production")
    from django.core.management import execute_from_command_line

    # sys.path.insert(0, os.path.abspath('pillbox-engine'))
    execute_from_command_line(sys.argv)
