import numpy as np
import matplotlib.pyplot as plt


def swap_matrix(matrix):
    res = []
    r = len(matrix)

    m0 = matrix[0]
    if not (isinstance(m0, list) or isinstance(m0, tuple)):
        return matrix

    c = len(matrix[0])

    r, c = c, r
    for i in range(c):
        temp = []
        for j in range(r):
            eee = matrix[j][i]
            temp.append(eee)
        res.append(temp)
    return res


def bottoms_matrix(matrix):
    positives = []
    negatives = []
    for i, row_mat in enumerate(matrix):
        tmp_p = []
        tmp_n = []
        for j, cell in enumerate(row_mat):
            if cell >0:
                tmp_p.append(cell)
                tmp_n.append(0.)
            else:
                tmp_p.append(0.)
                tmp_n.append(cell)
        positives.append(tmp_p)
        negatives.append(tmp_n)

    # get cumulative sums
    positives = positives[:-1]
    negatives = negatives[:-1]
    positives.insert(0, [0.] * len (matrix[0]))
    negatives.insert(0, [0.] * len(matrix[0]))
    tmp = swap_matrix(positives)
    tmp = [list(np.cumsum(t)) for t in tmp]
    positives = swap_matrix(tmp)

    tmp = swap_matrix(negatives)
    tmp = [list(np.cumsum(t)) for t in tmp]
    negatives = swap_matrix(tmp)

    final_matrix =[]
    for i, row_mat in enumerate(matrix):
        tmp =[]
        for j, cell in enumerate(row_mat):
            tmp.append(positives[i][j] if cell > 0 else negatives[i][j])
        final_matrix.append(tmp)
    return final_matrix

# Sample Data
Out01 = [79.069,-1.602,5.067,-4.241,-5.433,-4.590]
Out02 = [50.348,13.944,-15.373,6.554,5.541,8.240]
Out03 = [-8.053,0.819,-9.741,2.814,22.475,56.098]
Out04 = [-17.350,33.710,-18.510,-0.842,3.050,26.537]
Out05 = [-20.169,37.583,-20.785,-2.041,1.728,17.695]
y = [Out01, Out02, Out03, Out04, Out05]

num_outputs= len(y)
num_inputs = len (y[0])
# invert rows to columns to prepare drawing (A function for that is attached)
y = swap_matrix(y)

# labels
label_inputs = []
for i in range(num_inputs):
    label_inputs.append('In ' + str(i))
label_outputs = []
for i in range(num_inputs):
    label_outputs.append('Out ' + str(i))

ind = np.arange(num_outputs)  # the x locations for the groups
width = 0.35  # the width of the bars: can also be len(x) sequence
bars = [0] * num_outputs
bottoms = bottoms_matrix(y)
for i in range(num_outputs):
    dat = tuple(y[i])
    bars[i] = plt.bar(ind, dat, width, bottom=bottoms[i], color=np.random.rand(3, 1))  # , yerr=menStd)
legend_info = []
for bar in bars:
    legend_info.append(bar[0])
legend_info = tuple(legend_info)

plt.ylabel('Relative contribution')
plt.title('Contribution of inputs to outputs')
plt.xticks(ind + width / 2., tuple(label_outputs))
plt.legend(legend_info, tuple(label_inputs))


