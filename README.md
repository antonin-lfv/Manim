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
		- [(a-b)²](#a-b)
		- [a²-b²](#a-b-1)
	- [Texte en couleur et entouré](#Texte-en-couleur-et-entouré)    
	- [Aligner du texte](#Aligner-du-texte)
	- [Ligne couleurs gradient](#Ligne-couleurs-gradient)
	- [Animation carré déformé](#Animation-carré-déformé)
	- [Déplacement disque](#Déplacement-disque)
	- [Distance Euclidienne](#Distance-Euclidienne)
2. [Graphiques 2D](#Graphiques-2D)
	- [Régression linéaire](#régression-linéaire)
	- [Polygone](#Polygone)
	- [Ligne verticale sous une courbe](#Ligne-verticale-sous-une-courbe)
	- [Sigmoid](#Sigmoid)
	- [Évolution d'une épidémie](#évolution-dune-épidémie)
	- [Skewness et kurtosis](#Skewness-et-kurtosis)
3. [Graphiques 3D](#Graphiques-3D)
	- [Descente de Gradient](#Descente-de-Gradient)
	- [Animation surfaces](#Animations-surfaces)
4. [Animations SVG](#Animations-SVG)
	- [Stickman](#Stickman)
	- [Zoom sur un neurone](#zoom-sur-un-neurone)


# Exemples basiques

<br/>

## Formules latex

<br/>
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

<br/>
## (a-b)²

<br/>
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

## a²-b²

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
<br/>

## Texte en couleur et entouré

<br/>
<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/117121735-4ee07f80-ad95-11eb-92b4-addd94c2ad31.gif" height="350">
<p/>

<details>
  <summary>Code</summary>

```py
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
```
</details>
<br/>

## Aligner du texte

<br/>
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

<br/>
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

<br/>
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

<br/>
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

<br/>
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

## Régression linéaire

<br/>
<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/117119618-9d404f00-ad92-11eb-986f-e9c938be8e57.gif" height="350">
<p/>

<details>
  <summary>Code</summary>

```py
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
```
</details>

## Polygone

<br/>
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

<br/>
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

<br/>
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

<br/>
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

<br/>
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

## Animation surfaces

<br/>
<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/117125122-6f123d80-ad99-11eb-8368-f7b8c3581c28.gif" height="350">
<p/>

<details>
  <summary>Code</summary>

```py
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
```

</details>
<br/>

# Animations SVG

<br/>

## Stickman

<br/>
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

## Zoom sur un neurone

<br/>
<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/117122527-489ed300-ad96-11eb-8412-109ec39eaf10.gif" height="350">
<p/>

<details>
  <summary>Code</summary>

```py
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
