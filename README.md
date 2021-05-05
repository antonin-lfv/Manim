<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116782710-0b330080-aa8b-11eb-9add-3fb93a94655d.png" height="200">
<p/>

<br/>


<p align="center">
Dans ce Github je vais partager des animations réalisées avec Manim, une librairie python développée par le YouTubeur 3Blue1Brown, qui permet de créer des animations de façon puissante et épurée. J'utilise ici la version 4.0 de Manim CE (Community Edition) qui est la version de Manim régulièrement mise à jour par la communauté et qui est la plus stable. Si vous voulez utilisez Manim l'installation est détaillée sur le site Manim community. 
	
<br/>
<p/>

<br/>

# Index

1. [Exemples basiques](#Exemples-basiques)
	- [Formules latex](#Formules-latex)
	- [identités remarquables](#identités-remarquables)
	- [Aligner du texte](#Aligner-du-texte)
	- [Ligne couleurs gradient](#Ligne-couleurs-gradient)
	- [Animation carré déformé](#Animation-carré-déformé)
	- [Déplacement disque](#Déplacement-disque)
	- [Distance Euclidienne](#Distance-Euclidienne)
2. [Graphiques 2D](#Graphiques-2D)
	- [Polygone](#Polygone)
	- [Ligne verticale sous une courbe](#Ligne-verticale-sous-une-courbe)
	- [Sigmoid](#Sigmoid)
	- [Évolution d'une épidémie](#évolution-dune-épidémie)
	- [Skewness et kurtosis](#Skewness-et-kurtosis)
3. [Graphiques 3D](#Graphiques-3D)
	- [Descente de Gradient](#Descente-de-Gradient)
4. [Animations SVG](#Animations-SVG)
	- [Stickman](#Stickman)


# Exemples basiques

<br/>

## Formules latex

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116814422-3126d680-ab59-11eb-8f6a-bacefb3eeaed.gif" height="350">
<p/>

<details>
  <summary >Code</summary>
	
```python 
class latex_formules(Scene): 
    def construct(self):
        latex = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        self.play(FadeInFrom(latex))
	self.wait() 
```

</details>

<br/>

## Identités remarquables

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/117114850-a0384100-ad8c-11eb-8661-9f693e2f5369.gif" height="350">
<p/>

<details>
  <summary>Code</summary>

```py
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

```
</details>

<br/>

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/117114404-1b4d2780-ad8c-11eb-949d-91e5afe31f37.gif" height="350">
<p/>

<details>
  <summary>Code</summary>

```py
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

```
</details>


## Aligner du texte

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116814430-3d129880-ab59-11eb-9d5f-674b6488c26c.gif" height="350">
<p/>

<details>
  <summary>Code</summary>
	
```py
class Aligner_text(Scene):
    def construct(self):
        text1 = Tex("text1").shift(2 * UL)  # UpLeft
        text2 = Tex("text2")
        text3 = Tex("text3").shift(2 * DR)  # DownRight
        group = VGroup(text1, text2, text3).scale(1.1)
        self.add(group)
        self.play(group.animate.arrange(RIGHT, .25, center=False))
```

</details>
<br/>

## Ligne couleurs gradient

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116814437-4b60b480-ab59-11eb-89bf-99db2bfba138.gif" height="350">
<p/>

<details>
  <summary>Code</summary>
	
```py
class LigneGradient(Scene):
    def construct(self):
        line_gradient = Line(LEFT * 4, RIGHT * 4)
        line_gradient.set_color(color=[PURPLE, BLUE, YELLOW, GREEN, RED])
        self.add(line_gradient)
        self.wait()
```
</details>

<br/>

## Animation carré déformé

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116870605-1a44ba80-ac13-11eb-8072-09fe52358a35.gif" height="350">
<p/>

<details>
  <summary >Code</summary>
	
```python 
class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()
```

</details>

<br/>

## Déplacement disque

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116870651-2b8dc700-ac13-11eb-8b8e-2536f580eabe.gif" height="350">
<p/>

<details>
  <summary >Code</summary>
	
```python 
class movecircle(Scene):
    def construct(self):
        sphere = Sphere().set_color(RED)
        self.add(sphere)
        self.play(ApplyMethod(sphere.shift, UP), run_time=2)
        self.play(ApplyMethod(sphere.scale, 0.4), run_time=2)
        self.wait()
```

</details>

<br/>

## Distance Euclidienne

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116870660-2f214e00-ac13-11eb-9588-56b55423cde0.gif" height="350">
<p/>

<details>
  <summary >Code</summary>
	
```python 
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
```

</details>

<br/>

# Graphiques 2D

<br/>

## Polygone

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116814445-561b4980-ab59-11eb-979f-dd322a001660.gif" height="350">
<p/>

<details>
  <summary>Code</summary>
	
```py
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
```
</details>

<br/>

## Ligne verticale sous une courbe

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116870663-30527b00-ac13-11eb-938c-87f8132376a9.gif" height="350">
<p/>

<details>
  <summary >Code</summary>
	
```python 
class Plot_line(GraphScene):
    def construct(self):
        self.setup_axes()
        self.v_graph = self.get_graph(lambda x: 4 * x - x ** 2, x_min=0, x_max=4)
        self.variable_point_label = "x_0"
        self.add_T_label(x_val=1)
        self.add(self.v_graph)
        self.wait()
```

</details>

<br/>

## Sigmoid

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116870640-2892d680-ac13-11eb-8af1-8ee91c0ef5c9.gif" height="350">
<p/>

<details>
  <summary >Code</summary>
	
```python 
class sigmoid(GraphScene):
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
```

</details>

<br/>

## Évolution d'une épidémie

<p align="center">
<img src="https://user-images.githubusercontent.com/63207451/114284499-b1718480-9a50-11eb-8b13-a7803d66c94f.gif" width="600">
	<p/>
	
<details>
  <summary >Code</summary>
	
```py
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
```
</details>
<br/>

## Skewness et kurtosis

<br/> 
<br/>

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116815034-fa05f480-ab5b-11eb-8f4b-29fd98e034ba.gif" height="350">
<p/>

<details>
  <summary>Code</summary>
	
```py
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
```
</details>

<br/>

# Graphiques 3D

<br/>

## Descente de gradient

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/117108691-d8875180-ad83-11eb-83b0-42ef904829bc.gif" height="350">
<p/>

<details>
  <summary >Code</summary>
	
```python 
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
```

</details>

<br/>


# Animations SVG

<br/>

## Stickman

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116814462-67fcec80-ab59-11eb-84bd-81e2a6e5e6b0.gif" height="350">
<p/>

<details>
  <summary>Code</summary>
	
```py
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
```

</details>

<br/>

<br/>

<br/>

<p align="center"><a href="#Index"><img src="http://randojs.com/images/backToTopButton.png" alt="Haut de la page" height="29"/></a></p>

<br/>


<p align="center">
  <a href="https://github.com/antonin-lfv" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97302854-e484da80-1859-11eb-9374-5b319ca51197.png" title="GitHub" width="40" height="40"></a>
  <a href="https://www.linkedin.com/in/antonin-lefevre-565b8b141" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303444-b2c04380-185a-11eb-8cfc-864c33a64e4b.png" title="LinkedIn" width="40" height="40"></a>
  <a href="mailto:antoninlefevre45@icloud.com" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303543-cec3e500-185a-11eb-8adc-c1364e2054a9.png" title="Mail" width="40" height="40"></a>
</p>


---------------------------
