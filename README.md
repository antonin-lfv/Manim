<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116782710-0b330080-aa8b-11eb-9add-3fb93a94655d.png" height="200">
<p/>

<br/>

<p align="center">
Dans ce Github je vais partager des animations réalisées avec Manim, une librairie python développée par le YouTubeur 3Blue1Brown, qui permet de créer des animations de façon puissante et épurée. J'utilise ici la version 4.0 de Manim CE (Community Edition) qui est la version de Manim régulièrement mise à jour par la communauté et qui est la plus stable. Si voulez utilisez Manim l'installation est détaillée sur le site Manim community. 
<br/>
<p/>


## Animation pour comprendre ce qu'est le kurtosis et le skewness

<br/> 

<p align="center">
	  <img src="https://user-images.githubusercontent.com/63207451/116785188-7b944e80-aa98-11eb-94a0-020071958081.gif" height="500">
<p/>

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

<br/>

<p align="center"><a href="#Animation-pour-comprendre-ce-qu'est-le-kurtosis-et-le-skewness"><img src="http://randojs.com/images/backToTopButton.png" alt="Haut de la page" height="29"/></a></p>

<br/>


<p align="center">
  <a href="https://github.com/antonin-lfv" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97302854-e484da80-1859-11eb-9374-5b319ca51197.png" title="GitHub" width="40" height="40"></a>
  <a href="https://www.linkedin.com/in/antonin-lefevre-565b8b141" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303444-b2c04380-185a-11eb-8cfc-864c33a64e4b.png" title="LinkedIn" width="40" height="40"></a>
  <a href="mailto:antoninlefevre45@icloud.com" class="fancybox" ><img src="https://user-images.githubusercontent.com/63207451/97303543-cec3e500-185a-11eb-8adc-c1364e2054a9.png" title="Mail" width="40" height="40"></a>
</p>


---------------------------
