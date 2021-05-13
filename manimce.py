from manim import *
import numpy as np
from scipy import signal
import scipy.stats
import scipy


# basique
## latex
class latex_formules(Scene):
    def construct(self):
        latex = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        self.play(FadeInFrom(latex))
        self.wait()

## identité remarquable (a-b)^2
class IR_amoinsb_2(Scene):  # (a-b)^2
    def construct(self):
        formula = TexMobject(
            "(",  # 0
            "a",  # 1
            "-",  # 2
            "b",  # 3
            ")",  # 4
            "^{2}",  # 5
            "=",  # 6
            "a",  # 7
            "^{2}",  # 8
            "-",  # 9
            "2",  # 10
            "a",  # 11
            "b",  # 12
            "+",  # 13
            "b",  # 14
            "^{2}"  # 15
        )
        formula.scale(2)
        self.play(Write(formula[0:7]))  # 0 à 6
        formula[7].set_color(RED)
        formula[14].set_color(BLUE)
        formula[11].set_color(RED)
        formula[12].set_color(BLUE)
        self.wait()
        self.play(
            ReplacementTransform(formula[1].copy(), formula[7]),
            Write(formula[8]),
            ReplacementTransform(formula[2].copy(), formula[9]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            Write(formula[13]),
            ReplacementTransform(formula[3].copy(), formula[14]),
            Write(formula[15]),
            run_time=2
        )
        self.wait(1.5)
        self.play(
            Write(formula[10]),
            ReplacementTransform(formula[1].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[12]),
            run_time=2
        )
        self.wait()

## identité remarquable a^2-b^2
class IR_a_b_2(Scene):  # a^2-b^2
    def construct(self):
        formula = Tex(
            "a",  # 0
            "^{2}",  # 1
            "-",  # 2
            "b",  # 3
            "^{2}",  # 4
            "=",  # 5
            "(",  # 6
            "a",  # 7
            "-",  # 8
            "b",  # 9
            ")",  # 10
            "(",  # 11
            "a",  # 12
            "+",  # 13
            "b",  # 14
            ")"  # 15
        )
        formula.scale(2)
        self.play(Write(formula[0:6]))  # 0 à 5
        formula[7].set_color(RED)
        formula[9].set_color(BLUE)
        formula[14].set_color(RED)
        formula[12].set_color(BLUE)
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[12]),
            Write(formula[6]), Write(formula[11]),
            Write(formula[10]), Write(formula[15]),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Write(formula[8]), Write(formula[13]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            ReplacementTransform(formula[3].copy(), formula[14]),
            run_time=1.5
        )
        self.wait()
        
## Texte en couleur et entouré
class TextColor(Scene):  # f(x)=ax+b
    def construct(self):
        text = Tex("f(x)", "=", "a", "x", "+", "b")
        text[0].set_color(WHITE)
        text[1].set_color(WHITE)
        text[2].set_color(BLUE)
        text[3].set_color(WHITE)
        text[4].set_color("#FFFFFF")  # Hexadecimal color
        text[5].set_color(RED)
        # text.to_corner(DL)

        frameBoxa = SurroundingRectangle(text[2], buff=0.8 * SMALL_BUFF)
        frameBoxa.set_stroke(BLUE, 3)
        boxtextea = Tex("{\\normalsize On fait varier a}")
        boxtextea.set_color(BLUE, 3)
        boxtextea.next_to(text[2].get_center(), UP, buff=0.7)

        frameBoxb = SurroundingRectangle(text[5], buff=0.8 * SMALL_BUFF)
        frameBoxb.set_stroke(RED)
        boxtexteb = Tex("{\\normalsize et b}")
        boxtexteb.set_color(RED)
        boxtexteb.next_to(text[5].get_center(), UP, buff=0.7)

        self.play(Write(text))
        self.wait(.1)

        self.play(ShowCreation(frameBoxa))
        self.play(Write(boxtextea))
        self.wait(0.4)
        self.remove(frameBoxa)
        self.wait(0.1)
        self.remove(boxtextea)

        self.play(ShowCreation(frameBoxb))
        self.play(Write(boxtexteb))
        self.wait(0.4)
        self.remove(frameBoxb)
        self.wait(0.1)
        self.remove(boxtexteb)
        self.wait(0.5)
        
## aligner text
class Aligner_text(Scene):
    def construct(self):
        text1 = Tex("text1").shift(2 * UL)  # UpLeft
        text2 = Tex("text2")
        text3 = Tex("text3").shift(2 * DR)  # DownRight
        group = VGroup(text1, text2, text3).scale(1.1)
        self.add(group)
        self.play(group.animate.arrange(RIGHT, .25, center=False))

## ligne couleur gradient
class LigneGradient(Scene):
    def construct(self):
        line_gradient = Line(LEFT * 4, RIGHT * 4)
        line_gradient.set_color(color=[PURPLE, BLUE, YELLOW, GREEN, RED])
        self.add(line_gradient)
        self.wait()

## deformer carré
class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()

## déplacement disque
class movecircle(Scene):
    def construct(self):
        sphere = Sphere().set_color(RED)
        self.add(sphere)
        self.play(ApplyMethod(sphere.shift, UP), run_time=2)
        self.play(ApplyMethod(sphere.scale, 0.4), run_time=2)
        self.wait(1)


# 2D


## polygone
class polygon(GraphScene):
    def construct(self):
        self.setup_axes(animate=True)
        polyg = [self.coords_to_point(0,0), #P1
                 self.coords_to_point(0,3.5), #P2
                 self.coords_to_point(3.5,1.75), #P3
                 self.coords_to_point(3.5,0), #P4
                 self.coords_to_point(0,0)] #P1 pour fermer la figure
        plol = Polygon(*polyg).move_to(UP+DOWN)
        self.play(ShowCreation(plol))

