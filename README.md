# Anticosti Expedition Map (2025)/ La carte d'expédition sur l'île d'Anticosti (2025)

(EN) This repository accompanies a field report for a research expedition taken to Anticosti Island, funded through the Fonds de recherche du Québec- Nature et Technologies (FRQNT). The main objective of the expedition and larger project is to characterize waterbodies by physicochemical, geological, and biological variables and collect water and fish biological samples across the island’s distinct environments. The research trip was conducted on foot, sampling rivers and streams within one kilometer of the river mouth at three sampling points: the river mouth, 500 meters upstream, and 1000 meters upstream. These sampling sites corresponded to the IUCN-nominated coastal biodiversity buffer zone for the Anticosti Biodiversity Reserve boundary, which is considered the largest global representation of Ordovician period biodiversity (IUCN Evaluation Report, 2023). Lagoons, lakes, and ponds were also sampled at multiple points along shorelines, with sampling points 500 meters apart. The sampling trip consisted of two primary sampling teams as well as support from scientists from Patrimoine mondial Anticosti, Ministère de l’Environnement, de la Lutte contre les changements climatiques, de la Faune et des Parcs, residents, and visitors on the island. One sampling team, which sampled from June 26th to July 3rd, 2025, consisted of a faculty advisor, Dr. David Deslauriers (Professor of Biology UQAR/ISMER), a Master’s student, Gabriel Moy, and a research assistant, Andrée-Ann Pinard. The second sampling team sampled from July 2nd to July 10, 2025, and consisted of a postdoctoral researcher, Dr. Peyton Thomas, and volunteers from the United States, Shirley Gao, Kelly Peuquet, and Brendan Davis. 

Following the sampling, the next steps are to assess the similarities and differences among waterbodies sampled and sampling sites within waterbodies. Here, the research team will assess differences in species presence, addressing both broad biodiversity and the presence/absence of Brook trout and Atlantic salmon at the sampling time period. The team will analyze Brook trout otoliths from fish sampled across the island and water samples for trace metals to characterize the waterbodies geological signatures and assess the migratory history of Brook trout on the island.

This repository contains an interactive map of an Anticosti Island field expedition to collect water for environmental DNA (eDNA) and trace metals, as well as fish caught opportunistically. Here we share the map along with the data and code used to generate it.

(FR) Ce dépôt accompagne un rapport de terrain rédigé dans le cadre d'une expédition de recherche menée sur l'île d'Anticosti, financée par le Fonds de recherche du Québec - Nature et technologies (FRQNT). L'objectif principal de l'expédition et du projet dans son ensemble est de caractériser les plans d'eau à l'aide de variables physicochimiques, géologiques et biologiques, et de prélever des échantillons d'eau et de poissons dans les différents environnements de l'île. Le voyage de recherche s'est déroulé à pied, avec des prélèvements dans les rivières et les ruisseaux situés à moins d'un kilomètre de l'embouchure de la rivière, à trois points d'échantillonnage : l'embouchure de la rivière, 500 mètres en amont et 1 000 mètres en amont. Ces sites d'échantillonnage correspondaient à la zone tampon de biodiversité côtière désignée par l'UICN pour la limite de la réserve de biodiversité d'Anticosti, considérée comme la plus grande représentation mondiale de la biodiversité de la période ordovicienne (rapport d'évaluation de l'UICN, 2023). Des lagunes, des lacs et des étangs ont également été échantillonnés à plusieurs endroits le long des côtes, avec des points d'échantillonnage espacés de 500 mètres. Le voyage d'échantillonnage a été mené par deux équipes principales, avec le soutien de scientifiques de Patrimoine mondial Anticosti, du ministère de l'Environnement, de la Lutte contre les changements climatiques, de la Faune et des Parcs, ainsi que de résidents et de visiteurs de l'île.

Après l'échantillonnage, les étapes suivantes consistent à évaluer les similitudes et les différences entre les plans d'eau échantillonnés et les sites d'échantillonnage au sein de ces plans d'eau. L'équipe de recherche évaluera les différences dans la présence des espèces, en tenant compte à la fois de la biodiversité globale et de la présence ou de l'absence de l'omble de fontaine et du saumon de l'Atlantique au moment de l'échantillonnage. L'équipe analysera les otolithes des ombles de fontaine provenant des poissons prélevés sur l'île et les échantillons d'eau pour détecter la présence de métaux traces afin de caractériser les signatures géologiques des plans d'eau et d'évaluer l'histoire migratoire de l'omble de fontaine sur l'île.

Ce référentiel contient une carte interactive d'une expédition sur le terrain à l'île d'Anticosti visant à collecter de l'eau pour l'ADN environnemental (ADNe) et les métaux traces, ainsi que les poissons capturés de manière opportuniste. Nous partageons ici la carte ainsi que les données et le code utilisés pour la générer.

## View the Map/Voir la carte
(EN) The live interactive map is hosted on GitHub Pages:

👉 [View Map](https://peyton-thomas.github.io/expedition-map/)

(FR) La carte interactive en direct est hébergée sur GitHub Pages :

👉 [Voir la carte](https://peyton-thomas.github.io/expedition-map/)

## Repository Contents/ Le contenu du référentiel
expedition-map/
├── expedition_map.html # Interactive map (open in browser)
├── expedition_map.py # Python script used to generate the map
├── anticosti25_map.csv # Expedition site data (lat/lon, metadata, photos)
├── gpx/ # GPS track files
│ ├── day1-2025-06-26.gpx
│ ├── day2-2025-06-27.gpx
│ └── ...
├── images/ # Field photos (linked in the CSV)
│ ├── site1_photo1.jpg
│ ├── site2_photo1.jpg
│ └── ...
└── README.md # Documentation

---

## How to Regenerate the Map/ Comment régénérer la carte
(EN)
1. Clone this repository:
   ```bash
   git clone https://github.com/peyton-thomas/expedition-map.git
   cd expedition-map
## Install folium
pip install folium pandas gpxpy

## Run Python script
python expedition-map.py

## Rename map file
mv expedition_map.html index.html

## Commit and refresh changes
git add .
git commit -m "update expedition map"
git push
(FR)
1. Cloner ce dépôt 
   ```bash
   git clone https://github.com/peyton-thomas/expedition-map.git
   cd expedition-map
## Installer folium
pip install folium pandas gpxpy

## Exécuter le script Python
python expedition-map.py

## Renommer le fichier de carte
mv expedition_map.html index.html

## Valider et actualiser les modifications
git add .
git commit -m "update expedition map"
git push


