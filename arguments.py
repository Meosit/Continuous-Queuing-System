import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Process input values')
    parser.add_argument('mu1', type=float, help='Intensity of chanel process')
    parser.add_argument('mu2', type=float, help='Intensity of chanel process')
    parser.add_argument('lmbd', type=float, help='Intensity of claim generated')
    return parser.parse_args()
