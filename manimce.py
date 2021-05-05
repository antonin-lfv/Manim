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

## distance euclidienne
class distance_euclidienne(GraphScene):
    CONFIG = {
        "camera_config": {"background_color": "#000000"},
        "axes_color": WHITE,
    }
    def construct(self):
        # Distance entre les deux points
        A = Dot().move_to(LEFT * 3 + DOWN * 1.5)
        B = Dot().move_to(3 * RIGHT + 2 * UP)
        arrow1 = Line(A.get_center(), B.get_center(), buff=0.1)  # ou DashedLine
        arrow1.set_color(WHITE)
        self.play(Write(A.set_color(RED), run_time=0.2))
        self.play(Write(B.set_color(RED), run_time=0.2))
        self.play(ShowCreation(arrow1), run_time=0.2)

        # Points name
        apoint = MathTex(r"A(x_{A}, y_{A})").next_to(A,LEFT,buff=0.5)
        bpoint = MathTex(r"B(x_{B}, y_{B})").next_to(B,UP,buff=0.5)
        self.play(Write(apoint),Write(bpoint), run_time=0.2)

        # Line Y
        Y = DashedLine(B.get_bottom(), B.get_center()+3.5*DOWN)
        self.play(Write(Y.set_color(YELLOW), run_time=0.2))

        # Line X
        X = DashedLine(A.get_right(), B.get_center()+3.5*DOWN)
        self.play(Write(X.set_color(YELLOW), run_time=0.2))

        # Braces
        t1 = Brace(X, DOWN, buf=1)
        t2 = Brace(Y, RIGHT, buf=1)
        txt1 = t1.get_text("$x_{B}-x_{A}$")
        txt2 = t2.get_text("$y_{B}-y_{A}$")
        self.play(Write(t1),Write(txt1), run_time=0.2)
        self.play(Write(t2),Write(txt2), run_time=0.2)

        self.wait()
        
# 2D

