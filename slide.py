import math
import random
from particle_factory import ParticleFactory


class Slide():
    slide = []
    i = 0
    def __init__(self, pos=0, factory=None):
        self.pos = pos

        if factory is None:
            self.factory = ParticleFactory(i=(pos*100))
        else:
            self.factory = factory

    def make(self):
        """Returns the list of ElementTree elements for this slide."""
        slide = []
        xpos = 1 - 0.9 + random.random()
        ypos = (11 * self.pos) - 0.5 + random.random()
        slide.append(self.factory.make_particle(
            px=xpos,
            py=ypos,
            radius=(0.01),
        ))
        self.i += 1
        slide.append(self.factory.make_particlecolor())
        slide.append(self.factory.make_particlepath())

        slide.append(self.factory.make_particle(
            px=xpos+0.4,
            py=ypos+0.2,
            radius=(1 * 0.2),
        ))
        for i in range(100):
            ii = i * random.random()
            slide.append(self.factory.make_particle(px=ii))
        for i in range(50):
            slide.append(self.factory.make_edge(i-1, i))
        #slide.append(self.factory.make_edgecolor())

        slide.append(self.factory.make_particlecolor())
        return slide
