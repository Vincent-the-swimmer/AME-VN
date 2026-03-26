transform quick_jump:
    yoffset 0
    zoom 1.0
    linear 0.08 yoffset -40 zoom 1.04
    linear 0.08 yoffset 0 zoom 1.0

transform descend_from_top:
    yoffset -500
    alpha 0.0
    linear 0.40 yoffset 0 alpha 1.0

transform tossed_into_portal_right:
    xoffset 0
    yoffset 0
    rotate 0
    zoom 1.0
    alpha 1.0
    linear 0.04 xoffset -20 rotate -4
    linear 0.20 xoffset 900 yoffset -120 rotate 16 zoom 0.85 alpha 0.0

define whiteflash = Fade(0.05, 0.0, 0.20, color="#ffffff")

transform shake_hard:
    xoffset 0
    yoffset 0
    linear 0.02 xoffset -16 yoffset 6
    linear 0.02 xoffset 16 yoffset -6
    linear 0.02 xoffset -12 yoffset 4
    linear 0.02 xoffset 12 yoffset -4
    linear 0.02 xoffset 0 yoffset 0

# Fireball

transform slow_house_zoom:
    zoom 1.0
    xalign 0.5
    yalign 0.5
    linear 0.7 zoom 1.08


transform fireball_trail(
    start_x=0.82,
    start_y=-0.56,
    end_x=-0.06,
    end_y=0.42,
    start_zoom=0.55,
    end_zoom=1.55,
    start_rot=34,
    end_rot=34,
    fade_in=0.03,
    travel_time=0.78
):
    xpos start_x
    ypos start_y
    zoom start_zoom
    rotate start_rot
    alpha 0.0

    parallel:
        linear fade_in alpha 1.0

    parallel:
        easein_quad travel_time xpos end_x ypos end_y zoom end_zoom rotate end_rot


transform bg_darken_in:
    alpha 0.0
    linear 0.20 alpha 0.12
    linear 0.30 alpha 0.24
    linear 0.25 alpha 0.34


screen fireball_darkening():
    zorder 90

    # Main dimming layer: translucent, not opaque.
    add Solid("#000000") at bg_darken_in

    # Very subtle warm tint so it doesn't feel like a plain fade-to-black.
    add Solid("#2a1200") at bg_darken_in


screen fireball():
    zorder 100

    fixed:
        at fireball_trail(
            start_x=0.82,
            start_y=-0.56,
            end_x=-0.06,
            end_y=0.42,
            start_zoom=0.34,
            end_zoom=1.40,
            start_rot=34,
            end_rot=34,
            fade_in=0.03,
            travel_time=0.75
        )

        text "●":
            xpos 150
            ypos -210
            size 150
            color "#ff5a0018"

        text "●":
            xpos 120
            ypos -165
            size 135
            color "#ff6a0022"

        text "●":
            xpos 92
            ypos -126
            size 120
            color "#ff7a0030"

        text "●":
            xpos 68
            ypos -92
            size 108
            color "#ff8a0044"

        text "●":
            xpos 48
            ypos -62
            size 96
            color "#ff980066"

        text "●":
            xpos 30
            ypos -38
            size 84
            color "#ffb02088"

        text "●":
            xpos 14
            ypos -18
            size 94
            color "#ff6a0038"

        text "●":
            xpos 0
            ypos 0
            size 78
            color "#ff9d00dd"

        text "●":
            xpos 6
            ypos 6
            size 58
            color "#ffd15acc"

        text "●":
            xpos 14
            ypos 14
            size 36
            color "#fff4cc"

