"""This file contains code used in "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

from variability import *

import thinkplot
import thinkbayes2


def RunEstimate(update_func, num_points=31, median_flag=False):
    """Runs the whole analysis.

    update_func: which of the update functions to use
    num_points: number of points in the Suite (in each dimension)
    """
    d = ReadHeights(nrows=None)
    labels = {1:'male', 2:'female'}

    suites = {}
    for key, xs in d.items():
        label = labels[key]
        print(label, len(xs))
        Summarize(xs)

        xs = thinkbayes2.Jitter(xs, 1.3)

        mus, sigmas = FindPriorRanges(xs, num_points, median_flag=median_flag)
        suite = Height(mus, sigmas, label)
        suites[label] = suite
        update_func(suite, xs)
        print('MAP', suite.MaximumLikelihood())

    # joint distributions of mu and sigma for men and women
    suite1 = suites['male']
    suite2 = suites['female']

    # TODO: compute and plot the distribution of d

    d_pmf = thinkbayes2.Pmf()
    for (m_mu, m_sig), m_p in suite1.Items():
        for (f_mu, f_sig), f_p in suite2.Items():
            d_pmf.Incr((m_mu - f_mu) * 2 / (m_sig + f_sig), m_p * f_p)

    thinkplot.Cdf(d_pmf.MakeCdf())

    m_mu = suite1.Marginal(0)
    f_mu = suite2.Marginal(0)
    m_sig = suite1.Marginal(1)
    f_sig = suite2.Marginal(1)

    d_pmf2 = ((m_mu - f_mu) * 2) / (m_sig + f_sig)
    thinkplot.Cdf(d_pmf2.MakeCdf())

    print(d_pmf.Mean())
    print(d_pmf2.Mean())

    thinkplot.Show()

def main():
    random.seed(17)

    func = UpdateSuite5
    median_flag = (func == UpdateSuite5)
    RunEstimate(func, median_flag=median_flag)


if __name__ == '__main__':
    main()


