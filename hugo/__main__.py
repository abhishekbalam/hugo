""" Entry Point for Program"""
import sys
from hugo import Hugo
import click


def main():
	"""Main entry point for the script."""
	d = Hugo("cmd")
	pass

if __name__ == '__main__':
	sys.exit(main())