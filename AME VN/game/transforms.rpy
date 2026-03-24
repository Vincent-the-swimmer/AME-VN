init python:
    _speakers = {}  # tracks shown sprites per character

    def dim_others(speaking_tag, event, **kwargs):
        if event != "begin":
            return
        for tag, transforms in _speakers.items():
            if tag == speaking_tag:
                renpy.show(tag, at_list=[active])
            else:
                renpy.show(tag, at_list=[inactive])

transform active:
    linear 0.2 matrixcolor IdentityMatrix()

transform inactive:
    linear 0.2 matrixcolor BrightnessMatrix(-0.35)