import matplotlib.pyplot as plt


def showpoints(title, filename, folderPath):
    x = []
    y = []
    d = []
    with open(folderPath+'\\'+filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip().split(',') for x in content]
    for item in content:
        d.append(item)
        x.append(float(item[0]))
        y.append(float(item[1]))

    d = [[float(y) for y in x] for x in d]
    # plt.axis([0, 1440, 2560, 0])

    # plt.scatter(x, y, s=1)
    # plt.title(title)
    # plt.show()
    return d


