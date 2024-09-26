

libr = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}

libr_copy = libr.copy()
libr_copy.pop('key1')

for key, val in libr_copy.item():

  libr[key] = 