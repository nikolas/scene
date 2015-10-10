import math
import random
from xml.etree import ElementTree as ET


class ParticleFactory:
    def __init__(self, i=0):
        self.i = i

    def make_particle(self, m=1, px=1, py=1, vx=0,
                      vy=1, fixed=0, radius=0.5):
        el = ET.Element(
            'particle', {
                'm': str(m + random.random() * 10),
                'px': str(px),
                'py': str(py),
                'vx': str(vx),
                'vy': str(vy - 0.5 + random.random()),
                'fixed': str(fixed),
                'radius': str(radius),
                'tag': 'teleport',
            })

        self.i += 1
        return el

    def make_particlecolor(self):
        return ET.Element(
            'particlecolor', {
                'i': str(max(self.i-1, 0)),
                'r': random.choice(('0.8', '0.9')),
                'g': '0.8',
                'b': str(math.sin((self.i) % 10 * 0.2)),
            })

    def make_particlepath(self):
        return ET.Element(
            'particlepath', {
                'i': str(max(self.i-1, 0)),
                'duration': '10.0',
                'r': random.choice(('0.85', '0.9')),
                'g': random.choice(('0.89', '0.9')),
                'b': random.choice(('0.82', '0.9')),
            })

    def make_edge(self):
        return ET.Element(
            'edge', {
                'i': str(max(self.i-1, 0)),
                'j': str(self.i),
                'radius': '0.1',
            })

    def make_edgecolor(self):
        return ET.Element(
            'edgecolor', {
                'i': str(min(max(self.i, 0), 80)),
                'r': random.choice(('0.0', '0')),
                'g': random.choice(('0.0', '0')),
                'b': random.choice(('0.0', '0')),
            })
