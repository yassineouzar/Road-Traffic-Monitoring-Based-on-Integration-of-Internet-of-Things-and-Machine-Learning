# Road-Traffic-Monitoring-Based-on-Integration-of-Internet-of-Things-and-Machine-Learning

** Le probleme : Vu l'augmentation de nombre des véhicules circulants et le problème d'embouteillage qu'on rencontre souvent, il est devenu nécessaire de trouver des solutions pour garantir la fluidité du trafic routier. 
Les solutions existantes sont basées sur les données des utilisateurs tels que la position et la vitesse pour fournir les iténéraires les plus rapides, Mais les travaux de recherches les plus récents utilisent les méthodes du machine learning pour surveiller le trafic routier. Dans ce contexte je propose une solution basée sur la détection et comptage des véhicules dans une scène video pour la prédiction de l'état du trafic, les résultats peuvent etre visualiser sur une interface web.

** Le public : 
    -les conducteurs
    -les responsables de gestion du trafic.

** La valeur : 
    -garantir la fluidité du trafic routier.
    -Analyser les périodes d'embouteillages, comportement des véhicules sur les routes afin de trouver des nouvelles solutions pour mettre      fin aux bouchons.
    -faible cout.
    -traitement se fait en local, donc il n'est pas nécessaire d'utiliser des serveurs.
    -solution basée sur des outils open source.

" en tant que conducteur: la solution vehicle_detection me permet d'éviter l'embouteillage "

" en tant que responsable de la gestion du trafic: cette solution me permet d'analyser le trafic routier, les habitudes de conduite et les périodes d'embouteillage pour chercher des solutions."

** La solution technique : implémenter un système de détection des véhicules dans une scène video capable de surveiller le trafic routier et fournir en temps réel des informations sur le comportement des véhicules et les piétons sur les différentes routes. Cette solution est basée sur des outils open source et à faible coût de développement.

-Principe :
1) Capturer une vidéo, une série des photos ou directement via une camera.
2) Détecter en temps réels les objets qui figurent sur les images capturées.
3) Classifier les objets détectés selon leurs types grace au model de réseaux de neurone convolutifs SSDLite Mobilenet v2
4) Extraire la classe des véhicules.
5) Compter le nombre des véhicules détectés.
6) Afficher le nombre des véhicules détectés sur les séries d’images de sortie.
7) Afficher en temps réel le nombre des véhicules détectés sur une interface web basée sur html/css/javascript coté client et javascript/node.js coté serveur. 
