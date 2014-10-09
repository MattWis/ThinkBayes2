"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import thinkplot
from thinkbayes2 import Suite


class Train(Suite):
    """Represents hypotheses about how many trains the company has.
    """

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: number of total trains
        data: (number of trains seen, maximum train number seen)
        """
        num_seen, max_seen = data
        num_trains = hypo

        if (num_trains < max_seen):
            return 0
        else:
            #Assume can see each train twice
            #return float(max_seen**(num_seen - 1)) / num_trains**num_seen
            return 1.0 / num_trains**num_seen




def main():
    hypos = range(1, 1001)
    suite = Train(hypos)

    suite.Update((3, 70))
    thinkplot.Pmf(suite, label='after')

    #thinkplot.Show(xlabel='Number of trains',
                   #ylabel='PMF')

    print('posterior mean', suite.Mean())


if __name__ == '__main__':
    main()
