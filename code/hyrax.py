from __future__ import print_function, division

import numpy
import thinkbayes2
import thinkplot


class Hyrax(thinkbayes2.Suite):
    """Represents hypotheses about the state of the electorate."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: number of hyraxes in the environment
        data: total_tagged, found, overlap
        """
        hyraxes = hypo
        total_tagged, found, overlap = data
        p_tagged = (total_tagged + 0.0) / hyraxes

        like = thinkbayes2.EvalBinomialPmf(overlap, found, p_tagged)
        return like

def main():
    hypos = numpy.linspace(18, 500, 501 - 18)
    suite = Hyrax(hypos)
    thinkplot.Pdf(suite, label = 'prior')

    data = 10, 10, 2
    suite.Update(data)
    print(suite.Mean())
    thinkplot.Pdf(suite, label = 'post')

    thinkplot.Show()


if __name__ == "__main__":
    main()


