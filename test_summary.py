import numpy as np

def test_1(sample, population):
    bar_x = sample.mean
    mu_0 = population.mean
    sigma = population.std
    n = sample.size
    return (bar_x - mu_0) / (sigma / np.sqrt(n))

def test_2(two_samples, two_populations): 
    samples1, samples2 = two_samples
    population1, population2 = two_populations
    bar_x1, bar_x2 = samples1.mean, samples2.mean
    n1, n2 = samples1.size, samples2.size
    mu1, mu2 = population1.mean, population2.mean
    sigma = population1.std
    return ((bar_x1 - bar_x2) - (mu1 - mu2)) / (sigma * np.sqrt(1. / n1 + 1. / n2))

def test_3(two_samples, two_populations): 
    samples1, samples2 = two_samples
    population1, population2 = two_populations
    bar_x1, bar_x2 = samples1.mean, samples2.mean
    n1, n2 = samples1.size, samples2.size
    mu1, mu2 = population1.mean, population2.mean
    sigma1_2, sigma2_2 = population1.var, population2.var
    return ((bar_x1 - bar_x2) - (mu1 - mu2)) / np.sqrt(sigma1_2 / n1 + sigma2_2 / n2)

def test_4(sample, population): 
    p, p0 = sample.mean, population.mean
    n = sample.size
    return  (np.abs(p - p0) - 1 / (2 * n)) / np.sqrt(p0 * (1 - p0) / n)

def test_5(two_samples, dummy):
    samples1, samples2 = two_samples
    p1, p2 = samples1.mean, samples2.mean
    n1, n2 = samples1.size, samples2.size
    P = (p1 * n1 + p2 * n2) / (n1 + n2)
    return (p1 - p2) / np.sqrt(P * (1 - P) * (1 / n1 + 1 / n2))

def test_6(two_samples, dummy):
    (samples1, samples2), (t1, t2) = two_samples
    R1, R2 = samples1.mean, samples2.mean
    return (R1 - R2) / np.sqrt(R1 / t1 + R2 / t2)

def test_7(sample, population):
    bar_x = sample.mean
    diff = sample.sample_data - bar_x
    s = np.sqrt(diff @ diff/ (sample.size - 1))
    return (bar_x - population.mean) / (s / np.sqrt(sample.size))

def test_8(two_samples, two_populations):
    sample1, sample2 = two_samples
    population1, population2 = two_populations
    n1, n2 = sample1.size, sample2.size
    bar_x_1, bar_x_2 = sample1.mean, sample2.mean
    diff_1 = sample1.sample_data - bar_x_1
    diff_2 = sample2.sample_data - bar_x_2
    s1_2, s2_2 = diff_1 @ diff_1, diff_2 @ diff_2
    s_2 = ((n1 - 1) * s1_2 + (n2 - 1) * s2_2) / (n1 + n2 - 2) 
    return ((bar_x_1 - bar_x_2) - (population1.mean - population2.mean)) / np.sqrt(s_2 * (1. / n1 + 1. / n2))

def test_9(two_samples, two_populations):
    sample1, sample2 = two_samples
    population1, population2 = two_populations
    bar_x_1, bar_x_2 = sample1.mean, sample2.mean
    n1, n2 = sample1.size, sample2.size
    diff_1 = sample1.sample_data - sample1.mean
    diff_2 = sample2.sample_data - sample2.mean
    s1_2, s2_2 = diff_1 @ diff_1 / (n1 - 1), diff_2 @ diff_2 / (n2 - 1)
    return ((bar_x_1 - bar_x_2) - (population1.mean - population2.mean)) / np.sqrt(s1_2 / n1 + s2_2 / n2)

def test_10(two_samples, dummy):
    sample1, sample2 = two_samples
    bar_x1, bar_x2 = sample1.mean, sample2.mean
    n = sample1.size
    diff = sample1.sample_data - sample2.sample_data
    bar_d1 = diff.mean()
    d_diff = diff - bar_d1
    s_2 = d_diff @ d_diff / (n - 1)
    return (bar_x1 - bar_x2) / np.sqrt(s_2 / n)

def test_11(two_samples, dummy):
    x, y = two_samples
    x_data, y_data = x.sample_data, y.sample_data
    n = x.size
    sum_xy = x_data @ y_data
    sum_x_2 = x_data @ x_data
    x2 = x_data ** 2
    sum_x = np.sqrt(sum_x_2)
    sum_y = np.sqrt(y_data @ y_data)
    sum_x2 = np.sqrt(x2 @ x2)
    b = (sum_xy - sum_x * sum_y / n) / (sum_x2 - sum_x_2 / n)
    bar_x, bar_y = x.mean, y.mean
    diff_x = x_data - bar_x
    sx_2 = diff_x @ diff_x / (n - 1)
    diff_y_bx = y_data - bar_y - b * diff_x
    syx_2 = diff_y_bx @ diff_y_bx / (n - 1)
    t = b * np.sqrt(sx_2 / syx_2 / (n - 1))
    return t

def test_12(two_samples, dummy):
    x, y = two_samples
    x_data, y_data = x.sample_data, y.sample_data
    diff_x = x_data - x.mean
    diff_y = y_data - y.mean
    n = x.size
    r = diff_x @ diff_y / np.sqrt(diff_x @ diff_x * diff_y @ diff_y)
    t = r * np.sqrt((n - 2) / (1 - r * r))
    return t

test_dict = {
    "Test_1" : test_1,
    "Test_2" : test_2,
    "Test_3" : test_3,
    "Test_4" : test_4,
    "Test_5" : test_5,
    "Test_6" : test_6,
    "Test_7" : test_7,
    "Test_8" : test_8,
    "Test_9" : test_9,
    "Test_10" : test_10,
    "Test_11" : test_11,
    "Test_12" : test_12,
}