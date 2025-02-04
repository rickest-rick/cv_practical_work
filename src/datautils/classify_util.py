import numpy as np


def split_data_labels(labeled_data):
    """
    Returns the labeled_data split into the data fields and the labels as ints.
    Additionally, a list is returned, that maps the string labels to their
    corresponding int labels.

    :author: Joschka Strüber
    :param labeled_data: array of tuples: [(path, roi, label), ...,
                                           (path, roi, label)]
        where path is a string, roi a tuple of ints and label a string.
    :return: data (list of tuples): [(img, roi), ..., (img, roi)],
        labels (array of ints): [label, ..., label],
        label_map (list of strings): [label_str, ..., label_str]
    """
    data = []
    str_labels = []
    for path, roi_coordinates, label in labeled_data:
        data.append((path, roi_coordinates))
        str_labels.append(label)
    labels, label_map = map_labels_to_int(str_labels)
    return data, labels, label_map


def get_roi(img, roi):
    """
    Extract the bounding box region of interest for a given image as numpy array
    and the coordinates of the roi as left x coordinate, lower y coordinate,
    width and height.

    :author: Thomas Poschadel, Joschka Strüber
    """
    x, y, w, h = roi
    return img[y:y + h, x:x + w]


def get_roi_with_aspect_ratio(img, roi, asp_ratio):
    """
    Extract the bounding box region of interest for a given image as numpy array
    and the coordinates of the roi as left x coordinate, lower y coordinate,
    width and height. But fits the ROI to have the same aspect ratio as used in
    asp_ratio

    :param asp_ratio: Provides the desired aspect ratio
    :author: Thomas Poschadel
    """
    x, y, w, h = roi
    current_ratio = w/h
    if current_ratio > asp_ratio:
        h_temp = int(w / asp_ratio)
        y = max(int(y - (h_temp - h)/2), 0)
        h = h_temp
    else:
        w_temp = int(asp_ratio * h)
        x = max(int(x - (w_temp - w)/2), 0)
        w = w_temp
    return get_roi(img, (x, y, w, h))


def map_labels_to_int(labels):
    """
    Map labels that are given as strings to integers that can be used with
    predefined classifiers that expect int labels.

    :author: Thomas Poschadel, Joschka Strüber
    """
    int_labels = []
    label_map = []
    for label in labels:
        if label not in label_map:
            label_map.append(label)
        int_label = label_map.index(label)
        int_labels.append(int_label)
    return np.array(int_labels), label_map


# Print iterations progress. Thanks to stackoverflow user Greenstick:
# https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def print_progress_bar (iteration, total, prefix='Progress:',
                        suffix='Complete', decimals=1, length=50, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent
                                  complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='')
    # Print New Line on Complete
    if iteration == total:
        print()


def print_h_m_s(seconds, message=""):
    """
    Print a number of seconds as days, hours and seconds with a given message.
    :author: Joschka Strüber
    """
    seconds = int(seconds)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print('{}{:d}h {:02d}m {:02d}s'.format(message, h, m, s))
