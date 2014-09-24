"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import numpy
import thinkbayes2
import thinkplot


class Electorate(thinkbayes2.Suite):
    """Represents hypotheses about the state of the electorate."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: percentage of voters
        data: mean, sigma, measurement of the poll
        """
        actual = hypo
        mean, sigma, measurement = data
        error = measurement - actual

        like = thinkbayes2.EvalNormalPdf(error, mean, sigma)
        return like


def main():
    hypos = numpy.linspace(0, 100, 101)
    suite = Electorate(hypos)

    thinkplot.Pdf(suite, label='prior')

    data = 1.1, 3.7, 53
    suite.Update(data)

    print(suite.Mean())
    print(suite.Std())
    print(suite.ProbLess(50))
    thinkplot.Pdf(suite, label='posterior')

    data = -2.3, 4.1, 49
    suite.Update(data)

    print(suite.Mean())
    print(suite.Std())
    print(suite.ProbLess(50))
    thinkplot.Pdf(suite, label='posterior2')
    thinkplot.Show()


if __name__ == '__main__':
    main()
