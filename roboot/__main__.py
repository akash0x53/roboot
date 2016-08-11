import argparse
from .scaffold import *

def main(*args, **kwargs):
	descr = "Creates directory structure for Robot Test cases"
	masterparser = argparse.ArgumentParser(description=descr)
	subparser = masterparser.add_subparsers(help="nothing")
	parser = subparser.add_parser("init", help="init project")
	parser.add_argument("project", type=str, nargs='?', default='', help="Project name")
	args = masterparser.parse_args()

	if "project" in args:
		create_project(args.project)
	else:
		print("Please provide project name")

if __name__ == "__main__":
	main()