# régression linéaire
class Reg_lin_final(GraphScene, MovingCameraScene):  # tracer une fonction
    def construct(self):
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(1.8)) # valeur précédente : 1.5
        self.setup_axes_1()

        # data
        np.random.seed(0)
        m = 10
        x = np.linspace(0, 3, m)
        y = x * 3 / 4 + 0.3 * np.random.randn(m)

        # créer les points + premières erreurs
        points = VGroup()
        error = VGroup()
        for i in range(len(x)):
            points.add(Dot(self.coords_to_point(x[i], y[i])).set_color(BLUE))

        # afficher les points
        self.play(FadeIn(points), run_time = 0.5)

        # creation d'un point de référence
        graph_corner = Dot(self.coords_to_point(3, 3))

        text1 = Text('modèle').set_color(YELLOW).scale(1)
        text1.next_to(graph_corner, 10 * RIGHT)
        text2 = MathTex('f(x) = ', 'a ', 'x + ', 'b').set_color(YELLOW).scale(1)
        text2.next_to(text1, 2 * DOWN)
        text3 = Text('paramètres').set_color(GREEN).scale(0.7)
        text3.next_to(text2, 3 * DOWN + 2 * RIGHT)
        framebox1 = SurroundingRectangle(text2[1], buff=0.05).set_color(GREEN)
        framebox2 = SurroundingRectangle(text2[3], buff=0.05).set_color(GREEN)

        # sliders
        a_slider = Line(start=RIGHT * 3.5 , end=RIGHT * 6.5)
        b_slider = Line(start=RIGHT * 3.5 + DOWN * 1.3, end=RIGHT * 6.5 + DOWN * 1.3)
        a_label = Text("Valeur de a ").scale(.6).next_to(a_slider, DOWN, buff=.2)
        b_label = Text("Valeur de b ").scale(.6).next_to(b_slider, DOWN, buff=.2)
        a_dot = Dot(point=RIGHT * 2.5).set_color(YELLOW)
        b_dot = Dot(point=RIGHT * 2.5 + DOWN * 1).set_color(YELLOW)
        a_value = Text("1.0").scale(.5).next_to(a_dot, UP, buff=.1)
        b_value = Text("1.0").scale(.5).next_to(b_dot, UP, buff=.1)


        func = self.get_graph(lambda x: x, x_min=-5, x_max=5, color=RED)
        a = ValueTracker(1)
        b = ValueTracker(0)

        def ReplaceGraph(mob):
            mob.become(
                self.get_graph(
                    lambda x: a.get_value() * x + b.get_value(),
                    x_min=-5, x_max=5, color=RED
                )
            )

        def MoveA(mob):
            mob.move_to([a.get_value()*2 / 2 + text1.get_x() - 0.5, a_slider.get_y(), 0])

        def MoveB(mob):
            mob.move_to([b.get_value()*2 / 2 + text1.get_x() - 0.5, b_slider.get_y(), 0])

        def ValueA(mob):
            atemp = str(round(a.get_value(), 1))
            mob.become(Text(atemp).scale(.5).next_to(a_dot, UP, buff=.1))

        def ValueB(mob):
            btemp = str(round(b.get_value(), 1))
            mob.become(Text(btemp).scale(.5).next_to(b_dot, UP, buff=.1))

        func.add_updater(ReplaceGraph)
        a_dot.add_updater(MoveA)
        b_dot.add_updater(MoveB)
        a_value.add_updater(ValueA)
        b_value.add_updater(ValueB)

        # ajout de tous les elements du slider dans un VGroup
        sliders = VGroup(a_dot, b_dot, a_value, b_value, a_slider, b_slider, a_label, b_label)

        sliders.next_to(text1, DOWN * 5)
        sliders.shift(LEFT * 0.5)

        # Lines
        line_1 = self.get_graph(lambda x : x, x_min=0, x_max=3)
        line_1.set_color(YELLOW)
        line_2 = self.get_graph(lambda x : x - 0.5, x_min=0.5, x_max=3)
        line_2.set_color(YELLOW)
        line_3 = self.get_graph(lambda x : 0.5 * x, x_min=0, x_max=3)
        line_3.set_color(YELLOW)
        line_4 = self.get_graph(lambda x : 0.4 * x + 1, x_min=0, x_max=3)
        line_4.set_color(YELLOW)
        line_5 = self.get_graph(lambda x : 0.5 * x + 0.5, x_min=0, x_max=3)
        line_5.set_color(YELLOW)
        line_6 = self.get_graph(lambda x : 0.6 * x + 0.3, x_min=0, x_max=3)
        line_6.set_color(YELLOW)

        line_7 = self.get_graph(lambda x : 0.7 * x + 1, x_min=0, x_max=3)
        line_7.set_color(YELLOW)


        self.wait(2.5)
        self.play(Write(line_1), Write(text1), run_time = 1)
        self.wait(0.5)
        self.play(Write(text2), run_time = 1)
        self.wait(3)
        self.play(Write(a_slider), Write(b_slider), Write(a_label), Write(b_label), Write(a_dot), Write(b_dot), Write(a_value), Write(b_value))

        self.play(
            Transform(line_1,line_2),
            a.animate.set_value(1),
            b.animate.set_value(-0.5),
            run_time=1
        )
        self.play(
            Transform(line_1,line_3),
            a.animate.set_value(0.5),
            b.animate.set_value(0),
            run_time=1
        )
        self.play(
            Transform(line_1,line_4),
            a.animate.set_value(0.4),
            b.animate.set_value(1),
            run_time=1
        )
        self.play(
            Transform(line_1,line_5),
            a.animate.set_value(0.5),
            b.animate.set_value(0.5),
            run_time=1
        )
        self.play(
            Transform(line_1,line_6),
            a.animate.set_value(0.6),
            b.animate.set_value(0.3),
            run_time=1
        )

        self.play(FadeOut(a_value), FadeOut(b_value), run_time=1)

        self.play(FadeOut(line_1),FadeOut(text1), FadeOut(text2),
            FadeOut(a_slider), FadeOut(b_slider), FadeOut(a_label), FadeOut(b_label),
            FadeOut(a_dot), FadeOut(b_dot),
            run_time=1
        )


        error = VGroup()
        for i in range(len(x)):
            error.add(Line(points[i].get_bottom(), Dot(self.coords_to_point(x[i], 0.27 * x[i] + 0.1)).get_center()).set_color(RED))


        new_error = VGroup()
        for i in range(len(x)):
            new_error.add(Line(points[i].get_bottom(), Dot(self.coords_to_point(x[i], 0.7 * x[i] + 1)).get_center()).set_color(RED))

        new_error_2 = VGroup()
        for i in range(len(x)):
            new_error_2.add(Line(points[i].get_bottom(), Dot(self.coords_to_point(x[i], 0.5 * x[i] + 0.5)).get_center()).set_color(RED))


        self.wait(2)
        # algo_opt = Text('Algorithme d\'Optimisation').set_color(GREEN)
        # algo_opt.shift(4 * UP + 6 * LEFT)
        # self.play(Write(algo_opt), run_time = 1)

        first_line = Line(Dot(self.coords_to_point(0, 0.1)).get_center(),Dot(self.coords_to_point(3, 0.9)).get_center()).set_color(YELLOW)
        self.setup_axes_2()
        dist_text = Tex('Distance').set_color(RED)
        dist_text.next_to(self.y_axis, UP + RIGHT)
        # iter_text = Tex('Itération')
        # iter_text.next_to(self.x_axis, DOWN + 3 * RIGHT)
        self.play(Write(first_line), Write(error), Write(self.x_axis), Write(self.y_axis), Write(dist_text), run_time=3)

        graphe1 = self.get_graph(lambda x: (x - 1.5) ** 2 + 0.5, color=RED, x_min=0.2, x_max=2.3)
        graphe2 = self.get_graph(lambda x: (x - 1.5) ** 2 + 0.5, color=RED, x_min=2.3, x_max=1.5)
        #graphe4 = self.get_graph(lambda x: (x - 1.5) ** 2 + 0.5, color=RED, x_min=0.1, x_max=2.8)


        # animations
        d_1 = Dot(self.coords_to_point(0.2, (0.2 - 1.5) ** 2 + 0.5)).set_color(YELLOW)
        d_2 = Dot(self.coords_to_point(2.3, (2.3 - 1.5) ** 2 + 0.5)).set_color(YELLOW)
        d_3 = Dot(self.coords_to_point(1.5,  0.5)).set_color(YELLOW)
        path = VMobject()
        path.set_points_as_corners([d_1.get_center(), d_1.get_center()])
        def update_path(path):
            previous_path = path.copy().set_color(RED)
            previous_path.add_points_as_corners([d_1.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)

        error_a = ValueTracker(0.2)
        error_a_2 = ValueTracker(2.3)
        error_value_a = Text("0.2").scale(.5).next_to(d_1, UP, buff=.1)
        error_value_a_2 = Text("2.3").scale(.5).next_to(d_2, UP, buff=.1)
        def error_update(mob):
            atemp = str(round(error_a.get_value(), 1))
            mob.become(Text(atemp).scale(.5).next_to(d_1, UP, buff=.1))
        error_value_a.add_updater(error_update)

        def error_update_2(mob):
            atemp = str(round(error_a_2.get_value(), 1))
            mob.become(Text(atemp).scale(.5).next_to(d_2, UP, buff=.1))
        error_value_a_2.add_updater(error_update_2)

        self.add(path, d_1)
        self.play(Write(error_value_a))
        self.play(Transform(first_line, line_7), Transform(error, new_error),MoveAlongPath(d_1, graphe1), error_a.animate.set_value(2.3),run_time=4)
        self.add(error_value_a_2)
        self.remove(d_1, error_value_a)

        self.play(Transform(first_line, line_5), Transform(error, new_error_2),MoveAlongPath(d_2, graphe2), error_a_2.animate.set_value(1.5),run_time=4)
        self.add(d_3)

        dashed_line_a = self.get_vertical_line_to_graph(1.5, graphe2, DashedLine, color=YELLOW)
        a_optimum = Tex("a optimum").next_to(Dot(self.coords_to_point(1.5,0)), DOWN).set_color(YELLOW)
        self.play(Write(dashed_line_a), Write(a_optimum))
        self.wait()

    def setup_axes_1(self, **kwargs):
        self.x_max = 3
        self.y_max = 3
        self.x_min = 0
        self.y_min = 0
        self.axes_color = WHITE
        self.graph_origin = 3 * DOWN + 10 * LEFT
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        GraphScene.setup_axes(self)
        self.y_axis.label_direction = UP
        self.x_axis.label_direction = RIGHT
        self.play(Write(self.x_axis), Write(self.y_axis), run_time=1)

    def setup_axes_2(self, **kwargs):
        self.x_max = 5
        self.y_max = 5
        self.x_min = 0
        self.y_min = 0
        self.axes_color = WHITE
        self.graph_origin = 3 * DOWN + RIGHT
        self.x_axis_label = "a"
        self.y_axis_label = ""
        GraphScene.setup_axes(self)
        self.y_axis.label_direction = UP
        self.x_axis.label_direction = RIGHT


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

## sigmoid
class D2_sigmoid(GraphScene):  # tracer une fonction
    def construct(self):
        self.y_max = 1
        self.y_min = -1
        self.x_max = 7
        self.x_min = -7
        self.y_tick_frequency = 0.25
        self.axes_color = WHITE
        self.graph_origin = ORIGIN
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        sigmoid_txt = MathTex(r"Fonction Sigmoid : \frac{1}{1+e^{-x}}")
        self.play(Write(sigmoid_txt))
        self.wait(1)
        self.play(sigmoid_txt.animate.shift(DOWN * 2 + LEFT * 3.5).scale(0.7),
                  run_time=1)

        self.setup_axes()
        graph = self.get_graph(lambda x: 1 / (1 + np.exp(-x)), color=RED)
        self.play(ShowCreation(graph), run_time=4)

    def setup_axes(self, **kwargs):
        GraphScene.setup_axes(self)
        self.y_axis.label_direction = UP
        self.x_axis.label_direction = RIGHT
        self.play(Write(self.x_axis), Write(self.y_axis))        
        
        
## Évolution d'une épidémie 
class sim_virus_courbes(GraphScene, MovingCameraScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            graph_origin=DOWN * 2.3 + LEFT * 0.95,
            x_axis_visibility=False,
            y_axis_visibility=False,
            **kwargs
        )

    def construct(self):
        self.camera.background_color = '#FFFFFF'
        def distance_e(x, y):  # distance entre 2 points du plan cartésien
            return distance.euclidean([x[0], x[1]], [y[0], y[1]])

        def chance_infecte(p):  # return True si il devient infecté avec une proba p
            proba = int(p * 100)
            return rd.randint(0, 100) <= proba

        def immuniser(l, l2, p):  # l: infectés; l2: immunisés précédents
            drop = 0
            for i in range(len(l)):
                proba = int(p * 100)
                if rd.randint(0, 100) <= proba:
                    l2.append(l[i - drop])
                    l.remove(l[i - drop])
                    drop += 1
            return l, l2

        def deces(l, l2, l3, p):  # l: infectés; l2: décès précédents; l3: immunisés
            l_p = l[:]  # création d'une copie pour éviter erreur d'indice
            for i in range(len(l_p)):
                proba = int(p * 100)
                if rd.randint(0, 100) <= proba and l_p[i] not in l3:
                    l2.append(l_p[i])
                    l.remove(l_p[i])
            return l, l2

        # Caméra et axes ############
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(1.2).move_to(2*DOWN))  # 0.65
        self.setup_axes()

        # Paramètres virus ##############

        nb_individu = 5000  # recommandé : 500 à 10000
        variance_pop = 1  # recommandé : 1
        rayon_contamination = 0.6  # recommandé : 0.5
        infectiosite = 0.1  # recommandé : 10%
        p = 0.1  # recommandé : 10%
        d = 0.05  # recommandé : 5%

        # dataset
        x, y = make_blobs(n_samples=nb_individu, centers=1, cluster_std=variance_pop)
        df = pd.DataFrame(dict(x=x[:, 0],
                               y=x[:, 1]))

        # création des courbes finales et listes des coordonnées
        data = dict(courbe_sains=[], coord_infectes=[], coord_sains=[], coord_immunises=[], coord_deces=[])
        numero_infecte_1 = rd.randint(0, nb_individu - 1)  # on choisit le premier individu infecté au hasard
        coord_1er_infecte = [df['x'][numero_infecte_1], df['y'][numero_infecte_1]]  # coordonnées du 1er infecté

        # Remplissage des listes
        for k in range(nb_individu):
            if k == numero_infecte_1:
                data['coord_infectes'].append(coord_1er_infecte)
            else:
                data['coord_sains'].append([df['x'][k], df['y'][k]])

        data['courbe_sains'].append(nb_individu - 1)

        ## plot
        sains_1 = VGroup()
        infect_1 = VGroup()
        dece_1 = VGroup()
        immun_1 = VGroup()

        # first points
        for i in data['coord_sains']:
            sains_1.add(Dot(self.coords_to_point(i[0], i[1])).scale(0.3).set_color('#2358DA'))
        for i in data['coord_infectes']:
            infect_1.add(Dot(self.coords_to_point(i[0], i[1])).scale(0.3).set_color('#FB0D0D'))
        for i in data['coord_deces']:
            dece_1.add(Dot(self.coords_to_point(i[0], i[1])).scale(0.3).set_color('#BE11C9'))
        for i in data['coord_immunises']:
            immun_1.add(Dot(self.coords_to_point(i[0], i[1])).scale(0.3).set_color('#0DC501'))

        # jour 1
        points_dico = [dict(sains = sains_1,infecte = infect_1,deces = dece_1, immunise = immun_1)]
        courbes_dico = [dict(sains=[0,5*len(data['coord_sains'])/nb_individu],
                             infecte=[0,5*len(data['coord_infectes'])/nb_individu],
                             deces=[0,5*len(data['coord_deces'])/nb_individu],
                             immunise=[0,5*len(data['coord_immunises'])/nb_individu])]

        # jours 2 à n
        jour=1
        while len(data['coord_infectes']) > 0.08 * nb_individu or len(data['courbe_sains']) < 10:  # condition d'arrêt

            for k in range(len(data['coord_infectes'])):
                non_sains = 0
                for j in range(len(data['coord_sains'])):
                    if distance_e(data['coord_infectes'][k],data['coord_sains'][j - non_sains]) < rayon_contamination and data['coord_sains'][j - non_sains] not in data['coord_infectes'] and chance_infecte(infectiosite):
                        data['coord_infectes'].append(data['coord_sains'][j - non_sains])
                        data['coord_sains'].remove(data['coord_sains'][j - non_sains])
                        non_sains += 1

            coord_infectes1, data['coord_immunises'] = immuniser(data['coord_infectes'], data['coord_immunises'], p)
            data['coord_infectes'], data['coord_deces'] = deces(coord_infectes1, data['coord_deces'],
                                                                data['coord_immunises'], d)
            data['courbe_sains'].append(len(data['coord_sains']))

            # plot des points
            sains_2 = VGroup()
            infect_2 = VGroup()
            dece_2 = VGroup()
            immun_2 = VGroup()
            for i in data['coord_sains']:
                sains_2.add(Dot(self.coords_to_point(i[0], i[1])).scale(0.3).set_color('#2358DA'))
            for i in data['coord_infectes']:
                infect_2.add(Dot(self.coords_to_point(i[0], i[1])).scale(0.3).set_color('#FB0D0D'))
            for i in data['coord_deces']:
                dece_2.add(Dot(self.coords_to_point(i[0], i[1])).scale(0.3).set_color('#BE11C9'))
            for i in data['coord_immunises']:
                immun_2.add(Dot(self.coords_to_point(i[0], i[1])).scale(0.3).set_color('#0DC501'))


            points_dico.append(dict(sains=sains_2,infecte=infect_2,deces=dece_2,immunise=immun_2))
            courbes_dico.append(dict(sains=[jour, 5*len(data['coord_sains']) /nb_individu],
                                 infecte=[jour, 5*len(data['coord_infectes']) / nb_individu],
                                 deces=[jour, 5*len(data['coord_deces']) / nb_individu],
                                 immunise=[jour, 5*len(data['coord_immunises']) / nb_individu]))
            jour+=1

        # afficher jour 0 à n
        self.setup_axes()
        self.add(points_dico[0]['sains'], points_dico[0]['infecte'], points_dico[0]['deces'],points_dico[0]['immunise'])
        self.setup_axes_2()
        self.add(Dot(self.coords_to_point(courbes_dico[0]['sains'][0], courbes_dico[0]['sains'][1])).set_color('#2358DA').scale(0.5),
                 Dot(self.coords_to_point(courbes_dico[0]['infecte'][0], courbes_dico[0]['infecte'][1])).set_color('#FB0D0D').scale(0.5),
                 Dot(self.coords_to_point(courbes_dico[0]['deces'][0], courbes_dico[0]['deces'][1])).set_color('#BE11C9').scale(0.5),
                 Dot(self.coords_to_point(courbes_dico[0]['immunise'][0], courbes_dico[0]['immunise'][1])).set_color('#0DC501').scale(0.5))

        self.wait(1)
        for i in range (1,jour):
            self.setup_axes()
            self.add(points_dico[i]['sains'],points_dico[i]['infecte'],points_dico[i]['deces'],points_dico[i]['immunise'])
            self.setup_axes_2()
            self.add(Dot(self.coords_to_point(courbes_dico[i]['sains'][0]*18/jour,courbes_dico[i]['sains'][1])).set_color('#2358DA').scale(0.5),
                     Dot(self.coords_to_point(courbes_dico[i]['infecte'][0]*18/jour,courbes_dico[i]['infecte'][1])).set_color('#FB0D0D').scale(0.5),
                     Dot(self.coords_to_point(courbes_dico[i]['deces'][0]*18/jour,courbes_dico[i]['deces'][1])).set_color('#BE11C9').scale(0.5),
                     Dot(self.coords_to_point(courbes_dico[i]['immunise'][0]*18/jour,courbes_dico[i]['immunise'][1])).set_color('#0DC501').scale(0.5),
                     Line(Dot(self.coords_to_point(courbes_dico[i-1]['sains'][0]*18/jour,courbes_dico[i-1]['sains'][1])).scale(0.5).get_center(),Dot(self.coords_to_point(courbes_dico[i]['sains'][0]*18/jour,courbes_dico[i]['sains'][1])).scale(0.5).get_center(),width=0.8).set_color('#2358DA'),
                     Line(Dot(self.coords_to_point(courbes_dico[i-1]['infecte'][0]*18/jour,courbes_dico[i-1]['infecte'][1])).scale(0.5).get_center(),Dot(self.coords_to_point(courbes_dico[i]['infecte'][0]*18/jour,courbes_dico[i]['infecte'][1])).scale(0.5).get_center(),width=0.8).set_color('#FB0D0D'),
                     Line(Dot(self.coords_to_point(courbes_dico[i-1]['deces'][0]*18/jour,courbes_dico[i-1]['deces'][1])).scale(0.5).get_center(),Dot(self.coords_to_point(courbes_dico[i]['deces'][0]*18/jour,courbes_dico[i]['deces'][1])).scale(0.5).get_center(),width=0.8).set_color('#BE11C9'),
                     Line(Dot(self.coords_to_point(courbes_dico[i-1]['immunise'][0]*18/jour,courbes_dico[i-1]['immunise'][1])).scale(0.5).get_center(),Dot(self.coords_to_point(courbes_dico[i]['immunise'][0]*18/jour,courbes_dico[i]['immunise'][1])).scale(0.5).get_center(),width=0.8).set_color('#0DC501'))
            self.wait(1)

        self.wait(0.5)

    def setup_axes_2(self, **kwargs):
        self.graph_origin = DOWN * 5.5 + LEFT * 7,
        GraphScene.setup_axes(self)

