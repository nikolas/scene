import math
import random
from particle_factory import ParticleFactory

SLIDES = (
    [
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 2, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 2, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 2, 1, 1, 1, 1,
        1, 2, 1, 1, 1, 1, 1, 1, 1, 2,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 2,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 2,
    ],
    # [
    #     1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    #     1, 1, 1, 1, 2, 1, 1, 1, 1, 1,
    #     1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    #     1, 2, 1, 1, 1, 1, 1, 1, 1, 1,
    #     1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    #     1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    #     1, 1, 1, 1, 1, 2, 1, 1, 1, 1,
    #     1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    #     1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    #     1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    # ],
)


class Slide():
    slide = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
        0, 0, 1, 0, 0, 0, 1, 1, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
    ]

    def __init__(self, pos=0, factory=None):
        self.pos = pos

        if factory is None:
            self.factory = ParticleFactory(i=(pos*100))
        else:
            self.factory = factory

    def make(self):
        for i, el in enumerate(self.slide):
            if math.sin(i) > 0:
                self.slide[i] = 1
            else:
                self.slide[i] = 0

        self.slide = random.choice(SLIDES)

        """Returns the list of ElementTree elements for this slide."""
        slide = []
        for i, el in enumerate(self.slide):
            xpos = i % 10 - 0.5 + random.random()
            ypos = (i / 10) + (11 * self.pos) - 0.5 + random.random()
            if el == 1:
                slide.append(self.factory.make_particle(
                    px=xpos,
                    py=ypos,
                    radius=(0.1),
                ))
                slide.append(self.factory.make_particlecolor())
                slide.append(self.factory.make_particlepath())
                if i < len(self.slide) - 10:
                    slide.append(self.factory.make_edge())
                    slide.append(self.factory.make_edgecolor())
            elif el == 2:
                slide.append(self.factory.make_particle(
                    px=xpos,
                    py=ypos,
                    radius=(i % 2 / 2),
                ))
                slide.append(self.factory.make_particlecolor())
        return slide
