import argparse
import glob
import os
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a data.json file to be used with view and label')
    parser.add_argument('-i', '--input_dir', required=True, help="Input directory containing a set of video clips to be labeled")
    parser.add_argument('-l', '--labels', required=True, help="Colon separated label definitions")

    options = parser.parse_args()

    f = sorted(glob.glob(options.input_dir + '/*.mp4'))
    f = map(os.path.basename, f)
    o_dict = {}
    labels = options.labels.split(':')
    o_dict['classes'] = labels
    o_dict['file_info'] = []
    for f_ in f:
        v = {}
        v['name'] = f_
        v['class'] ='XXX'
        o_dict['file_info'].append(v)

    with open(options.input_dir+'/data.json', 'w') as fd:
        json.dump(o_dict, fd)