## skewness et kurtosis
class skewness_kurt(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min = 0,
            x_max = 4,
            y_min = -2,
            y_max = 4,
            graph_origin = DOWN + LEFT * 4,
            **kwargs)

    def construct(self):

        # Intro
        skew_intro = Text("Coefficient d'asymétrie : Skewness")
        self.play(FadeIn(skew_intro))
        self.wait(2)
        self.setup_axes()

        # skewness nul
        skewn_nul = self.get_graph(lambda x : 5/np.sqrt(2*np.pi)*np.exp(-0.5*(x-2)**2))
        nul = Text("Skewness nul, la distribution est centrée")
        self.add(skewn_nul)
        self.play(
            Transform(skew_intro, nul.move_to(RIGHT*1+UP * 2).scale(0.5).set_color(BLUE))
        )
        self.wait(5)

        # à gauche, skewness positif
        dist_name = "gamma"
        dist = getattr(scipy.stats, dist_name)
        length = 30000
        bins = 500
        data = np.random.gamma(2, 1, length)
        param = dist.fit(data)
        loc = param[-2]
        scale = param[-1]
        arg = param[:-2]
        y, x = np.histogram(data, bins=bins, density=True)
        x = (x + np.roll(x, -1))[:-1] / 2.0
        skewn_pos = self.get_graph(lambda x : 5*dist.pdf(x, loc=loc, scale=scale, *arg))
        pos = Text("Skewness positif, la distribution est oblique à gauche, étalée à droite")
        self.play(
            Transform(skewn_nul, skewn_pos),
            Transform(skew_intro, pos.move_to(RIGHT*1+UP * 2).scale(0.5).set_color(GREEN))
        )
        self.wait(5)

        # à droite, skewness négatif
        skewn_neg = self.get_graph(lambda x : 5*dist.pdf(x, loc=loc, scale=scale, *arg)).flip(UP)
        neg = Text("Skewness négatif, la distribution est oblique à droite, étalée à gauche")
        self.play(
            Transform(skewn_nul, skewn_neg),
            Transform(skew_intro, neg.move_to(RIGHT*1+UP * 2).scale(0.5).set_color(YELLOW))
        )
        self.wait(5)
        V = VGroup()
        V.add(skew_intro, self.axes)
        self.remove(skewn_nul)

        d=Text("Coefficient d'aplatissment : Kurtosis")
        self.play(
            Transform(V, d)
        )
        self.wait(5)
        self.remove(V)
        self.setup_axes()

        # Loi normale : kurtosis nul
        kurt_nul = self.get_graph(lambda x : 5/np.sqrt(2*np.pi)*np.exp(-0.5*(x-2)**2))
        nul = Text("Kurtosis nul, la distribution est aplatie comme la loi normale")
        self.add(kurt_nul)
        self.play(
            Transform(d, nul.move_to(RIGHT*1+UP * 2).scale(0.5).set_color(BLUE))
        )
        self.wait(5)

        # kurtosis positif
        kurt_pos = self.get_graph(lambda x : 8/np.sqrt(2*np.pi)*np.exp(-0.5*(x-2)**2))
        pos = Text("Kurtosis positif, la distribution est moins aplatie que la loi normale")
        self.play(
            Transform(kurt_nul,kurt_pos),
            Transform(d, pos.move_to(RIGHT*1+DOWN * 2).scale(0.5).set_color(GREEN))
        )
        self.wait(5)

        # kurtosis négatif
        kurt_neg = self.get_graph(lambda x : 2/np.sqrt(2*np.pi)*np.exp(-0.5*(x-2)**2))
        pos = Text("Kurtosis négatif, la distribution est plus aplatie que la loi normale")
        self.play(
            Transform(kurt_nul, kurt_neg),
            Transform(d, pos.move_to(RIGHT*1+DOWN * 2).scale(0.5).set_color(YELLOW))
        )
        self.wait(5)
        self.remove(
            kurt_nul, d
        )
        d=Dot()
        self.play(
            Transform(self.axes, d)
        )
        self.wait()