## ligne verticale sous courbe
class Plot_AO(GraphScene):
    def construct(self):
        self.setup_axes()
        self.v_graph = self.get_graph(lambda x: 4 * x - x ** 2, x_min=0, x_max=4)
        self.variable_point_label = "x_0"
        self.add_T_label(x_val=1)
        self.add(self.v_graph)
        self.wait()

# 3D

## Animation surfaces
class SurfacesAnimation(ThreeDScene):  ####### Surface
    def construct(self):
        axes = ThreeDAxes()
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)).fade(0.5)  # Resolution of the surfaces

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v) * u,
                np.sin(v) * u,
                u ** 2
            ]), v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)).scale(2)

        para_hyp = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u ** 2 - v ** 2
            ]), v_min=-2, v_max=2, u_min=-2, u_max=2, checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)).scale(1)

        cone = ParametricSurface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                u
            ]), v_min=0, v_max=TAU, u_min=-2, u_max=2, checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)).scale(1)

        hip_one_side = ParametricSurface(
            lambda u, v: np.array([
                np.cosh(u) * np.cos(v),
                np.cosh(u) * np.sin(v),
                np.sinh(u)
            ]), v_min=0, v_max=TAU, u_min=-2, u_max=2, checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(15, 32))

        ellipsoid = ParametricSurface(
            lambda u, v: np.array([
                1 * np.cos(u) * np.cos(v),
                2 * np.cos(u) * np.sin(v),
                0.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2, checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)).scale(2)

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2, checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        self.add(axes)
        self.play(Write(sphere))
        self.wait()
        self.play(ReplacementTransform(sphere, ellipsoid))
        self.wait()
        self.play(ReplacementTransform(ellipsoid, cone))
        self.wait()
        self.play(ReplacementTransform(cone, hip_one_side))
        self.wait()
        self.play(ReplacementTransform(hip_one_side, para_hyp))
        self.wait()
        self.play(ReplacementTransform(para_hyp, paraboloid))
        self.wait()
        self.play(ReplacementTransform(paraboloid, cylinder))
        self.wait()
        self.play(FadeOut(cylinder))


# SVG

## stickman
class SVGStickMan(GraphScene, MovingCameraScene):
    def construct(self):
        start_man = SVGMobject("/Users/antoninlefevre/Downloads/ManimCE/SVG_files/stick_man_plain.svg").set_color(WHITE)
        start_man_2 = SVGMobject("/Users/antoninlefevre/Downloads/ManimCE/SVG_files/stick_man_plain.svg").set_color(WHITE)
        wave_man = SVGMobject("/Users/antoninlefevre/Downloads/ManimCE/SVG_files/stick_man_wave.svg").set_color(WHITE)
        wave_man_2 = SVGMobject("/Users/antoninlefevre/Downloads/ManimCE/SVG_files/stick_man_wave.svg").set_color(WHITE)
        base = SVGMobject("/Users/antoninlefevre/Downloads/ManimCE/SVG_files/stick_man_plain.svg").set_color(WHITE)
        self.camera.frame.save_state()

        self.add(start_man.move_to(2*LEFT))
        self.add(start_man_2.move_to(2*RIGHT))
        self.play(self.camera.frame.animate.move_to(start_man.get_top()).scale(0.4))
        self.wait(0.5)
        salut = Tex("Salut !").set_color(YELLOW).next_to(start_man, UP+LEFT, buff=0.5)
        self.play(Transform(start_man, wave_man.move_to(2*LEFT)), FadeIn(salut))
        self.wait()


        self.play(self.camera.frame.animate.move_to(start_man_2.get_top()))
        self.wait(0.5)
        salut_2 = Tex("Hey !").set_color(YELLOW).next_to(start_man_2, UP+RIGHT, buff=0.5)
        self.play(Transform(start_man_2, wave_man_2.move_to(2*RIGHT)), FadeIn(salut_2))
        self.play(FadeOut(salut), FadeOut(salut_2), run_time=0.01)
        self.play(Transform(start_man, base.move_to(2 * LEFT)), Transform(start_man_2, base.copy().move_to(2 * RIGHT)))
        self.play(Restore(self.camera.frame))

## Zoom sur un neurone
class ZoomOnNeuron(ZoomedScene, MovingCameraScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.4,
            zoomed_display_height=3,
            zoomed_display_width=4,
            image_frame_stroke_width=15,
            zoomed_camera_config={
                "default_frame_stroke_width": 2,
                },
            **kwargs
        )
    def construct(self):
        # image du neurone
        neurone_1 = SVGMobject("/Users/antoninlefevre/Downloads/ManimCE/SVG_files/neuron_video.svg").set_color(WHITE).scale(3).rotate(PI/2)
        self.play(Write(neurone_1))

        # texte du zoom
        #zoomed_camera_text = Text("Dendrites", color=WHITE).scale(1.1) # box qui suit le zoom

        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(neurone_1[0].get_left())
        frame.set_color(PURPLE)

        # placer le cadre du zoom
        zd_rect = BackgroundRectangle(zoomed_display.move_to(neurone_1[0].get_left()+DOWN), fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)

        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display))

        self.play(ShowCreation(frame), direction=DOWN)
        self.activate_zooming()
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)

        self.wait(2)

        # dezoom et fin de l'animation
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
        self.wait()
