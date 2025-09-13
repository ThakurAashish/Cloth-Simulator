from pygame.draw import line


class ConstrainHandler:
    def __init__(self):
        pass

    def update(self, constrain, display=None):
        '''
        0 -> particle 1
        1 -> particle 2
        2 -> length
        3 -> particle 1 is fix
        4 -> particle 2 is fix
        '''
        vec = constrain[1].position - constrain[0].position
        dD = vec.magnitude() - constrain[2]
        vec.scale_to_length(dD)
        if display is not None:
            line(display, (255, 250, 0), constrain[0].position, constrain[1].position, 1)
            line(display, (55, 0, 255), constrain[0].position, constrain[0].position + vec, 3)
        if dD != 0:
            constrain[0].position += vec / 2
            constrain[0].velocity += vec / 2
            constrain[1].position -= vec / 2
            constrain[1].velocity -= vec / 2