# 3D

## descente de gradient
class Gradient_descent_3D(ThreeDScene):
    def construct(self):
        ####### 3D
        self.y_tick_frequency = 0.5
        self.x_tick_frequency = 0.5
        self.graph_origin = ORIGIN
        resolution_fa = 30
        self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES, distance=7)

        def param_plane(u, v):
            x = u
            y = v
            z = 0
            return np.array([x, y, z])

        plane = ParametricSurface(
            param_plane,
            resolution=(resolution_fa, resolution_fa),
            v_min=-1,
            v_max=+1,
            u_min=-1,
            u_max=+1,
        )
        plane.scale_about_point(2, ORIGIN)

        def f(x,y):
            return 0.5*(0.5*x+0.5*y)**2+0.5*(0.5*x-0.5*y)**2

        def param_carree(u, v):
            x = u
            y = v
            z = f(x,y)
            return np.array([x, y, z])

        carree_plane = ParametricSurface(
            param_carree,
            resolution=(resolution_fa, resolution_fa),
            v_min=-2,
            v_max=+2,
            u_min=-2,
            u_max=+2,
        )

        carree_plane.scale_about_point(1, ORIGIN)
        carree_plane.set_style(fill_opacity=1)
        plane.set_style(fill_color=GREEN, fill_opacity=0.9)
        carree_plane.set_style(stroke_color=GREEN)
        carree_plane.set_fill_by_checkerboard(BLACK, opacity=0.9)

        axes = ThreeDAxes()

        self.add(axes)
        self.play(Write(plane))
        self.begin_ambient_camera_rotation(rate=-0.4)
        self.play(Transform(plane, carree_plane), run_time=4)
        for i in np.linspace(-1.8,0,10):
            d = Dot(axes.coords_to_point(0, i, f(0, i))).scale(0.8).set_color(RED)
            self.add(d)
            self.wait(0.8)
            self.remove(d)
        for i in np.linspace(0.1,0.3,5):
            d = Dot(axes.coords_to_point(0, i, f(0, i))).scale(0.8).set_color(RED)
            self.add(d)
            self.wait(0.8)
            self.remove(d)
        for i in np.linspace(0.2, 0, 5):
            d = Dot(axes.coords_to_point(0, i, f(0, i))).scale(0.8).set_color(RED)
            self.add(d)
            self.wait(0.7)
            self.remove(d)
        self.add(Dot(axes.coords_to_point(0, 0, f(0, 0))).scale(0.8).set_color(RED))
        self.wait(7)
        self.stop_ambient_camera_rotation()
        self.wait()

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
