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
