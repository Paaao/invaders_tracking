import argparse
from tracker.invaders_tracker import Tracker

arguments_parser = argparse.ArgumentParser()
arguments_parser.add_argument("-f", "--sample_file", help="Filename with radar img", default='./data/radar_sample.txt')

args = arguments_parser.parse_args()

if args.sample_file:
    radar_input_file = args.sample_file
else:
    radar_input_file = './data/radar_sample.txt'

radar_output_file = './data/output.txt'

tracker = Tracker(radar_input_file, radar_output_file)
tracker.run_search()