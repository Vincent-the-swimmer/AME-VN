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

define a = Character("Ame",
    callback=lambda event, **kw: dim_others("ame1", event, **kw))

define k = Character("Kai",
    callback=lambda event, **kw: dim_others("kai1", event, **kw))

define c = Character("Cole",
    callback=lambda event, **kw: dim_others("cole1", event, **kw))

define h = Character("Hina",
    callback=lambda event, **kw: dim_others("hina1", event, **kw))