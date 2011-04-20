try:
    import cPickle as pickle
except ImportError:
    import pickle

if __name__ == '__main__':
    location = 'data/banner.p'
    with open(location) as f:
        messages = pickle.load(f)

    for line in messages:
        print ''.join([char * count for (char, count) in line])
