transform same_transform(old, new):
    old
    new with Dissolve(0.2, alpha=True)

define config.side_image_same_transform = same_transform


screen riddle1:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.6
        auto "Pylon_%s.jpg"
        action Jump("right1")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.6
        auto "Obelisk_%s.jpg"
        action Jump("wrong1")

screen riddle2:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.6
        auto "Swimming Pool_%s.jpg"
        action Jump("wrong2")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.6
        auto "Lagoon_%s.jpg"
        action Jump("right2")

screen riddle3:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.6
        auto "NALRC_%s.jpg"
        action Jump("right3")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.6
        auto "Interfaith Chapel_%s.jpg"
        action Jump("wrong3")

screen riddle5:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.6
        auto "Pylon_%s.jpg"
        action Jump("wrong5")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.6
        auto "Obelisk_%s.jpg"
        action Jump("right5")

screen riddle6:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.6
        auto "Gymnasium_%s.jpg"
        action Jump("wrong6")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.6
        auto "Swimming Pool_%s.jpg"
        action Jump("right6")

screen riddle7:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.6
        auto "Linear Park_%s.jpg"
        action Jump("wrong7")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.6
        auto "Interfaith Chapel_%s.jpg"
        action Jump("right7")

screen riddle9:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.6
        auto "Open Court_%s.jpg"
        action Jump("wrong9")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.6
        auto "Oval_%s.jpg"
        action Jump("right9")

screen riddle10:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.6
        auto "Main Building_%s.jpg"
        action Jump("wrong10")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.6
        auto "Intramuros_%s.jpg"
        action Jump("right10")

screen riddle11:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.6
        auto "Research Center_%s.jpg"
        action Jump("right11")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.6
        auto "NALRC_%s.jpg"
        action Jump("wrong11")
