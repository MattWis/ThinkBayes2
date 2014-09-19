from __future__ import print_function, division

import thinkbayes2

class Turtle(thinkbayes2.Suite):
    """A map from string bowl ID to probablity."""

    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        like = hypo[data] / hypo.Total()
        return like


def main():
    turtles = []
    num_turtles = 100
    for i in range(num_turtles + 1):
        turtles.append(thinkbayes2.Hist(dict(blue=i, green=num_turtles-i)))
    pmf = Turtle(turtles)

    pmf.Update('green')

    for hypo, prob in pmf.Items():
        print(hypo, prob)


if __name__ == '__main__':
    main()
