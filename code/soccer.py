"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import numpy
import thinkbayes2
import thinkplot


class Soccer(thinkbayes2.Suite):
    """Represents hypotheses about."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: lambda parameter (goals per game)
        data: time between goals
        """

        goals_per_minute = hypo / 90.0

        like = thinkbayes2.EvalExponentialPdf(data, goals_per_minute)

        return like

    def PredRemaining(self, rem_time, score):
        """Plots the predictive distribution for final number of goals.

        rem_time: remaining time in the game in minutes
        score: number of goals already scored
        """
        metaPmf = thinkbayes2.Pmf()

        for lam, prob in self.Items():
            poisson = thinkbayes2.MakePoissonPmf(lam * rem_time / 90, 12)
            metaPmf[poisson] = prob

        return thinkbayes2.MakeMixture(metaPmf) + score


def main():
    hypos = numpy.linspace(0, 12, 201)
    suite = Soccer(hypos)

    #Create prior with pseudo-observation
    suite.Update(69)
    thinkplot.Pdf(suite, label='prior')
    print('prior mean', suite.Mean())

    inter_arrival_times = [11, 12] #, 1, 2, 3]
    for i, time in enumerate(inter_arrival_times):
        suite.Update(time)
        #thinkplot.Pdf(suite, label='posterior ' + str(i))
        print('after ' + str(i) + ' goal', suite.Mean())

    prediction = suite.PredRemaining(67, 2)
    print(prediction.ProbGreater(6.5))

    thinkplot.Hist(prediction)
    thinkplot.Show()


if __name__ == '__main__':
    main()
