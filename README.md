# Road-Traffic-Monitoring-Based-on-Integration-of-Internet-of-Things-and-Machine-Learning

** Le probleme : Vu l'augmentation de nombre des véhicules circulants, il est devenu nécessaire de veiller à la sécurité des conducteurs et les piétons et gérer le trafic routier. Ceci a obligé les résponsables du trafic routier à prendre des mésures pour garantir de bonne habitudes de conduite et une conduite sùr sur les routes.

** Le public : les conducteurs, les responsables de gestion du trafic.

** La valeur : garantir la fluidité du trafic routier, essayer de trouver des nouvelles solutions pour mettre fin aux bouchons

" en tant que conducteur, la solution vehicle_detection me permet d'éviter l'embouteillage "

" en tant que responsable de la gestion du trafic, cette solution me permet d'analyser le trafic routier, les habitudes de conduite et les périodes ou il y a beaucoup d'embouteillage et donc chercher des solutions."

** La solution technique : implémenter un système de détection des véhicules dans une scène video capable de surveiller le trafic routier et fournir en temps réel des informations sur le comportement des véhicules et les piétons sur les différentes routes. Cette solution est basée sur des outils open source et à faible coût de développement.
Principe :
1) Capturer une vidéo, une série des photos ou directement via une camera.
2) Détecter en temps réels les objets qui figurent sur les images capturées.
3) Classifier les objets détectés selon leurs types grace au model de réseaux de neurone convolutifs SSDLite Mobilenet v2
4) Extraire la classe des véhicules.
5) Compter le nombre des véhicules détectés.
6) Afficher le nombre des véhicules détectés sur les séries d’images de sortie.
7) Afficher en temps réel le nombre des véhicules détectés sur une interface web basée sur html/css/javascript coté client et javascript/node.js coté serveur. 
